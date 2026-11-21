#!/usr/bin/env python3
"""
BTC 5-minute UP/DOWN signal bot, 24/7 edition (runs on GitHub Actions).

ADVISORY ONLY: it places no trades, uses no API keys and needs no packages (Python 3.8+ standard library).

What it does, every 5-minute window (aligned to :00, :05, :10 ...):
  1. About SIGNAL_MINUTE minutes in, it reads Coinbase prices and order book and predicts UP or DOWN.
  2. It reads Polymarket's live Up and Down prices and decides by edge: only the side it leans toward,
     and only when its probability beats the price plus a fee allowance by MIN_EDGE.
  3. When the window ends it records Coinbase's result, then later reads Polymarket's OWN result
     (only once the market is closed and its prices are exactly 1 and 0) and uses that instead.
  4. It learns from every window, using Polymarket's result when it has it.

Files it writes (committed back to the repo every 30 minutes):
  STATUS.md        a readable report (open this on your phone)
  data/log.csv     every window: probability, prices, bet, result and where the result came from
  data/model.json  what the bot has learned
"""
import csv
import json
import math
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

# ---------------------------------------------------------------- settings
def env_num(name, default):
    try:
        return float(os.environ.get(name, "") or default)
    except ValueError:
        return float(default)

M = int(env_num("SIGNAL_MINUTE", 2))          # minutes into each window when the signal is made (1-4)
MIN_EDGE = env_num("MIN_EDGE", 0.02)          # needed edge after fees, as a fraction (0.02 = 2 cents)
FEE = env_num("FEE", 0.02)                    # fee and slippage allowance per share
MIN_CONF = env_num("MIN_CONF", 0.55)          # confidence needed only when Polymarket's price is unavailable
BACKFILL_DAYS = int(env_num("BACKFILL_DAYS", 7))
RUN_SECONDS = int(env_num("RUN_SECONDS", 20100))   # how long one job keeps making signals (5h35m)
PUSH_EVERY = 1800                              # seconds between commits of the data files
TRAIN_FALLBACK = 1500                          # learn from Coinbase's result if Polymarket's has not settled by then
TRACK_EVERY = 20                               # seconds between price checks while a window is running (limit order study)
LIMIT_OFFSETS = (0, 0.02, 0.04, 0.06, 0.08)    # limit prices tested: the bot's fair price minus each of these

WINDOW = 300
EXTRA = 2
NFEAT = 9 + EXTRA
LR, L2 = 0.01, 1e-3
CAL_EDGES = [0.5, 0.55, 0.6, 0.65, 0.7, 0.8, 0.9, 1.01]
CLOSE_USD = 50
DATA_DIR = "data"
LOG_FILE = os.path.join(DATA_DIR, "log.csv")
MODEL_FILE = os.path.join(DATA_DIR, "model.json")
STATUS_FILE = "STATUS.md"
CB = "https://api.exchange.coinbase.com/products/BTC-USD"

NOW = time.time       # replaceable so the bot can be tested on a fake clock
SLEEP = time.sleep
LATEST = None         # the most recent call, shown at the top of STATUS.md


def say(*a):
    print(datetime.now(timezone.utc).strftime("%H:%M:%S"), *a, flush=True)


# ---------------------------------------------------------------- web
def http_json(url, timeout=12):
    req = urllib.request.Request(url, headers={"User-Agent": "btc-signal-bot/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch(url, tries=3, timeout=12):
    for i in range(tries):
        try:
            return http_json(url, timeout)
        except Exception:
            if i == tries - 1:
                raise
            SLEEP(1.5 * (i + 1))


def fetch_or_none(url, timeout=8):
    try:
        return http_json(url, timeout)
    except Exception:
        return None


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def get_candles(start, end):
    """{minute_ts: (open, high, low, close, volume)} for 1-minute Coinbase candles in [start, end]."""
    out = {}
    t = start - start % 60
    while t < end:
        t2 = min(t + 300 * 60, end)
        q = urllib.parse.urlencode({"granularity": 60, "start": iso(t), "end": iso(t2)})
        for row in fetch(f"{CB}/candles?{q}"):
            ts, lo, hi, op, cl, vol = row[:6]
            out[int(ts)] = (float(op), float(hi), float(lo), float(cl), float(vol))
        t = t2
        SLEEP(0.15)
    return out


def get_book():
    j = fetch_or_none(f"{CB}/book?level=2", 10)
    return book_imbalance(j) if j else None


def live_ask(token_id):
    j = fetch_or_none("https://clob.polymarket.com/price?token_id=" + urllib.parse.quote(str(token_id)) + "&side=BUY", 6)
    try:
        v = float(j["price"])
    except Exception:
        return None
    return v if 0 < v < 1 else None


def parse_listish(v):
    return json.loads(v) if isinstance(v, str) else v


def get_odds(W):
    """What it costs right now to buy one Up share and one Down share: {'up': ..., 'down': ...} or None."""
    try:
        j = fetch_or_none("https://gamma-api.polymarket.com/events?slug=btc-updown-5m-%d" % W, 6)
        mk = j[0]["markets"][0]
        outs = [str(o).lower() for o in parse_listish(mk["outcomes"])]
        ids = parse_listish(mk["clobTokenIds"])
        iu, idn = outs.index("up"), outs.index("down")
        up, dn = live_ask(ids[iu]), live_ask(ids[idn])
        if up is None and dn is None:
            return None
        return {"up": up, "down": dn, "ids": {"up": ids[iu], "down": ids[idn]}}
    except Exception:
        return None


def official_from_market(ev, mk):
    """Polymarket's official result, but only once settled: closed, with prices of exactly 1 and 0.
    Before that the prices are just live trading prices and must never be mistaken for a result."""
    try:
        done = (mk.get("closed") is True or (ev or {}).get("closed") is True
                or str(mk.get("umaResolutionStatus") or "").lower() == "resolved")
        if not done:
            return None
        outs = [str(o).lower() for o in parse_listish(mk["outcomes"])]
        pr = parse_listish(mk["outcomePrices"])
        pu, pd = float(pr[outs.index("up")]), float(pr[outs.index("down")])
        if pu >= 0.9999 and pd <= 0.0001:
            return "UP"
        if pd >= 0.9999 and pu <= 0.0001:
            return "DOWN"
    except Exception:
        pass
    return None


def get_official(W):
    j = fetch_or_none("https://gamma-api.polymarket.com/events?slug=btc-updown-5m-%d" % W, 8)
    try:
        ev = j[0]
        return official_from_market(ev, ev["markets"][0])
    except Exception:
        return None


# ---------------------------------------------------------------- features
def clip(v, lim):
    return max(-lim, min(lim, v))


def mean(a):
    return sum(a) / len(a)


def std(a):
    if len(a) < 2:
        return 0.0
    m = mean(a)
    return math.sqrt(sum((v - m) ** 2 for v in a) / len(a))


def features(c, W, m):
    """The 9 price-based inputs, using only candles complete before W + m*60."""
    t_end = W + m * 60
    if W not in c:
        return None
    if any(t not in c for t in range(t_end - 1800, t_end, 60)):
        return None
    ts = [t for t in range(t_end - 3600, t_end, 60) if t in c]
    closes = [c[t][3] for t in ts]
    opens = [c[t][0] for t in ts]
    vols = [c[t][4] for t in ts]
    rets = [math.log(closes[i] / closes[i - 1]) for i in range(1, len(closes))]
    s = max(std(rets[-30:]), 1e-5)
    cur = closes[-1]
    z_win = math.log(cur / c[W][0]) / (s * math.sqrt(m))
    mom1 = rets[-1] / s
    mom3 = math.log(cur / closes[-4]) / (s * math.sqrt(3))
    mom15 = math.log(cur / closes[-16]) / (s * math.sqrt(15))
    s5 = max(std(rets[-5:]), 1e-6)
    s_all = max(std(rets), 1e-6)
    vol_ratio = math.log(s5 / s_all)
    v3 = max(mean(vols[-3:]), 1e-9)
    vol_surge = math.log(v3 / max(mean(vols), 1e-9))
    last10 = list(zip(opens[-10:], closes[-10:]))
    green = (sum(1 for o, cl in last10 if cl > o) / len(last10) - 0.5) * 4
    dt = datetime.fromtimestamp(t_end, timezone.utc)
    h = (dt.hour + dt.minute / 60) / 24 * 2 * math.pi
    return [clip(z_win, 4), clip(mom1, 4), clip(mom3, 4), clip(mom15, 4),
            clip(vol_ratio, 3), clip(vol_surge, 3), green, math.sin(h), math.cos(h)]


def book_imbalance(book):
    """(bid size - ask size) / total near the mid price, at 0.1% and 0.02% depth. None if the book is unusable."""
    try:
        bids = [(float(r[0]), float(r[1])) for r in book["bids"]]
        asks = [(float(r[0]), float(r[1])) for r in book["asks"]]
        if not bids or not asks:
            return None
        bb, ba = max(p for p, _ in bids), min(p for p, _ in asks)
        mid = (bb + ba) / 2
        if not mid > 0 or ba < bb:
            return None

        def at(frac):
            b = sum(s for p, s in bids if p >= mid * (1 - frac))
            a = sum(s for p, s in asks if p <= mid * (1 + frac))
            return (b - a) / (b + a) if (a + b) > 0 else 0.0
        return [at(0.001), at(0.0002)]
    except Exception:
        return None


def label(c, W):
    """1 if the window closed at or above its open (Polymarket 'Up'), 0 if below, None if data is missing."""
    if W not in c or W + 240 not in c:
        return None
    return 1 if c[W + 240][3] >= c[W][0] else 0


# ---------------------------------------------------------------- model
def cal_bin(conf):
    for i in range(len(CAL_EDGES) - 1):
        if conf < CAL_EDGES[i + 1]:
            return i
    return len(CAL_EDGES) - 2


class Model:
    def __init__(self, minute):
        self.minute = minute
        self.w = [0.0] * NFEAT
        self.b = 0.0
        self.n = 0
        self.hist = []                                        # [lean was right, was a confident call]
        self.calib = [[0, 0.0, 0] for _ in CAL_EDGES[1:]]     # per confidence band: windows, sum of confidence, right
        self.backfilled = False
        self.pending = []                                     # finished windows waiting to be learned from

    def predict(self, x):
        z = self.b + sum(a * b for a, b in zip(self.w, x))
        z = max(-30.0, min(30.0, z))
        return 1 / (1 + math.exp(-z))

    def update(self, x, y):
        g = self.predict(x) - y
        for i in range(NFEAT):
            self.w[i] -= LR * (g * x[i] + L2 * self.w[i])
        self.b -= LR * g
        self.n += 1

    def learn(self, x, p, called, y):
        """Learn from one finished window; p is the probability the bot gave before it knew the result."""
        conf = max(p, 1 - p)
        correct = (p >= 0.5) == (y == 1)
        self.update(x, y)
        self.hist.append([int(correct), int(called)])
        self.hist = self.hist[-1000:]
        r = self.calib[cal_bin(conf)]
        r[0] += 1
        r[1] += conf
        r[2] += int(correct)

    def save(self):
        with open(MODEL_FILE, "w") as f:
            json.dump(self.__dict__, f)

    @staticmethod
    def load(minute):
        if not os.path.exists(MODEL_FILE):
            return None
        try:
            with open(MODEL_FILE) as f:
                d = json.load(f)
            if d.get("minute") != minute or len(d.get("w", [])) != NFEAT:
                say("Saved model used a different setup; starting fresh.")
                return None
            mdl = Model(minute)
            mdl.__dict__.update(d)
            return mdl
        except Exception:
            say("Could not read the saved model; starting fresh.")
            return None


def backfill(model, days):
    end = int(NOW() // WINDOW * WINDOW)
    start = end - days * 86400
    say("Learning from the last %d days of history..." % days)
    c = get_candles(start - 3600, end)
    n = 0
    for W in range(start, end, WINDOW):
        x0, y = features(c, W, M), label(c, W)
        if x0 is None or y is None:
            continue
        x = x0 + [0.0] * EXTRA
        p = model.predict(x)
        model.learn(x, p, max(p, 1 - p) >= MIN_CONF, y)
        n += 1
    model.backfilled = True
    say("Learned from %d past windows." % n)


# ---------------------------------------------------------------- decisions and scoring
def best_side(p_up, up, dn, fee):
    """Edge on the side the bot leans toward: its probability minus the price to buy it minus a fee allowance.
    It never bets against its own lean."""
    side = "UP" if p_up >= 0.5 else "DOWN"
    prob = p_up if side == "UP" else 1 - p_up
    ask = up if side == "UP" else dn
    if not isinstance(ask, (int, float)):
        return None
    return {"side": side, "prob": prob, "ask": ask, "net": prob - ask - fee}


def evaluate(rows, thr, fee):
    """Replays logged windows: bets a minimum-edge rule would have made, wins, and average profit per share."""
    n = w = 0
    s = 0.0
    for r in rows:
        b = best_side(r["p"], r.get("upAsk"), r.get("dnAsk"), fee)
        if not b or b["net"] < thr - 1e-9:
            continue
        win = r["outcome"] == b["side"]
        n += 1
        w += 1 if win else 0
        s += (1 - b["ask"] if win else -b["ask"]) - fee
    return n, w, (s / n if n else None)


def is_close(r):
    return r["src"] != "polymarket" and isinstance(r.get("mv"), (int, float)) and abs(r["mv"]) < CLOSE_USD


# ---------------------------------------------------------------- log file
HEAD = ["window_start_utc", "signal_minute", "bot_p_up", "lean", "polymarket_up_ask", "polymarket_down_ask",
        "bet", "basis", "net_edge", "outcome", "bet_result", "book_imbalance_wide", "book_imbalance_near",
        "window_open", "price_at_signal", "coinbase_move_usd", "close_call", "result_source", "coinbase_outcome",
        "lean_min_ask", "lean_ask_path"]


def fnum(s):
    try:
        return float(s) if s not in ("", None) else None
    except ValueError:
        return None


def write_log(rows):
    os.makedirs(DATA_DIR, exist_ok=True)
    tmp = LOG_FILE + ".tmp"
    with open(tmp, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEAD)
        for r in rows:
            bet = r.get("bet")
            w.writerow([iso(r["W"]), r["m"], r["p"], r["lean"], r.get("upAsk", ""), r.get("dnAsk", ""),
                        bet or "", r.get("basis", ""), "" if r.get("net") is None else r["net"], r["outcome"],
                        ("win" if bet == r["outcome"] else "loss") if bet else "",
                        "" if r.get("imbW") is None else r["imbW"], "" if r.get("imbN") is None else r["imbN"],
                        r.get("open", ""), r.get("cur", ""), r.get("mv", ""),
                        ("yes" if is_close(r) else "no") if isinstance(r.get("mv"), (int, float)) else "",
                        "polymarket" if r["src"] == "polymarket" else "coinbase", r["cb"],
                        "" if r.get("lmin") is None else r["lmin"], r.get("lpath", "")])
    os.replace(tmp, LOG_FILE)


def load_log():
    rows = []
    if not os.path.exists(LOG_FILE):
        return rows
    try:
        with open(LOG_FILE, newline="") as f:
            for d in csv.DictReader(f):
                W = int(datetime.strptime(d["window_start_utc"], "%Y-%m-%dT%H:%M:%SZ")
                        .replace(tzinfo=timezone.utc).timestamp())
                rows.append({
                    "W": W, "m": int(d["signal_minute"]), "p": float(d["bot_p_up"]), "lean": d["lean"],
                    "upAsk": fnum(d["polymarket_up_ask"]), "dnAsk": fnum(d["polymarket_down_ask"]),
                    "bet": d["bet"] or None, "basis": d["basis"], "net": fnum(d["net_edge"]),
                    "outcome": d["outcome"], "src": "polymarket" if d["result_source"] == "polymarket" else "coinbase",
                    "cb": d["coinbase_outcome"] or d["outcome"], "imbW": fnum(d["book_imbalance_wide"]),
                    "imbN": fnum(d["book_imbalance_near"]), "open": fnum(d["window_open"]),
                    "cur": fnum(d["price_at_signal"]), "mv": fnum(d["coinbase_move_usd"]),
                    "lmin": fnum(d.get("lean_min_ask")), "lpath": d.get("lean_ask_path") or ""})
    except Exception as e:
        say("Could not fully read the log (%s); continuing with %d rows." % (e, len(rows)))
    return rows


# ---------------------------------------------------------------- report
def et(W):
    try:
        from zoneinfo import ZoneInfo
        return datetime.fromtimestamp(W, ZoneInfo("America/New_York")).strftime("%b %d %I:%M %p ET").replace(" 0", " ")
    except Exception:
        return datetime.fromtimestamp(W, timezone.utc).strftime("%b %d %H:%M UTC")


def pct(v):
    return "n/a" if v is None else "%d%%" % round(v * 100)


def md_table(head, body):
    lines = ["| " + " | ".join(head) + " |", "|" + "|".join(["---"] * len(head)) + "|"]
    lines += ["| " + " | ".join(str(c) for c in r) + " |" for r in body]
    return "\n".join(lines)


def edge_table(rows):
    body = []
    # "Every call" acts as if every call, even a skip, had been bought at the price shown when it was made.
    for thr, name in ((-1.0, "Every call"), (0, "+0¢"), (0.02, "+2¢"), (0.04, "+4¢"), (0.06, "+6¢"), (0.08, "+8¢")):
        n, w, avg = evaluate(rows, thr, FEE)
        body.append([name, n, pct(w / n) if n else "—", "—" if avg is None else "%+.1f¢" % (avg * 100)])
    return md_table(["Min edge", "Bets", "Win rate", "Avg per bet"], body)


def limit_sim(rows):
    """Limit order study on skipped windows. A resting buy order at price L on the bot's lean is assumed filled if the
    lowest ask seen during the window reached L or lower. That is optimistic: a real order may not be filled."""
    skipped = [r for r in rows if not r.get("bet") and r.get("lmin") is not None]
    out = []
    for off in LIMIT_OFFSETS:
        n = f = w = 0
        s = 0.0
        for r in skipped:
            L = max(r["p"], 1 - r["p"]) - off
            if L <= 0.01:
                continue
            n += 1
            if r["lmin"] <= L + 1e-9:
                f += 1
                win = r["outcome"] == r["lean"]
                w += 1 if win else 0
                s += (1 - L if win else -L) - FEE
        out.append((off, n, f, w, s))
    return len(skipped), out


def limit_section(rows):
    n_sk, res = limit_sim(rows)
    o = ["## Limit order test", "",
         "What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? "
         "The bot checks Polymarket's price every %d seconds and counts an order as filled if the lowest ask reached your price. "
         "That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **%d**." % (TRACK_EVERY, n_sk), ""]
    body = []
    for off, n, f, w, s in res:
        body.append(["Fair" if off == 0 else "Fair −%d¢" % round(off * 100), n, f, pct(f / n) if n else "—",
                     pct(w / f) if f else "—", "—" if not f else "%+.1f¢" % (s / f * 100),
                     "—" if not n else "%+.1f¢" % (s / n * 100)])
    o += [md_table(["Limit price", "Windows", "Filled", "Fill rate", "Won when filled", "Avg per fill", "Avg per window"], body), "",
          "If \"Won when filled\" sits below the price you paid, the fills are catching windows that moved against you.", ""]
    return o


def hm(ts):
    try:
        from zoneinfo import ZoneInfo
        return datetime.fromtimestamp(ts, ZoneInfo("America/New_York")).strftime("%I:%M %p").lstrip("0")
    except Exception:
        return datetime.fromtimestamp(ts, timezone.utc).strftime("%H:%M UTC")


def latest_call_md(cur):
    """The newest call as a short block for the top of STATUS.md."""
    if not cur:
        return ["## Latest call", "", "Waiting for the next signal. A call appears about %d minutes into each 5-minute window." % M, ""]
    lean, prob = cur["lean"], max(cur["p"], 1 - cur["p"])
    ask = cur["upAsk"] if lean == "UP" else cur["dnAsk"]
    head = ("**%s BET %s**" % ("▲" if cur["bet"] == "UP" else "▼", cur["bet"])) if cur["bet"] else "**SKIP**"
    detail = "Bot leans %s %s" % (lean, pct(prob))
    detail += (", %s costs %d¢" % (lean, round(ask * 100))) if ask is not None else ", no Polymarket price available"
    if cur.get("net") is not None:
        detail += ", edge %+d¢ after fees" % round(cur["net"] * 100)
    return ["## Latest call", "", "%s for the window %s to %s" % (head, hm(cur["W"]), hm(cur["W"] + WINDOW)), "",
            detail + ".", "",
            "Called at %s. The result is known at %s. Reload this page for the next call." % (hm(cur.get("at", cur["W"])), hm(cur["W"] + WINDOW)), ""]


def build_report(rows, model, started):
    now = NOW()
    priced = [r for r in rows if r.get("upAsk") is not None or r.get("dnAsk") is not None]
    confirmed = [r for r in rows if r["src"] == "polymarket"]
    last50 = rows[-50:]
    cov = sum(1 for r in last50 if r.get("upAsk") is not None or r.get("dnAsk") is not None)
    last100 = rows[-100:]
    right100 = sum(1 for r in last100 if r["lean"] == r["outcome"]) / len(last100) if last100 else None
    o = ["# BTC 5-minute signal bot", "",
         "Last update: **%s** (this job started %s)" % (et(now), et(started)), ""] + latest_call_md(LATEST) + [
         "## Summary", "",
         "- Windows logged: **%d**" % len(rows),
         "- Result confirmed by Polymarket: **%d** (other windows use Coinbase's result until Polymarket's settles)" % len(confirmed),
         "- Polymarket prices captured: **%d of the last %d** windows" % (cov, len(last50)),
         "- Bot's lean was right in **%s** of the last %d windows" % (pct(right100), len(last100)),
         "- Bot has learned from **%d** windows" % model.n,
         "- Settings: signal %d min in, minimum edge %d¢, fee allowance %d¢" % (M, round(MIN_EDGE * 100), round(FEE * 100)),
         "", "## Versus Polymarket prices", "",
         "Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.",
         "", "**All windows with a price (%d)**" % len(priced), "", edge_table(priced), "",
         "**Only windows whose result Polymarket confirmed (%d)**" % len([r for r in priced if r["src"] == "polymarket"]), "",
         edge_table([r for r in priced if r["src"] == "polymarket"]), ""]
    close_bets = [r for r in priced if is_close(r) and (best_side(r["p"], r.get("upAsk"), r.get("dnAsk"), FEE) or {"net": -9})["net"] >= MIN_EDGE - 1e-9]
    o += ["Unconfirmed close calls (Coinbase moved under $%d) among bets at your minimum edge: **%d**" % (CLOSE_USD, len(close_bets)), ""]
    o += limit_section(rows)
    o += ["## Calibration", ""]
    tot = sum(r[0] for r in model.calib)
    if tot:
        said = sum(r[1] for r in model.calib) / tot
        act = sum(r[2] for r in model.calib) / tot
        o += ["Across %d windows the bot claimed %s on average and was right %s." % (tot, pct(said), pct(act)), ""]
    body = []
    for i, r in enumerate(model.calib):
        lo, hi = round(CAL_EDGES[i] * 100), min(100, round(CAL_EDGES[i + 1] * 100))
        body.append(["%d%%+" % lo if i == len(model.calib) - 1 else "%d-%d%%" % (lo, hi), r[0],
                     pct(r[1] / r[0]) if r[0] else "—", pct(r[2] / r[0]) if r[0] else "—"])
    o += [md_table(["Bot said", "Windows", "Avg said", "Right"], body), "", "## Recent windows", ""]
    body = []
    for r in reversed(rows[-12:]):
        conf = max(r["p"], 1 - r["p"])
        ask = r.get("upAsk") if r["lean"] == "UP" else r.get("dnAsk")
        res = r["outcome"] + ((" ✓" if r["bet"] == r["outcome"] else " ✗") if r.get("bet") else "")
        body.append([et(r["W"]), "%s %s" % (r["lean"], pct(conf)), "n/a" if ask is None else "%d¢" % round(ask * 100),
                     r["bet"] or "skip", res, "Polymarket" if r["src"] == "polymarket" else ("Coinbase (close)" if is_close(r) else "Coinbase")])
    o += [md_table(["Window", "Bot", "Price", "Bet", "Result", "Source"], body), "",
          "Signals are advice only. No trades are placed. Not financial advice.", ""]
    return "\n".join(o)


def save_all(model, rows, started):
    os.makedirs(DATA_DIR, exist_ok=True)
    write_log(rows)
    model.save()
    with open(STATUS_FILE, "w") as f:
        f.write(build_report(rows, model, started))


def sh(*cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def push():
    """Commit the data files back to the repository so nothing is lost when the job ends."""
    if os.environ.get("NO_PUSH"):
        return
    branch = os.environ.get("GITHUB_REF_NAME") or "main"
    try:
        sh("git", "config", "user.name", "github-actions[bot]")
        sh("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
        sh("git", "add", DATA_DIR, STATUS_FILE)
        if sh("git", "diff", "--cached", "--quiet")[0] == 0:
            return
        sh("git", "commit", "-m", "Update bot data")
        for i in range(3):
            sh("git", "pull", "--rebase", "origin", branch)
            rc, out = sh("git", "push", "origin", "HEAD:" + branch)
            if rc == 0:
                say("Saved data to the repository.")
                return
            say("Push failed (try %d): %s" % (i + 1, out[-200:]))
            SLEEP(5)
    except Exception as e:
        say("Push error:", e)


# ---------------------------------------------------------------- the loop
def make_signal(W, model):
    c = get_candles(W - 3700, W + M * 60)
    x0 = features(c, W, M)
    if x0 is None:
        return None
    imb = get_book()
    x = x0 + ([clip(imb[0] * 2, 2), clip(imb[1] * 2, 2)] if imb else [0.0, 0.0])
    p = model.predict(x)
    conf = max(p, 1 - p)
    lean = "UP" if p >= 0.5 else "DOWN"
    called = conf >= MIN_CONF
    bet, basis, net = (lean if called else None), "conf", None
    odds = get_odds(W)
    if odds:
        b = best_side(p, odds.get("up"), odds.get("down"), FEE)
        if b:
            basis, net = "edge", b["net"]
            bet = b["side"] if b["net"] >= MIN_EDGE - 1e-9 else None
    cur = {"W": W, "m": M, "x": x, "p": round(p, 4), "lean": lean, "called": called, "bet": bet, "basis": basis,
           "net": None if net is None else round(net, 4), "upAsk": odds["up"] if odds else None,
           "dnAsk": odds["down"] if odds else None, "imbW": round(imb[0], 4) if imb else None,
           "imbN": round(imb[1], 4) if imb else None, "open": c[W][0], "cur": c[W + M * 60 - 60][3],
           "next": 0, "tries": 0, "at": NOW(), "tokens": (odds or {}).get("ids"), "track": [],
           "poll_at": NOW() + TRACK_EVERY}
    ask = cur["upAsk"] if lean == "UP" else cur["dnAsk"]
    if ask is not None:
        cur["track"].append((int(NOW() - W), ask))
    say("%s  leans %s %d%%  price %s  ->  %s" % (et(W), lean, round(conf * 100),
        "n/a" if ask is None else "%d¢" % round(ask * 100), ("BET " + bet) if bet else "skip"))
    return cur


def poll_track(cur, now):
    """While the window runs, note the price of the side the bot leans toward (for the limit order test)."""
    tok = (cur.get("tokens") or {}).get("up" if cur["lean"] == "UP" else "down")
    if not tok:
        cur["poll_at"] = float("inf")
        return
    cur["poll_at"] = now + TRACK_EVERY
    a = live_ask(tok)
    if a is not None:
        cur["track"].append((int(now - cur["W"]), a))


def write_live(cur, rows):
    """A small file the live web page reads to show the newest call without a reload."""
    last = rows[-1] if rows else None
    d = {"updated": int(NOW()), "W": cur["W"], "m": cur["m"], "at": int(cur["at"]), "window": WINDOW,
         "p": cur["p"], "lean": cur["lean"], "conf": round(max(cur["p"], 1 - cur["p"]), 4),
         "bet": cur["bet"], "basis": cur["basis"], "net": cur["net"], "upAsk": cur["upAsk"], "dnAsk": cur["dnAsk"],
         "open": cur["open"], "cur": cur["cur"], "tokens": cur.get("tokens"), "fee": FEE, "minEdge": MIN_EDGE,
         "last": ({"W": last["W"], "lean": last["lean"], "bet": last["bet"], "outcome": last["outcome"], "src": last["src"]}
                  if last else None)}
    os.makedirs(DATA_DIR, exist_ok=True)
    tmp = os.path.join(DATA_DIR, "live.json.tmp")
    with open(tmp, "w") as f:
        json.dump(d, f)
    os.replace(tmp, os.path.join(DATA_DIR, "live.json"))


def finish_window(cur, rows, by_w, model):
    W = cur["W"]
    c = get_candles(W - 60, W + WINDOW)
    y = label(c, W)
    if y is None:
        cur["tries"] += 1
        if cur["tries"] >= 6:
            say("Could not confirm the result for", et(W))
            return None
        cur["next"] = NOW() + 5
        return cur
    outcome = "UP" if y == 1 else "DOWN"
    row = {k: cur[k] for k in ("W", "m", "p", "lean", "upAsk", "dnAsk", "bet", "basis", "net", "imbW", "imbN", "open", "cur")}
    tr = cur.get("track") or []
    row.update({"outcome": outcome, "src": "coinbase", "cb": outcome, "mv": round(c[W + 240][3] - c[W][0], 2),
                "lmin": min(a for _, a in tr) if tr else None,
                "lpath": "|".join("%d:%.2f" % (t, a) for t, a in tr)})
    rows.append(row)
    by_w[W] = row
    model.pending.append({"W": W, "x": [round(v, 5) for v in cur["x"]], "p": cur["p"], "called": cur["called"], "y": y})
    say("%s  Coinbase result %s%s" % (et(W), outcome, (" (bet %s)" % ("won" if cur["bet"] == outcome else "lost")) if cur["bet"] else ""))
    return None


def reconcile(rows, by_w, next_try, now):
    """Looks for Polymarket's official result of recent windows (settlement can take several minutes)."""
    todo = [r for r in rows[-400:] if r["src"] != "polymarket" and 360 <= now - (r["W"] + WINDOW) <= 10800
            and next_try.get(r["W"], 0) <= now][:3]
    for r in todo:
        next_try[r["W"]] = now + 120
        off = get_official(r["W"])
        if off:
            if off != r["outcome"]:
                say("%s  Polymarket says %s, Coinbase said %s. Using Polymarket." % (et(r["W"]), off, r["outcome"]))
            r["outcome"], r["src"] = off, "polymarket"


def drain_training(model, by_w, now):
    """Learn from finished windows once Polymarket's result is known (or after a wait, from Coinbase's)."""
    keep = []
    for e in model.pending:
        row = by_w.get(e["W"])
        if row is None:
            continue
        if row["src"] == "polymarket":
            y = 1 if row["outcome"] == "UP" else 0
        elif now >= e["W"] + WINDOW + TRAIN_FALLBACK:
            y = e["y"]
        else:
            keep.append(e)
            continue
        model.learn(e["x"], e["p"], e["called"], y)
    model.pending = keep


def run():
    os.makedirs(DATA_DIR, exist_ok=True)
    rows = load_log()
    by_w = {r["W"]: r for r in rows}
    model = Model.load(M)
    started = NOW()
    if model is None or not model.backfilled:
        model = Model(M)
        backfill(model, BACKFILL_DAYS)
        save_all(model, rows, started)
        push()
    say("Running. %d windows logged so far. Signal %d min into each window." % (len(rows), M))
    end_at = NOW() + RUN_SECONDS
    global LATEST
    cur, last_sig, sig_retry, next_rec, errors = None, 0, 0, 0, 0
    next_try = {}
    last_push = NOW()
    try:
        while True:
            now = NOW()
            W = int(now // WINDOW * WINDOW)
            ph = now - W
            try:
                if cur is None and now >= end_at:
                    break
                if cur is not None:
                    if now >= cur["W"] + WINDOW + 5 and now >= cur["next"]:
                        cur = finish_window(cur, rows, by_w, model)
                        if cur is None:
                            save_all(model, rows, started)
                    elif now < cur["W"] + WINDOW and now >= cur.get("poll_at", 0):
                        poll_track(cur, now)
                elif now < end_at and last_sig != W and M * 60 + 3 <= ph < M * 60 + 45 and now >= sig_retry:
                    cur = make_signal(W, model)
                    if cur is None:
                        sig_retry = now + 6
                    else:
                        last_sig = W
                        LATEST = cur
                        write_live(cur, rows)
                        save_all(model, rows, started)   # publish the new call right away
                        push()
                        last_push = NOW()
                elif now >= next_rec and not (M * 60 - 15 < ph < M * 60 + 55):
                    next_rec = now + 30
                    reconcile(rows, by_w, next_try, now)
                    drain_training(model, by_w, now)
                errors = 0
            except Exception as e:
                errors += 1
                say("Problem (%d): %s" % (errors, e))
                if errors > 50:
                    raise
                sig_retry = NOW() + 6
                if cur is not None:
                    cur["next"] = NOW() + 8
            if NOW() - last_push >= PUSH_EVERY:
                save_all(model, rows, started)
                push()
                last_push = NOW()
            SLEEP(1)
    finally:
        try:
            save_all(model, rows, started)
        finally:
            push()
    say("Job time is up. Data saved; the next job continues from here.")


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        sys.exit(0)
