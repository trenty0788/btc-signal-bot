# BTC 5-minute signal bot

Last update: **Nov 21 1:32 AM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 1:30 AM to 1:35 AM

Bot leans UP 61%, UP costs 61¢, edge -2¢ after fees.

Called at 1:32 AM. The result is known at 1:35 AM. Reload this page for the next call.

## Summary

- Windows logged: **463**
- Result confirmed by Polymarket: **462** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **75%** of the last 100 windows
- Bot has learned from **2466** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (463)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 463 | 78% | -0.7¢ |
| +0¢ | 161 | 68% | +2.4¢ |
| +2¢ | 129 | 64% | +2.3¢ |
| +4¢ | 108 | 62% | +2.0¢ |
| +6¢ | 86 | 59% | +2.9¢ |
| +8¢ | 66 | 55% | +2.4¢ |

**Only windows whose result Polymarket confirmed (462)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 462 | 78% | -0.7¢ |
| +0¢ | 161 | 68% | +2.4¢ |
| +2¢ | 129 | 64% | +2.3¢ |
| +4¢ | 108 | 62% | +2.0¢ |
| +6¢ | 86 | 59% | +2.9¢ |
| +8¢ | 66 | 55% | +2.4¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **33**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 33 | 15 | 45% | 60% | -19.9¢ | -9.1¢ |
| Fair −2¢ | 33 | 13 | 39% | 54% | -21.1¢ | -8.3¢ |
| Fair −4¢ | 33 | 11 | 33% | 45% | -24.5¢ | -8.2¢ |
| Fair −6¢ | 33 | 11 | 33% | 45% | -22.5¢ | -7.5¢ |
| Fair −8¢ | 33 | 11 | 33% | 45% | -20.5¢ | -6.8¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2466 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 348 | 52% | 58% |
| 55-60% | 335 | 57% | 64% |
| 60-65% | 298 | 62% | 67% |
| 65-70% | 309 | 68% | 73% |
| 70-80% | 508 | 75% | 77% |
| 80-90% | 407 | 85% | 89% |
| 90%+ | 261 | 94% | 93% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 1:25 AM ET | UP 72% | 80¢ | skip | UP | Coinbase |
| Nov 21 1:20 AM ET | DOWN 80% | 58¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 21 1:15 AM ET | DOWN 100% | 89¢ | DOWN | UP ✗ | Polymarket |
| Nov 21 1:10 AM ET | UP 90% | 61¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 1:05 AM ET | UP 63% | 51¢ | UP | UP ✓ | Polymarket |
| Nov 21 1:00 AM ET | UP 52% | 49¢ | skip | DOWN | Polymarket |
| Nov 21 12:55 AM ET | UP 54% | 48¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 12:50 AM ET | DOWN 69% | 79¢ | skip | DOWN | Polymarket |
| Nov 21 12:45 AM ET | UP 61% | 64¢ | skip | UP | Polymarket |
| Nov 21 12:40 AM ET | DOWN 94% | 95¢ | skip | DOWN | Polymarket |
| Nov 21 12:35 AM ET | DOWN 92% | 88¢ | skip | UP | Polymarket |
| Nov 21 12:30 AM ET | DOWN 94% | 95¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
