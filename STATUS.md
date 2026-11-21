# BTC 5-minute signal bot

Last update: **Nov 21 8:37 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 8:35 AM to 8:40 AM

Bot leans UP 98%, UP costs 95¢, edge +1¢ after fees.

Called at 8:37 AM. The result is known at 8:40 AM. Reload this page for the next call.

## Summary

- Windows logged: **526**
- Result confirmed by Polymarket: **525** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **74%** of the last 100 windows
- Bot has learned from **2529** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (526)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 526 | 78% | -0.3¢ |
| +0¢ | 179 | 68% | +2.1¢ |
| +2¢ | 143 | 64% | +2.1¢ |
| +4¢ | 118 | 63% | +2.5¢ |
| +6¢ | 94 | 61% | +3.8¢ |
| +8¢ | 72 | 57% | +4.2¢ |

**Only windows whose result Polymarket confirmed (525)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 525 | 78% | -0.3¢ |
| +0¢ | 179 | 68% | +2.1¢ |
| +2¢ | 143 | 64% | +2.1¢ |
| +4¢ | 118 | 63% | +2.5¢ |
| +6¢ | 94 | 61% | +3.8¢ |
| +8¢ | 72 | 57% | +4.2¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **82**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 82 | 46 | 56% | 72% | -5.5¢ | -3.1¢ |
| Fair −2¢ | 82 | 35 | 43% | 63% | -9.5¢ | -4.1¢ |
| Fair −4¢ | 82 | 30 | 37% | 57% | -11.6¢ | -4.2¢ |
| Fair −6¢ | 82 | 28 | 34% | 54% | -12.5¢ | -4.3¢ |
| Fair −8¢ | 82 | 27 | 33% | 52% | -11.3¢ | -3.7¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2529 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 353 | 52% | 58% |
| 55-60% | 343 | 57% | 64% |
| 60-65% | 309 | 62% | 67% |
| 65-70% | 315 | 68% | 74% |
| 70-80% | 520 | 75% | 77% |
| 80-90% | 418 | 85% | 89% |
| 90%+ | 271 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 8:30 AM ET | UP 84% | 87¢ | skip | UP | Coinbase |
| Nov 21 8:20 AM ET | UP 86% | 85¢ | skip | UP | Polymarket |
| Nov 21 8:15 AM ET | DOWN 86% | 77¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 21 8:10 AM ET | UP 62% | 61¢ | skip | UP | Polymarket |
| Nov 21 8:05 AM ET | UP 92% | 96¢ | skip | UP | Polymarket |
| Nov 21 8:00 AM ET | UP 66% | 88¢ | skip | UP | Polymarket |
| Nov 21 7:55 AM ET | UP 60% | 72¢ | skip | UP | Polymarket |
| Nov 21 7:50 AM ET | DOWN 60% | 77¢ | skip | DOWN | Polymarket |
| Nov 21 7:45 AM ET | DOWN 61% | 70¢ | skip | DOWN | Polymarket |
| Nov 21 7:40 AM ET | DOWN 73% | 92¢ | skip | UP | Polymarket |
| Nov 21 7:35 AM ET | UP 98% | 99¢ | skip | UP | Polymarket |
| Nov 21 7:25 AM ET | UP 58% | 65¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
