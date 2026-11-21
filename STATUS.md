# BTC 5-minute signal bot

Last update: **Nov 21 1:07 AM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**▲ BET UP** for the window 1:05 AM to 1:10 AM

Bot leans UP 63%, UP costs 51¢, edge +10¢ after fees.

Called at 1:07 AM. The result is known at 1:10 AM. Reload this page for the next call.

## Summary

- Windows logged: **458**
- Result confirmed by Polymarket: **457** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **77%** of the last 100 windows
- Bot has learned from **2461** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (458)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 458 | 78% | -0.6¢ |
| +0¢ | 157 | 68% | +2.8¢ |
| +2¢ | 125 | 65% | +2.9¢ |
| +4¢ | 104 | 62% | +2.7¢ |
| +6¢ | 82 | 60% | +3.9¢ |
| +8¢ | 62 | 55% | +3.6¢ |

**Only windows whose result Polymarket confirmed (457)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 457 | 78% | -0.5¢ |
| +0¢ | 156 | 69% | +3.2¢ |
| +2¢ | 125 | 65% | +2.9¢ |
| +4¢ | 104 | 62% | +2.7¢ |
| +6¢ | 82 | 60% | +3.9¢ |
| +8¢ | 62 | 55% | +3.6¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **32**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 32 | 15 | 47% | 60% | -19.9¢ | -9.4¢ |
| Fair −2¢ | 32 | 13 | 41% | 54% | -21.1¢ | -8.6¢ |
| Fair −4¢ | 32 | 11 | 34% | 45% | -24.5¢ | -8.4¢ |
| Fair −6¢ | 32 | 11 | 34% | 45% | -22.5¢ | -7.7¢ |
| Fair −8¢ | 32 | 11 | 34% | 45% | -20.5¢ | -7.0¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2461 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 347 | 52% | 58% |
| 55-60% | 335 | 57% | 64% |
| 60-65% | 297 | 62% | 67% |
| 65-70% | 309 | 68% | 73% |
| 70-80% | 508 | 75% | 77% |
| 80-90% | 405 | 85% | 89% |
| 90%+ | 260 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 1:00 AM ET | UP 52% | 49¢ | skip | DOWN | Coinbase (close) |
| Nov 21 12:55 AM ET | UP 54% | 48¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 12:50 AM ET | DOWN 69% | 79¢ | skip | DOWN | Polymarket |
| Nov 21 12:45 AM ET | UP 61% | 64¢ | skip | UP | Polymarket |
| Nov 21 12:40 AM ET | DOWN 94% | 95¢ | skip | DOWN | Polymarket |
| Nov 21 12:35 AM ET | DOWN 92% | 88¢ | skip | UP | Polymarket |
| Nov 21 12:30 AM ET | DOWN 94% | 95¢ | skip | DOWN | Polymarket |
| Nov 21 12:25 AM ET | UP 53% | 67¢ | skip | UP | Polymarket |
| Nov 21 12:20 AM ET | UP 65% | 22¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 12:15 AM ET | UP 77% | 80¢ | skip | UP | Polymarket |
| Nov 21 12:10 AM ET | UP 75% | 78¢ | skip | DOWN | Polymarket |
| Nov 21 12:05 AM ET | DOWN 78% | 85¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
