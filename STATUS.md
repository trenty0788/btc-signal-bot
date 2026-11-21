# BTC 5-minute signal bot

Last update: **Nov 21 3:42 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 3:40 AM to 3:45 AM

Bot leans UP 97%, UP costs 99¢, edge -4¢ after fees.

Called at 3:42 AM. The result is known at 3:45 AM. Reload this page for the next call.

## Summary

- Windows logged: **472**
- Result confirmed by Polymarket: **472** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **76%** of the last 100 windows
- Bot has learned from **2476** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (472)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 472 | 78% | -0.2¢ |
| +0¢ | 164 | 68% | +2.9¢ |
| +2¢ | 131 | 65% | +2.9¢ |
| +4¢ | 110 | 63% | +2.7¢ |
| +6¢ | 88 | 60% | +3.8¢ |
| +8¢ | 68 | 56% | +3.6¢ |

**Only windows whose result Polymarket confirmed (472)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 472 | 78% | -0.2¢ |
| +0¢ | 164 | 68% | +2.9¢ |
| +2¢ | 131 | 65% | +2.9¢ |
| +4¢ | 110 | 63% | +2.7¢ |
| +6¢ | 88 | 60% | +3.8¢ |
| +8¢ | 68 | 56% | +3.6¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **40**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 40 | 20 | 50% | 70% | -11.7¢ | -5.9¢ |
| Fair −2¢ | 40 | 16 | 40% | 62% | -13.4¢ | -5.4¢ |
| Fair −4¢ | 40 | 12 | 30% | 50% | -21.1¢ | -6.3¢ |
| Fair −6¢ | 40 | 12 | 30% | 50% | -19.1¢ | -5.7¢ |
| Fair −8¢ | 40 | 12 | 30% | 50% | -17.1¢ | -5.1¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2476 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 349 | 52% | 58% |
| 55-60% | 336 | 57% | 65% |
| 60-65% | 299 | 62% | 67% |
| 65-70% | 309 | 68% | 73% |
| 70-80% | 510 | 75% | 77% |
| 80-90% | 409 | 85% | 89% |
| 90%+ | 264 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 3:30 AM ET | DOWN 78% | 81¢ | skip | DOWN | Polymarket |
| Nov 21 3:25 AM ET | UP 59% | 74¢ | skip | UP | Polymarket |
| Nov 21 3:20 AM ET | DOWN 95% | 94¢ | skip | DOWN | Polymarket |
| Nov 21 3:15 AM ET | UP 86% | 71¢ | UP | UP ✓ | Polymarket |
| Nov 21 1:50 AM ET | UP 86% | 88¢ | skip | UP | Polymarket |
| Nov 21 1:45 AM ET | UP 90% | 89¢ | skip | UP | Polymarket |
| Nov 21 1:40 AM ET | UP 93% | 90¢ | skip | UP | Polymarket |
| Nov 21 1:35 AM ET | UP 51% | 40¢ | UP | UP ✓ | Polymarket |
| Nov 21 1:30 AM ET | UP 61% | 61¢ | skip | UP | Polymarket |
| Nov 21 1:25 AM ET | UP 72% | 80¢ | skip | UP | Polymarket |
| Nov 21 1:20 AM ET | DOWN 80% | 58¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 21 1:15 AM ET | DOWN 100% | 89¢ | DOWN | UP ✗ | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
