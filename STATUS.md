# BTC 5-minute signal bot

Last update: **Nov 20 10:52 PM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 10:50 PM to 10:55 PM

Bot leans DOWN 82%, DOWN costs 87¢, edge -7¢ after fees.

Called at 10:52 PM. The result is known at 10:55 PM. Reload this page for the next call.

## Summary

- Windows logged: **431**
- Result confirmed by Polymarket: **430** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **82%** of the last 100 windows
- Bot has learned from **2434** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (431)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 431 | 79% | +0.0¢ |
| +0¢ | 148 | 72% | +5.3¢ |
| +2¢ | 118 | 68% | +4.8¢ |
| +4¢ | 98 | 65% | +4.4¢ |
| +6¢ | 76 | 63% | +6.2¢ |
| +8¢ | 56 | 59% | +6.8¢ |

**Only windows whose result Polymarket confirmed (430)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 430 | 79% | -0.0¢ |
| +0¢ | 148 | 72% | +5.3¢ |
| +2¢ | 118 | 68% | +4.8¢ |
| +4¢ | 98 | 65% | +4.4¢ |
| +6¢ | 76 | 63% | +6.2¢ |
| +8¢ | 56 | 59% | +6.8¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **12**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 12 | 10 | 83% | 80% | -2.8¢ | -2.3¢ |
| Fair −2¢ | 12 | 8 | 67% | 75% | -1.6¢ | -1.0¢ |
| Fair −4¢ | 12 | 6 | 50% | 67% | -2.9¢ | -1.5¢ |
| Fair −6¢ | 12 | 6 | 50% | 67% | -0.9¢ | -0.5¢ |
| Fair −8¢ | 12 | 6 | 50% | 67% | +1.1¢ | +0.5¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2434 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 342 | 52% | 59% |
| 55-60% | 334 | 57% | 65% |
| 60-65% | 293 | 62% | 67% |
| 65-70% | 307 | 68% | 73% |
| 70-80% | 501 | 75% | 77% |
| 80-90% | 401 | 85% | 89% |
| 90%+ | 256 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 20 10:45 PM ET | UP 73% | 80¢ | skip | UP | Coinbase |
| Nov 20 10:40 PM ET | UP 77% | 89¢ | skip | DOWN | Polymarket |
| Nov 20 10:35 PM ET | UP 76% | 89¢ | skip | UP | Polymarket |
| Nov 20 10:30 PM ET | DOWN 100% | 99¢ | skip | DOWN | Polymarket |
| Nov 20 10:25 PM ET | UP 67% | 71¢ | skip | DOWN | Polymarket |
| Nov 20 10:20 PM ET | UP 63% | 73¢ | skip | UP | Polymarket |
| Nov 20 10:15 PM ET | DOWN 88% | 93¢ | skip | DOWN | Polymarket |
| Nov 20 10:10 PM ET | UP 95% | 95¢ | skip | UP | Polymarket |
| Nov 20 10:05 PM ET | DOWN 90% | 84¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 20 10:00 PM ET | DOWN 86% | 82¢ | skip | DOWN | Polymarket |
| Nov 20 9:55 PM ET | DOWN 87% | 70¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 20 9:50 PM ET | DOWN 58% | 81¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
