# BTC 5-minute signal bot

Last update: **Nov 21 5:37 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 5:35 AM to 5:40 AM

Bot leans DOWN 84%, DOWN costs 91¢, edge -9¢ after fees.

Called at 5:37 AM. The result is known at 5:40 AM. Reload this page for the next call.

## Summary

- Windows logged: **492**
- Result confirmed by Polymarket: **491** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **74%** of the last 100 windows
- Bot has learned from **2495** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (492)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 492 | 78% | -0.4¢ |
| +0¢ | 175 | 68% | +2.5¢ |
| +2¢ | 141 | 65% | +2.3¢ |
| +4¢ | 116 | 63% | +2.7¢ |
| +6¢ | 92 | 61% | +4.1¢ |
| +8¢ | 71 | 58% | +4.8¢ |

**Only windows whose result Polymarket confirmed (491)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 491 | 78% | -0.4¢ |
| +0¢ | 175 | 68% | +2.5¢ |
| +2¢ | 141 | 65% | +2.3¢ |
| +4¢ | 116 | 63% | +2.7¢ |
| +6¢ | 92 | 61% | +4.1¢ |
| +8¢ | 71 | 58% | +4.8¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **50**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 50 | 27 | 54% | 70% | -9.1¢ | -4.9¢ |
| Fair −2¢ | 50 | 21 | 42% | 62% | -13.4¢ | -5.6¢ |
| Fair −4¢ | 50 | 17 | 34% | 53% | -18.2¢ | -6.2¢ |
| Fair −6¢ | 50 | 16 | 32% | 50% | -19.1¢ | -6.1¢ |
| Fair −8¢ | 50 | 15 | 30% | 47% | -18.9¢ | -5.7¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2495 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 350 | 52% | 58% |
| 55-60% | 338 | 57% | 64% |
| 60-65% | 303 | 62% | 67% |
| 65-70% | 312 | 68% | 73% |
| 70-80% | 515 | 75% | 77% |
| 80-90% | 411 | 85% | 89% |
| 90%+ | 266 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 5:30 AM ET | DOWN 96% | 98¢ | skip | DOWN | Coinbase |
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
| Nov 21 4:35 AM ET | DOWN 57% | 50¢ | DOWN | DOWN ✓ | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
