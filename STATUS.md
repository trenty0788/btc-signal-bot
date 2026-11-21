# BTC 5-minute signal bot

Last update: **Nov 20 9:57 PM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**▼ BET DOWN** for the window 9:55 PM to 10:00 PM

Bot leans DOWN 87%, DOWN costs 70¢, edge +15¢ after fees.

Called at 9:57 PM. The result is known at 10:00 PM. Reload this page for the next call.

## Summary

- Windows logged: **420**
- Result confirmed by Polymarket: **419** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **82%** of the last 100 windows
- Bot has learned from **2423** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (420)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 420 | 79% | -0.1¢ |
| +0¢ | 145 | 71% | +5.1¢ |
| +2¢ | 116 | 67% | +4.6¢ |
| +4¢ | 96 | 65% | +4.1¢ |
| +6¢ | 75 | 63% | +5.9¢ |
| +8¢ | 55 | 58% | +6.4¢ |

**Only windows whose result Polymarket confirmed (419)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 419 | 79% | +0.1¢ |
| +0¢ | 145 | 71% | +5.1¢ |
| +2¢ | 116 | 67% | +4.6¢ |
| +4¢ | 96 | 65% | +4.1¢ |
| +6¢ | 75 | 63% | +5.9¢ |
| +8¢ | 55 | 58% | +6.4¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **3**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 3 | 3 | 100% | 67% | -16.2¢ | -16.2¢ |
| Fair −2¢ | 3 | 3 | 100% | 67% | -14.2¢ | -14.2¢ |
| Fair −4¢ | 3 | 2 | 67% | 50% | -20.7¢ | -13.8¢ |
| Fair −6¢ | 3 | 2 | 67% | 50% | -18.7¢ | -12.5¢ |
| Fair −8¢ | 3 | 2 | 67% | 50% | -16.7¢ | -11.1¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2423 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 342 | 52% | 59% |
| 55-60% | 333 | 57% | 65% |
| 60-65% | 292 | 62% | 67% |
| 65-70% | 306 | 68% | 73% |
| 70-80% | 499 | 75% | 77% |
| 80-90% | 398 | 85% | 89% |
| 90%+ | 253 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 20 9:50 PM ET | DOWN 58% | 81¢ | skip | UP | Coinbase (close) |
| Nov 20 9:45 PM ET | UP 88% | 87¢ | skip | UP | Polymarket |
| Nov 20 9:40 PM ET | DOWN 97% | 94¢ | skip | DOWN | Polymarket |
| Nov 20 9:30 PM ET | DOWN 73% | 82¢ | skip | DOWN | Polymarket |
| Nov 20 9:25 PM ET | DOWN 69% | 75¢ | skip | DOWN | Polymarket |
| Nov 20 9:20 PM ET | DOWN 69% | 75¢ | skip | DOWN | Polymarket |
| Nov 20 9:15 PM ET | DOWN 77% | 85¢ | skip | DOWN | Polymarket |
| Nov 20 9:10 PM ET | UP 89% | 84¢ | UP | UP ✓ | Polymarket |
| Nov 20 9:05 PM ET | UP 86% | 92¢ | skip | DOWN | Polymarket |
| Nov 20 9:00 PM ET | UP 55% | 51¢ | UP | UP ✓ | Polymarket |
| Nov 20 8:55 PM ET | UP 81% | 63¢ | UP | UP ✓ | Polymarket |
| Nov 20 8:50 PM ET | UP 53% | 66¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
