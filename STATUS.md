# BTC 5-minute signal bot

Last update: **Nov 21 4:32 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 4:30 AM to 4:35 AM

Bot leans DOWN 74%, DOWN costs 72¢, edge +0¢ after fees.

Called at 4:32 AM. The result is known at 4:35 AM. Reload this page for the next call.

## Summary

- Windows logged: **479**
- Result confirmed by Polymarket: **478** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **73%** of the last 100 windows
- Bot has learned from **2482** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (479)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 479 | 78% | -0.6¢ |
| +0¢ | 166 | 67% | +2.1¢ |
| +2¢ | 133 | 64% | +2.0¢ |
| +4¢ | 110 | 63% | +2.7¢ |
| +6¢ | 88 | 60% | +3.8¢ |
| +8¢ | 68 | 56% | +3.6¢ |

**Only windows whose result Polymarket confirmed (478)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 478 | 78% | -0.6¢ |
| +0¢ | 166 | 67% | +2.1¢ |
| +2¢ | 133 | 64% | +2.0¢ |
| +4¢ | 110 | 63% | +2.7¢ |
| +6¢ | 88 | 60% | +3.8¢ |
| +8¢ | 68 | 56% | +3.6¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **45**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 45 | 23 | 51% | 70% | -12.0¢ | -6.2¢ |
| Fair −2¢ | 45 | 18 | 40% | 61% | -16.0¢ | -6.4¢ |
| Fair −4¢ | 45 | 14 | 31% | 50% | -23.0¢ | -7.2¢ |
| Fair −6¢ | 45 | 14 | 31% | 50% | -21.0¢ | -6.5¢ |
| Fair −8¢ | 45 | 13 | 29% | 46% | -21.4¢ | -6.2¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2482 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 350 | 52% | 58% |
| 55-60% | 336 | 57% | 65% |
| 60-65% | 300 | 62% | 67% |
| 65-70% | 309 | 68% | 73% |
| 70-80% | 512 | 75% | 77% |
| 80-90% | 410 | 85% | 89% |
| 90%+ | 265 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 4:25 AM ET | UP 63% | 67¢ | skip | UP | Coinbase |
| Nov 21 4:20 AM ET | UP 95% | 95¢ | skip | UP | Polymarket |
| Nov 21 4:15 AM ET | UP 78% | 73¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 4:10 AM ET | UP 53% | 49¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 3:55 AM ET | DOWN 81% | 92¢ | skip | DOWN | Polymarket |
| Nov 21 3:50 AM ET | UP 78% | 85¢ | skip | DOWN | Polymarket |
| Nov 21 3:45 AM ET | UP 60% | 73¢ | skip | UP | Polymarket |
| Nov 21 3:30 AM ET | DOWN 78% | 81¢ | skip | DOWN | Polymarket |
| Nov 21 3:25 AM ET | UP 59% | 74¢ | skip | UP | Polymarket |
| Nov 21 3:20 AM ET | DOWN 95% | 94¢ | skip | DOWN | Polymarket |
| Nov 21 3:15 AM ET | UP 86% | 71¢ | UP | UP ✓ | Polymarket |
| Nov 21 1:50 AM ET | UP 86% | 88¢ | skip | UP | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
