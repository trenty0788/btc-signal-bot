# BTC 5-minute signal bot

Last update: **Nov 21 9:07 AM ET** (this job started Nov 21 8:50 AM ET)

## Latest call

**SKIP** for the window 9:05 AM to 9:10 AM

Bot leans DOWN 67%, DOWN costs 89¢, edge -24¢ after fees.

Called at 9:07 AM. The result is known at 9:10 AM. Reload this page for the next call.

## Summary

- Windows logged: **520**
- Result confirmed by Polymarket: **519** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **71%** of the last 100 windows
- Bot has learned from **2523** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (520)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 520 | 77% | -1.0¢ |
| +0¢ | 179 | 67% | +1.6¢ |
| +2¢ | 143 | 64% | +1.5¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

**Only windows whose result Polymarket confirmed (519)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 519 | 77% | -0.9¢ |
| +0¢ | 178 | 67% | +2.0¢ |
| +2¢ | 142 | 64% | +2.0¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **1**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **76**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 76 | 45 | 59% | 67% | -10.5¢ | -6.2¢ |
| Fair −2¢ | 76 | 35 | 46% | 57% | -15.4¢ | -7.1¢ |
| Fair −4¢ | 76 | 30 | 39% | 50% | -18.5¢ | -7.3¢ |
| Fair −6¢ | 76 | 28 | 37% | 46% | -19.9¢ | -7.3¢ |
| Fair −8¢ | 76 | 27 | 36% | 44% | -19.0¢ | -6.8¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2523 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 353 | 52% | 58% |
| 55-60% | 341 | 57% | 64% |
| 60-65% | 308 | 62% | 67% |
| 65-70% | 315 | 68% | 73% |
| 70-80% | 520 | 75% | 77% |
| 80-90% | 416 | 85% | 89% |
| 90%+ | 270 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 9:00 AM ET | UP 72% | 67¢ | UP | DOWN ✗ | Coinbase (close) |
| Nov 21 8:55 AM ET | DOWN 69% | 73¢ | skip | UP | Polymarket |
| Nov 21 8:50 AM ET | UP 62% | 61¢ | skip | DOWN | Polymarket |
| Nov 21 7:40 AM ET | DOWN 73% | 92¢ | skip | UP | Polymarket |
| Nov 21 7:35 AM ET | UP 98% | 99¢ | skip | UP | Polymarket |
| Nov 21 7:25 AM ET | UP 58% | 65¢ | skip | DOWN | Polymarket |
| Nov 21 7:20 AM ET | DOWN 88% | 86¢ | skip | DOWN | Polymarket |
| Nov 21 7:15 AM ET | UP 59% | 67¢ | skip | UP | Polymarket |
| Nov 21 7:10 AM ET | UP 86% | 87¢ | skip | UP | Polymarket |
| Nov 21 7:05 AM ET | UP 72% | 70¢ | skip | UP | Polymarket |
| Nov 21 7:00 AM ET | DOWN 67% | 77¢ | skip | DOWN | Polymarket |
| Nov 21 6:55 AM ET | UP 64% | 83¢ | skip | UP | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
