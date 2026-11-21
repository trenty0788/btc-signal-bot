# BTC 5-minute signal bot

Last update: **Nov 21 5:42 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 5:40 AM to 5:45 AM

Bot leans DOWN 72%, DOWN costs 84¢, edge -14¢ after fees.

Called at 5:42 AM. The result is known at 5:45 AM. Reload this page for the next call.

## Summary

- Windows logged: **493**
- Result confirmed by Polymarket: **492** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **74%** of the last 100 windows
- Bot has learned from **2496** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (493)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 493 | 78% | -0.4¢ |
| +0¢ | 175 | 68% | +2.5¢ |
| +2¢ | 141 | 65% | +2.3¢ |
| +4¢ | 116 | 63% | +2.7¢ |
| +6¢ | 92 | 61% | +4.1¢ |
| +8¢ | 71 | 58% | +4.8¢ |

**Only windows whose result Polymarket confirmed (492)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 492 | 78% | -0.4¢ |
| +0¢ | 175 | 68% | +2.5¢ |
| +2¢ | 141 | 65% | +2.3¢ |
| +4¢ | 116 | 63% | +2.7¢ |
| +6¢ | 92 | 61% | +4.1¢ |
| +8¢ | 71 | 58% | +4.8¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **51**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 51 | 28 | 55% | 71% | -8.3¢ | -4.5¢ |
| Fair −2¢ | 51 | 22 | 43% | 64% | -12.0¢ | -5.2¢ |
| Fair −4¢ | 51 | 18 | 35% | 56% | -16.2¢ | -5.7¢ |
| Fair −6¢ | 51 | 17 | 33% | 53% | -16.8¢ | -5.6¢ |
| Fair −8¢ | 51 | 16 | 31% | 50% | -16.4¢ | -5.1¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2496 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 350 | 52% | 58% |
| 55-60% | 338 | 57% | 64% |
| 60-65% | 303 | 62% | 67% |
| 65-70% | 312 | 68% | 73% |
| 70-80% | 515 | 75% | 77% |
| 80-90% | 411 | 85% | 89% |
| 90%+ | 267 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 5:35 AM ET | DOWN 84% | 91¢ | skip | DOWN | Coinbase (close) |
| Nov 21 5:30 AM ET | DOWN 96% | 98¢ | skip | DOWN | Polymarket |
| Nov 21 5:25 AM ET | UP 93% | 80¢ | UP | UP ✓ | Polymarket |
| Nov 21 5:20 AM ET | UP 85% | 80¢ | UP | UP ✓ | Polymarket |
| Nov 21 5:15 AM ET | DOWN 62% | 68¢ | skip | DOWN | Polymarket |
| Nov 21 5:10 AM ET | UP 57% | 77¢ | skip | DOWN | Polymarket |
| Nov 21 5:05 AM ET | UP 68% | 58¢ | UP | UP ✓ | Polymarket |
| Nov 21 5:00 AM ET | UP 60% | 52¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 4:55 AM ET | UP 67% | 77¢ | skip | UP | Polymarket |
| Nov 21 4:50 AM ET | DOWN 78% | 71¢ | DOWN | UP ✗ | Polymarket |
| Nov 21 4:45 AM ET | DOWN 67% | 56¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 21 4:40 AM ET | UP 77% | 71¢ | UP | UP ✓ | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
