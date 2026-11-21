# BTC 5-minute signal bot

Last update: **Nov 21 9:17 AM ET** (this job started Nov 21 8:50 AM ET)

## Latest call

**▲ BET UP** for the window 9:15 AM to 9:20 AM

Bot leans UP 57%, UP costs 51¢, edge +4¢ after fees.

Called at 9:17 AM. The result is known at 9:20 AM. Reload this page for the next call.

## Summary

- Windows logged: **522**
- Result confirmed by Polymarket: **521** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **72%** of the last 100 windows
- Bot has learned from **2525** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (522)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 522 | 78% | -0.7¢ |
| +0¢ | 180 | 68% | +2.3¢ |
| +2¢ | 144 | 65% | +2.4¢ |
| +4¢ | 118 | 63% | +2.6¢ |
| +6¢ | 94 | 61% | +3.9¢ |
| +8¢ | 73 | 58% | +4.5¢ |

**Only windows whose result Polymarket confirmed (521)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 521 | 78% | -0.8¢ |
| +0¢ | 179 | 68% | +2.2¢ |
| +2¢ | 143 | 64% | +2.2¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **1**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **77**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 77 | 45 | 58% | 67% | -10.5¢ | -6.1¢ |
| Fair −2¢ | 77 | 35 | 45% | 57% | -15.4¢ | -7.0¢ |
| Fair −4¢ | 77 | 30 | 39% | 50% | -18.5¢ | -7.2¢ |
| Fair −6¢ | 77 | 28 | 36% | 46% | -19.9¢ | -7.2¢ |
| Fair −8¢ | 77 | 27 | 35% | 44% | -19.0¢ | -6.7¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2525 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 353 | 52% | 58% |
| 55-60% | 341 | 57% | 64% |
| 60-65% | 308 | 62% | 67% |
| 65-70% | 316 | 68% | 73% |
| 70-80% | 521 | 75% | 77% |
| 80-90% | 416 | 85% | 89% |
| 90%+ | 270 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 9:10 AM ET | UP 88% | 70¢ | UP | UP ✓ | Coinbase (close) |
| Nov 21 9:05 AM ET | DOWN 67% | 89¢ | skip | DOWN | Polymarket |
| Nov 21 9:00 AM ET | UP 72% | 67¢ | UP | UP ✓ | Polymarket |
| Nov 21 8:55 AM ET | DOWN 69% | 73¢ | skip | UP | Polymarket |
| Nov 21 8:50 AM ET | UP 62% | 61¢ | skip | DOWN | Polymarket |
| Nov 21 7:40 AM ET | DOWN 73% | 92¢ | skip | UP | Polymarket |
| Nov 21 7:35 AM ET | UP 98% | 99¢ | skip | UP | Polymarket |
| Nov 21 7:25 AM ET | UP 58% | 65¢ | skip | DOWN | Polymarket |
| Nov 21 7:20 AM ET | DOWN 88% | 86¢ | skip | DOWN | Polymarket |
| Nov 21 7:15 AM ET | UP 59% | 67¢ | skip | UP | Polymarket |
| Nov 21 7:10 AM ET | UP 86% | 87¢ | skip | UP | Polymarket |
| Nov 21 7:05 AM ET | UP 72% | 70¢ | skip | UP | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
