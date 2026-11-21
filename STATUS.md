# BTC 5-minute signal bot

Last update: **Nov 21 2:47 AM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 2:45 AM to 2:50 AM

Bot leans DOWN 75%, DOWN costs 81¢, edge -8¢ after fees.

Called at 2:47 AM. The result is known at 2:50 AM. Reload this page for the next call.

## Summary

- Windows logged: **478**
- Result confirmed by Polymarket: **477** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **74%** of the last 100 windows
- Bot has learned from **2481** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (478)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 478 | 78% | -0.2¢ |
| +0¢ | 168 | 69% | +3.7¢ |
| +2¢ | 134 | 66% | +3.9¢ |
| +4¢ | 112 | 63% | +3.5¢ |
| +6¢ | 89 | 61% | +4.4¢ |
| +8¢ | 69 | 57% | +4.4¢ |

**Only windows whose result Polymarket confirmed (477)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 477 | 78% | -0.1¢ |
| +0¢ | 168 | 69% | +3.7¢ |
| +2¢ | 134 | 66% | +3.9¢ |
| +4¢ | 112 | 63% | +3.5¢ |
| +6¢ | 89 | 61% | +4.4¢ |
| +8¢ | 69 | 57% | +4.4¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **43**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 43 | 23 | 53% | 65% | -13.8¢ | -7.4¢ |
| Fair −2¢ | 43 | 20 | 47% | 60% | -14.3¢ | -6.7¢ |
| Fair −4¢ | 43 | 15 | 35% | 47% | -21.8¢ | -7.6¢ |
| Fair −6¢ | 43 | 15 | 35% | 47% | -19.8¢ | -6.9¢ |
| Fair −8¢ | 43 | 15 | 35% | 47% | -17.8¢ | -6.2¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2481 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 349 | 52% | 58% |
| 55-60% | 338 | 57% | 64% |
| 60-65% | 299 | 62% | 67% |
| 65-70% | 309 | 68% | 73% |
| 70-80% | 512 | 75% | 77% |
| 80-90% | 409 | 85% | 89% |
| 90%+ | 265 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 2:40 AM ET | UP 50% | 50¢ | skip | DOWN | Coinbase |
| Nov 21 2:35 AM ET | UP 74% | 72¢ | skip | UP | Polymarket |
| Nov 21 2:30 AM ET | UP 70% | 64¢ | UP | UP ✓ | Polymarket |
| Nov 21 2:25 AM ET | DOWN 75% | 86¢ | skip | DOWN | Polymarket |
| Nov 21 2:20 AM ET | DOWN 56% | 59¢ | skip | UP | Polymarket |
| Nov 21 2:15 AM ET | UP 81% | 70¢ | UP | UP ✓ | Polymarket |
| Nov 21 2:10 AM ET | DOWN 55% | 51¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 21 2:05 AM ET | UP 92% | 90¢ | skip | UP | Polymarket |
| Nov 21 2:00 AM ET | DOWN 92% | 94¢ | skip | DOWN | Polymarket |
| Nov 21 1:55 AM ET | UP 59% | 39¢ | UP | UP ✓ | Polymarket |
| Nov 21 1:50 AM ET | UP 86% | 88¢ | skip | UP | Polymarket |
| Nov 21 1:45 AM ET | UP 90% | 89¢ | skip | UP | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
