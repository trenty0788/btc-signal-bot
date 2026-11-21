# BTC 5-minute signal bot

Last update: **Nov 21 8:07 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 8:05 AM to 8:10 AM

Bot leans UP 92%, UP costs 96¢, edge -6¢ after fees.

Called at 8:07 AM. The result is known at 8:10 AM. Reload this page for the next call.

## Summary

- Windows logged: **521**
- Result confirmed by Polymarket: **520** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **74%** of the last 100 windows
- Bot has learned from **2524** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (521)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 521 | 78% | -0.4¢ |
| +0¢ | 178 | 67% | +2.0¢ |
| +2¢ | 142 | 64% | +2.0¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

**Only windows whose result Polymarket confirmed (520)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 520 | 78% | -0.5¢ |
| +0¢ | 178 | 67% | +2.0¢ |
| +2¢ | 142 | 64% | +2.0¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **78**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 78 | 44 | 56% | 70% | -6.8¢ | -3.8¢ |
| Fair −2¢ | 78 | 34 | 44% | 62% | -10.9¢ | -4.7¢ |
| Fair −4¢ | 78 | 29 | 37% | 55% | -13.4¢ | -5.0¢ |
| Fair −6¢ | 78 | 27 | 35% | 52% | -14.5¢ | -5.0¢ |
| Fair −8¢ | 78 | 26 | 33% | 50% | -13.4¢ | -4.5¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2524 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 353 | 52% | 58% |
| 55-60% | 343 | 57% | 64% |
| 60-65% | 308 | 62% | 67% |
| 65-70% | 314 | 68% | 74% |
| 70-80% | 520 | 75% | 77% |
| 80-90% | 416 | 85% | 89% |
| 90%+ | 270 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 8:00 AM ET | UP 66% | 88¢ | skip | UP | Coinbase |
| Nov 21 7:55 AM ET | UP 60% | 72¢ | skip | UP | Polymarket |
| Nov 21 7:50 AM ET | DOWN 60% | 77¢ | skip | DOWN | Polymarket |
| Nov 21 7:45 AM ET | DOWN 61% | 70¢ | skip | DOWN | Polymarket |
| Nov 21 7:40 AM ET | DOWN 73% | 92¢ | skip | UP | Polymarket |
| Nov 21 7:35 AM ET | UP 98% | 99¢ | skip | UP | Polymarket |
| Nov 21 7:25 AM ET | UP 58% | 65¢ | skip | DOWN | Polymarket |
| Nov 21 7:20 AM ET | DOWN 88% | 86¢ | skip | DOWN | Polymarket |
| Nov 21 7:15 AM ET | UP 59% | 67¢ | skip | UP | Polymarket |
| Nov 21 7:10 AM ET | UP 86% | 87¢ | skip | UP | Polymarket |
| Nov 21 7:05 AM ET | UP 72% | 70¢ | skip | UP | Polymarket |
| Nov 21 7:00 AM ET | DOWN 67% | 77¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
