# BTC 5-minute signal bot

Last update: **Nov 21 6:02 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 6:00 AM to 6:05 AM

Bot leans DOWN 82%, DOWN costs 84¢, edge -4¢ after fees.

Called at 6:02 AM. The result is known at 6:05 AM. Reload this page for the next call.

## Summary

- Windows logged: **497**
- Result confirmed by Polymarket: **496** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **75%** of the last 100 windows
- Bot has learned from **2500** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (497)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 497 | 78% | -0.2¢ |
| +0¢ | 176 | 68% | +2.6¢ |
| +2¢ | 141 | 65% | +2.3¢ |
| +4¢ | 116 | 63% | +2.7¢ |
| +6¢ | 92 | 61% | +4.1¢ |
| +8¢ | 71 | 58% | +4.8¢ |

**Only windows whose result Polymarket confirmed (496)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 496 | 78% | -0.3¢ |
| +0¢ | 176 | 68% | +2.6¢ |
| +2¢ | 141 | 65% | +2.3¢ |
| +4¢ | 116 | 63% | +2.7¢ |
| +6¢ | 92 | 61% | +4.1¢ |
| +8¢ | 71 | 58% | +4.8¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **55**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 55 | 29 | 53% | 72% | -7.3¢ | -3.8¢ |
| Fair −2¢ | 55 | 23 | 42% | 65% | -10.6¢ | -4.4¢ |
| Fair −4¢ | 55 | 19 | 35% | 58% | -14.1¢ | -4.9¢ |
| Fair −6¢ | 55 | 18 | 33% | 56% | -14.4¢ | -4.7¢ |
| Fair −8¢ | 55 | 17 | 31% | 53% | -13.8¢ | -4.3¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2500 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 350 | 52% | 58% |
| 55-60% | 338 | 57% | 64% |
| 60-65% | 304 | 62% | 67% |
| 65-70% | 312 | 68% | 73% |
| 70-80% | 517 | 75% | 77% |
| 80-90% | 412 | 85% | 89% |
| 90%+ | 267 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 5:55 AM ET | DOWN 75% | 83¢ | skip | DOWN | Coinbase |
| Nov 21 5:50 AM ET | UP 64% | 76¢ | skip | UP | Polymarket |
| Nov 21 5:45 AM ET | UP 78% | 75¢ | skip | UP | Polymarket |
| Nov 21 5:40 AM ET | DOWN 72% | 84¢ | skip | DOWN | Polymarket |
| Nov 21 5:35 AM ET | DOWN 84% | 91¢ | skip | DOWN | Polymarket |
| Nov 21 5:30 AM ET | DOWN 96% | 98¢ | skip | DOWN | Polymarket |
| Nov 21 5:25 AM ET | UP 93% | 80¢ | UP | UP ✓ | Polymarket |
| Nov 21 5:20 AM ET | UP 85% | 80¢ | UP | UP ✓ | Polymarket |
| Nov 21 5:15 AM ET | DOWN 62% | 68¢ | skip | DOWN | Polymarket |
| Nov 21 5:10 AM ET | UP 57% | 77¢ | skip | DOWN | Polymarket |
| Nov 21 5:05 AM ET | UP 68% | 58¢ | UP | UP ✓ | Polymarket |
| Nov 21 5:00 AM ET | UP 60% | 52¢ | UP | DOWN ✗ | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
