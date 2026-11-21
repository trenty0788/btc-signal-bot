# BTC 5-minute signal bot

Last update: **Nov 21 3:12 AM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 3:10 AM to 3:15 AM

Bot leans UP 87%, UP costs 84¢, edge +1¢ after fees.

Called at 3:12 AM. The result is known at 3:15 AM. Reload this page for the next call.

## Summary

- Windows logged: **483**
- Result confirmed by Polymarket: **482** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **73%** of the last 100 windows
- Bot has learned from **2486** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (483)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 483 | 78% | -0.2¢ |
| +0¢ | 171 | 69% | +3.2¢ |
| +2¢ | 135 | 65% | +3.3¢ |
| +4¢ | 113 | 63% | +2.8¢ |
| +6¢ | 90 | 60% | +3.5¢ |
| +8¢ | 70 | 56% | +3.2¢ |

**Only windows whose result Polymarket confirmed (482)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 482 | 78% | -0.1¢ |
| +0¢ | 170 | 69% | +3.7¢ |
| +2¢ | 134 | 66% | +3.9¢ |
| +4¢ | 112 | 63% | +3.5¢ |
| +6¢ | 89 | 61% | +4.4¢ |
| +8¢ | 69 | 57% | +4.4¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **1**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **47**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 47 | 26 | 55% | 69% | -10.8¢ | -6.0¢ |
| Fair −2¢ | 47 | 23 | 49% | 65% | -10.6¢ | -5.2¢ |
| Fair −4¢ | 47 | 16 | 34% | 50% | -18.1¢ | -6.2¢ |
| Fair −6¢ | 47 | 16 | 34% | 50% | -16.1¢ | -5.5¢ |
| Fair −8¢ | 47 | 16 | 34% | 50% | -14.1¢ | -4.8¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2486 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 350 | 52% | 58% |
| 55-60% | 338 | 57% | 64% |
| 60-65% | 300 | 62% | 67% |
| 65-70% | 309 | 68% | 73% |
| 70-80% | 513 | 75% | 77% |
| 80-90% | 409 | 85% | 89% |
| 90%+ | 267 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 3:05 AM ET | UP 87% | 76¢ | UP | DOWN ✗ | Coinbase (close) |
| Nov 21 3:00 AM ET | DOWN 98% | 96¢ | skip | DOWN | Polymarket |
| Nov 21 2:55 AM ET | UP 64% | 64¢ | skip | UP | Polymarket |
| Nov 21 2:50 AM ET | UP 95% | 92¢ | skip | UP | Polymarket |
| Nov 21 2:45 AM ET | DOWN 75% | 81¢ | skip | DOWN | Polymarket |
| Nov 21 2:40 AM ET | UP 50% | 50¢ | skip | DOWN | Polymarket |
| Nov 21 2:35 AM ET | UP 74% | 72¢ | skip | UP | Polymarket |
| Nov 21 2:30 AM ET | UP 70% | 64¢ | UP | UP ✓ | Polymarket |
| Nov 21 2:25 AM ET | DOWN 75% | 86¢ | skip | DOWN | Polymarket |
| Nov 21 2:20 AM ET | DOWN 56% | 59¢ | skip | UP | Polymarket |
| Nov 21 2:15 AM ET | UP 81% | 70¢ | UP | UP ✓ | Polymarket |
| Nov 21 2:10 AM ET | DOWN 55% | 51¢ | DOWN | DOWN ✓ | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
