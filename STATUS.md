# BTC 5-minute signal bot

Last update: **Nov 21 9:37 AM ET** (this job started Nov 21 8:50 AM ET)

## Latest call

**▼ BET DOWN** for the window 9:35 AM to 9:40 AM

Bot leans DOWN 88%, DOWN costs 74¢, edge +12¢ after fees.

Called at 9:37 AM. The result is known at 9:40 AM. Reload this page for the next call.

## Summary

- Windows logged: **526**
- Result confirmed by Polymarket: **525** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **69%** of the last 100 windows
- Bot has learned from **2529** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (526)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 526 | 77% | -1.0¢ |
| +0¢ | 183 | 67% | +1.3¢ |
| +2¢ | 145 | 63% | +1.3¢ |
| +4¢ | 118 | 62% | +1.7¢ |
| +6¢ | 94 | 60% | +2.8¢ |
| +8¢ | 73 | 56% | +3.1¢ |

**Only windows whose result Polymarket confirmed (525)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 525 | 77% | -1.1¢ |
| +0¢ | 182 | 66% | +1.1¢ |
| +2¢ | 145 | 63% | +1.3¢ |
| +4¢ | 118 | 62% | +1.7¢ |
| +6¢ | 94 | 60% | +2.8¢ |
| +8¢ | 73 | 56% | +3.1¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **80**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 80 | 48 | 60% | 67% | -10.1¢ | -6.1¢ |
| Fair −2¢ | 80 | 37 | 46% | 57% | -15.1¢ | -7.0¢ |
| Fair −4¢ | 80 | 32 | 40% | 50% | -17.8¢ | -7.1¢ |
| Fair −6¢ | 80 | 30 | 38% | 47% | -19.0¢ | -7.1¢ |
| Fair −8¢ | 80 | 29 | 36% | 45% | -17.9¢ | -6.5¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2529 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 353 | 52% | 58% |
| 55-60% | 343 | 57% | 64% |
| 60-65% | 308 | 62% | 67% |
| 65-70% | 316 | 68% | 73% |
| 70-80% | 521 | 75% | 77% |
| 80-90% | 417 | 85% | 89% |
| 90%+ | 271 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 9:30 AM ET | UP 60% | 58¢ | skip | UP | Coinbase |
| Nov 21 9:25 AM ET | DOWN 59% | 56¢ | skip | UP | Polymarket |
| Nov 21 9:20 AM ET | UP 91% | 91¢ | skip | UP | Polymarket |
| Nov 21 9:15 AM ET | UP 57% | 51¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 9:10 AM ET | UP 88% | 70¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 9:05 AM ET | DOWN 67% | 89¢ | skip | DOWN | Polymarket |
| Nov 21 9:00 AM ET | UP 72% | 67¢ | UP | UP ✓ | Polymarket |
| Nov 21 8:55 AM ET | DOWN 69% | 73¢ | skip | UP | Polymarket |
| Nov 21 8:50 AM ET | UP 62% | 61¢ | skip | DOWN | Polymarket |
| Nov 21 7:40 AM ET | DOWN 73% | 92¢ | skip | UP | Polymarket |
| Nov 21 7:35 AM ET | UP 98% | 99¢ | skip | UP | Polymarket |
| Nov 21 7:25 AM ET | UP 58% | 65¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
