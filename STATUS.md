# BTC 5-minute signal bot

Last update: **Nov 21 7:57 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 7:55 AM to 8:00 AM

Bot leans UP 60%, UP costs 72¢, edge -14¢ after fees.

Called at 7:57 AM. The result is known at 8:00 AM. Reload this page for the next call.

## Summary

- Windows logged: **519**
- Result confirmed by Polymarket: **518** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **74%** of the last 100 windows
- Bot has learned from **2522** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (519)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 519 | 78% | -0.5¢ |
| +0¢ | 178 | 67% | +2.0¢ |
| +2¢ | 142 | 64% | +2.0¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

**Only windows whose result Polymarket confirmed (518)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 518 | 78% | -0.5¢ |
| +0¢ | 178 | 67% | +2.0¢ |
| +2¢ | 142 | 64% | +2.0¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **76**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 76 | 44 | 58% | 70% | -6.8¢ | -3.9¢ |
| Fair −2¢ | 76 | 34 | 45% | 62% | -10.9¢ | -4.9¢ |
| Fair −4¢ | 76 | 29 | 38% | 55% | -13.4¢ | -5.1¢ |
| Fair −6¢ | 76 | 27 | 36% | 52% | -14.5¢ | -5.1¢ |
| Fair −8¢ | 76 | 26 | 34% | 50% | -13.4¢ | -4.6¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2522 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 353 | 52% | 58% |
| 55-60% | 341 | 57% | 64% |
| 60-65% | 308 | 62% | 67% |
| 65-70% | 314 | 68% | 74% |
| 70-80% | 520 | 75% | 77% |
| 80-90% | 416 | 85% | 89% |
| 90%+ | 270 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 7:50 AM ET | DOWN 60% | 77¢ | skip | DOWN | Coinbase (close) |
| Nov 21 7:45 AM ET | DOWN 61% | 70¢ | skip | DOWN | Polymarket |
| Nov 21 7:40 AM ET | DOWN 73% | 92¢ | skip | UP | Polymarket |
| Nov 21 7:35 AM ET | UP 98% | 99¢ | skip | UP | Polymarket |
| Nov 21 7:25 AM ET | UP 58% | 65¢ | skip | DOWN | Polymarket |
| Nov 21 7:20 AM ET | DOWN 88% | 86¢ | skip | DOWN | Polymarket |
| Nov 21 7:15 AM ET | UP 59% | 67¢ | skip | UP | Polymarket |
| Nov 21 7:10 AM ET | UP 86% | 87¢ | skip | UP | Polymarket |
| Nov 21 7:05 AM ET | UP 72% | 70¢ | skip | UP | Polymarket |
| Nov 21 7:00 AM ET | DOWN 67% | 77¢ | skip | DOWN | Polymarket |
| Nov 21 6:55 AM ET | UP 64% | 83¢ | skip | UP | Polymarket |
| Nov 21 6:50 AM ET | UP 61% | 58¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
