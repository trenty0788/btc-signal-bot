# BTC 5-minute signal bot

Last update: **Nov 20 10:32 PM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 10:30 PM to 10:35 PM

Bot leans DOWN 100%, DOWN costs 99¢, edge -1¢ after fees.

Called at 10:32 PM. The result is known at 10:35 PM. Reload this page for the next call.

## Summary

- Windows logged: **427**
- Result confirmed by Polymarket: **426** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **82%** of the last 100 windows
- Bot has learned from **2430** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (427)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 427 | 79% | +0.2¢ |
| +0¢ | 148 | 72% | +5.3¢ |
| +2¢ | 118 | 68% | +4.8¢ |
| +4¢ | 98 | 65% | +4.4¢ |
| +6¢ | 76 | 63% | +6.2¢ |
| +8¢ | 56 | 59% | +6.8¢ |

**Only windows whose result Polymarket confirmed (426)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 426 | 79% | +0.3¢ |
| +0¢ | 148 | 72% | +5.3¢ |
| +2¢ | 118 | 68% | +4.8¢ |
| +4¢ | 98 | 65% | +4.4¢ |
| +6¢ | 76 | 63% | +6.2¢ |
| +8¢ | 56 | 59% | +6.8¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **8**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 8 | 7 | 88% | 86% | +4.6¢ | +4.0¢ |
| Fair −2¢ | 8 | 6 | 75% | 83% | +6.8¢ | +5.1¢ |
| Fair −4¢ | 8 | 4 | 50% | 75% | +8.0¢ | +4.0¢ |
| Fair −6¢ | 8 | 4 | 50% | 75% | +10.0¢ | +5.0¢ |
| Fair −8¢ | 8 | 4 | 50% | 75% | +12.0¢ | +6.0¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2430 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 342 | 52% | 59% |
| 55-60% | 334 | 57% | 65% |
| 60-65% | 293 | 62% | 67% |
| 65-70% | 306 | 68% | 73% |
| 70-80% | 499 | 75% | 77% |
| 80-90% | 401 | 85% | 89% |
| 90%+ | 255 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 20 10:25 PM ET | UP 67% | 71¢ | skip | DOWN | Coinbase |
| Nov 20 10:20 PM ET | UP 63% | 73¢ | skip | UP | Polymarket |
| Nov 20 10:15 PM ET | DOWN 88% | 93¢ | skip | DOWN | Polymarket |
| Nov 20 10:10 PM ET | UP 95% | 95¢ | skip | UP | Polymarket |
| Nov 20 10:05 PM ET | DOWN 90% | 84¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 20 10:00 PM ET | DOWN 86% | 82¢ | skip | DOWN | Polymarket |
| Nov 20 9:55 PM ET | DOWN 87% | 70¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 20 9:50 PM ET | DOWN 58% | 81¢ | skip | DOWN | Polymarket |
| Nov 20 9:45 PM ET | UP 88% | 87¢ | skip | UP | Polymarket |
| Nov 20 9:40 PM ET | DOWN 97% | 94¢ | skip | DOWN | Polymarket |
| Nov 20 9:30 PM ET | DOWN 73% | 82¢ | skip | DOWN | Polymarket |
| Nov 20 9:25 PM ET | DOWN 69% | 75¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
