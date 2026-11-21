# BTC 5-minute signal bot

Last update: **Nov 21 2:22 AM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 2:20 AM to 2:25 AM

Bot leans DOWN 56%, DOWN costs 59¢, edge -5¢ after fees.

Called at 2:22 AM. The result is known at 2:25 AM. Reload this page for the next call.

## Summary

- Windows logged: **473**
- Result confirmed by Polymarket: **472** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **76%** of the last 100 windows
- Bot has learned from **2476** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (473)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 473 | 78% | -0.1¢ |
| +0¢ | 167 | 69% | +3.5¢ |
| +2¢ | 133 | 65% | +3.7¢ |
| +4¢ | 111 | 63% | +3.2¢ |
| +6¢ | 89 | 61% | +4.4¢ |
| +8¢ | 69 | 57% | +4.4¢ |

**Only windows whose result Polymarket confirmed (472)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 472 | 78% | -0.2¢ |
| +0¢ | 166 | 69% | +3.4¢ |
| +2¢ | 132 | 65% | +3.5¢ |
| +4¢ | 110 | 63% | +3.0¢ |
| +6¢ | 88 | 60% | +4.2¢ |
| +8¢ | 68 | 56% | +4.0¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **39**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 39 | 20 | 51% | 70% | -11.6¢ | -5.9¢ |
| Fair −2¢ | 39 | 17 | 44% | 65% | -12.2¢ | -5.3¢ |
| Fair −4¢ | 39 | 12 | 31% | 50% | -21.1¢ | -6.5¢ |
| Fair −6¢ | 39 | 12 | 31% | 50% | -19.1¢ | -5.9¢ |
| Fair −8¢ | 39 | 12 | 31% | 50% | -17.1¢ | -5.3¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2476 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 349 | 52% | 58% |
| 55-60% | 337 | 57% | 65% |
| 60-65% | 299 | 62% | 67% |
| 65-70% | 309 | 68% | 73% |
| 70-80% | 509 | 75% | 77% |
| 80-90% | 408 | 85% | 89% |
| 90%+ | 265 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 2:15 AM ET | UP 81% | 70¢ | UP | UP ✓ | Coinbase |
| Nov 21 2:10 AM ET | DOWN 55% | 51¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 21 2:05 AM ET | UP 92% | 90¢ | skip | UP | Polymarket |
| Nov 21 2:00 AM ET | DOWN 92% | 94¢ | skip | DOWN | Polymarket |
| Nov 21 1:55 AM ET | UP 59% | 39¢ | UP | UP ✓ | Polymarket |
| Nov 21 1:50 AM ET | UP 86% | 88¢ | skip | UP | Polymarket |
| Nov 21 1:45 AM ET | UP 90% | 89¢ | skip | UP | Polymarket |
| Nov 21 1:40 AM ET | UP 93% | 90¢ | skip | UP | Polymarket |
| Nov 21 1:35 AM ET | UP 51% | 40¢ | UP | UP ✓ | Polymarket |
| Nov 21 1:30 AM ET | UP 61% | 61¢ | skip | UP | Polymarket |
| Nov 21 1:25 AM ET | UP 72% | 80¢ | skip | UP | Polymarket |
| Nov 21 1:20 AM ET | DOWN 80% | 58¢ | DOWN | DOWN ✓ | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
