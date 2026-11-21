# BTC 5-minute signal bot

Last update: **Nov 21 6:12 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 6:10 AM to 6:15 AM

Bot leans UP 62%, UP costs 80¢, edge -20¢ after fees.

Called at 6:12 AM. The result is known at 6:15 AM. Reload this page for the next call.

## Summary

- Windows logged: **499**
- Result confirmed by Polymarket: **498** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **74%** of the last 100 windows
- Bot has learned from **2502** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (499)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 499 | 78% | -0.3¢ |
| +0¢ | 177 | 68% | +2.4¢ |
| +2¢ | 142 | 64% | +2.0¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

**Only windows whose result Polymarket confirmed (498)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 498 | 78% | -0.2¢ |
| +0¢ | 176 | 68% | +2.6¢ |
| +2¢ | 141 | 65% | +2.3¢ |
| +4¢ | 116 | 63% | +2.7¢ |
| +6¢ | 92 | 61% | +4.1¢ |
| +8¢ | 71 | 58% | +4.8¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **56**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 56 | 30 | 54% | 73% | -6.5¢ | -3.5¢ |
| Fair −2¢ | 56 | 24 | 43% | 67% | -9.4¢ | -4.0¢ |
| Fair −4¢ | 56 | 20 | 36% | 60% | -12.4¢ | -4.4¢ |
| Fair −6¢ | 56 | 19 | 34% | 58% | -12.5¢ | -4.2¢ |
| Fair −8¢ | 56 | 18 | 32% | 56% | -11.7¢ | -3.8¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2502 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 350 | 52% | 58% |
| 55-60% | 338 | 57% | 64% |
| 60-65% | 304 | 62% | 67% |
| 65-70% | 312 | 68% | 73% |
| 70-80% | 518 | 75% | 77% |
| 80-90% | 413 | 85% | 89% |
| 90%+ | 267 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 6:05 AM ET | DOWN 58% | 42¢ | DOWN | UP ✗ | Coinbase |
| Nov 21 6:00 AM ET | DOWN 82% | 84¢ | skip | DOWN | Polymarket |
| Nov 21 5:55 AM ET | DOWN 75% | 83¢ | skip | DOWN | Polymarket |
| Nov 21 5:50 AM ET | UP 64% | 76¢ | skip | UP | Polymarket |
| Nov 21 5:45 AM ET | UP 78% | 75¢ | skip | UP | Polymarket |
| Nov 21 5:40 AM ET | DOWN 72% | 84¢ | skip | DOWN | Polymarket |
| Nov 21 5:35 AM ET | DOWN 84% | 91¢ | skip | DOWN | Polymarket |
| Nov 21 5:30 AM ET | DOWN 96% | 98¢ | skip | DOWN | Polymarket |
| Nov 21 5:25 AM ET | UP 93% | 80¢ | UP | UP ✓ | Polymarket |
| Nov 21 5:20 AM ET | UP 85% | 80¢ | UP | UP ✓ | Polymarket |
| Nov 21 5:15 AM ET | DOWN 62% | 68¢ | skip | DOWN | Polymarket |
| Nov 21 5:10 AM ET | UP 57% | 77¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
