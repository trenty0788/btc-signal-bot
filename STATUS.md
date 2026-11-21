# BTC 5-minute signal bot

Last update: **Nov 21 5:17 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 5:15 AM to 5:20 AM

Bot leans DOWN 62%, DOWN costs 68¢, edge -8¢ after fees.

Called at 5:17 AM. The result is known at 5:20 AM. Reload this page for the next call.

## Summary

- Windows logged: **488**
- Result confirmed by Polymarket: **487** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **71%** of the last 100 windows
- Bot has learned from **2491** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (488)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 488 | 78% | -0.5¢ |
| +0¢ | 173 | 68% | +2.3¢ |
| +2¢ | 139 | 64% | +2.1¢ |
| +4¢ | 115 | 63% | +2.6¢ |
| +6¢ | 91 | 60% | +4.0¢ |
| +8¢ | 70 | 57% | +4.6¢ |

**Only windows whose result Polymarket confirmed (487)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 487 | 78% | -0.4¢ |
| +0¢ | 173 | 68% | +2.3¢ |
| +2¢ | 139 | 64% | +2.1¢ |
| +4¢ | 115 | 63% | +2.6¢ |
| +6¢ | 91 | 60% | +4.0¢ |
| +8¢ | 70 | 57% | +4.6¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **48**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 48 | 26 | 54% | 69% | -10.8¢ | -5.9¢ |
| Fair −2¢ | 48 | 20 | 42% | 60% | -16.0¢ | -6.6¢ |
| Fair −4¢ | 48 | 16 | 33% | 50% | -21.9¢ | -7.3¢ |
| Fair −6¢ | 48 | 15 | 31% | 47% | -23.2¢ | -7.2¢ |
| Fair −8¢ | 48 | 14 | 29% | 43% | -23.5¢ | -6.8¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2491 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 350 | 52% | 58% |
| 55-60% | 337 | 57% | 65% |
| 60-65% | 302 | 62% | 67% |
| 65-70% | 312 | 68% | 73% |
| 70-80% | 515 | 75% | 77% |
| 80-90% | 410 | 85% | 89% |
| 90%+ | 265 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 5:10 AM ET | UP 57% | 77¢ | skip | DOWN | Coinbase |
| Nov 21 5:05 AM ET | UP 68% | 58¢ | UP | UP ✓ | Polymarket |
| Nov 21 5:00 AM ET | UP 60% | 52¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 4:55 AM ET | UP 67% | 77¢ | skip | UP | Polymarket |
| Nov 21 4:50 AM ET | DOWN 78% | 71¢ | DOWN | UP ✗ | Polymarket |
| Nov 21 4:45 AM ET | DOWN 67% | 56¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 21 4:40 AM ET | UP 77% | 71¢ | UP | UP ✓ | Polymarket |
| Nov 21 4:35 AM ET | DOWN 57% | 50¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 21 4:30 AM ET | DOWN 74% | 72¢ | skip | DOWN | Polymarket |
| Nov 21 4:25 AM ET | UP 63% | 67¢ | skip | UP | Polymarket |
| Nov 21 4:20 AM ET | UP 95% | 95¢ | skip | UP | Polymarket |
| Nov 21 4:15 AM ET | UP 78% | 73¢ | UP | DOWN ✗ | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
