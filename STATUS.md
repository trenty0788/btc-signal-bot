# BTC 5-minute signal bot

Last update: **Nov 20 10:42 PM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 10:40 PM to 10:45 PM

Bot leans UP 77%, UP costs 89¢, edge -14¢ after fees.

Called at 10:42 PM. The result is known at 10:45 PM. Reload this page for the next call.

## Summary

- Windows logged: **429**
- Result confirmed by Polymarket: **428** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **83%** of the last 100 windows
- Bot has learned from **2432** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (429)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 429 | 79% | +0.2¢ |
| +0¢ | 148 | 72% | +5.3¢ |
| +2¢ | 118 | 68% | +4.8¢ |
| +4¢ | 98 | 65% | +4.4¢ |
| +6¢ | 76 | 63% | +6.2¢ |
| +8¢ | 56 | 59% | +6.8¢ |

**Only windows whose result Polymarket confirmed (428)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 428 | 79% | +0.2¢ |
| +0¢ | 148 | 72% | +5.3¢ |
| +2¢ | 118 | 68% | +4.8¢ |
| +4¢ | 98 | 65% | +4.4¢ |
| +6¢ | 76 | 63% | +6.2¢ |
| +8¢ | 56 | 59% | +6.8¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **10**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 10 | 9 | 90% | 89% | +5.8¢ | +5.2¢ |
| Fair −2¢ | 10 | 7 | 70% | 86% | +9.3¢ | +6.5¢ |
| Fair −4¢ | 10 | 5 | 50% | 80% | +11.6¢ | +5.8¢ |
| Fair −6¢ | 10 | 5 | 50% | 80% | +13.6¢ | +6.8¢ |
| Fair −8¢ | 10 | 5 | 50% | 80% | +15.6¢ | +7.8¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2432 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 342 | 52% | 59% |
| 55-60% | 334 | 57% | 65% |
| 60-65% | 293 | 62% | 67% |
| 65-70% | 307 | 68% | 73% |
| 70-80% | 499 | 75% | 77% |
| 80-90% | 401 | 85% | 89% |
| 90%+ | 256 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 20 10:35 PM ET | UP 76% | 89¢ | skip | UP | Coinbase |
| Nov 20 10:30 PM ET | DOWN 100% | 99¢ | skip | DOWN | Polymarket |
| Nov 20 10:25 PM ET | UP 67% | 71¢ | skip | DOWN | Polymarket |
| Nov 20 10:20 PM ET | UP 63% | 73¢ | skip | UP | Polymarket |
| Nov 20 10:15 PM ET | DOWN 88% | 93¢ | skip | DOWN | Polymarket |
| Nov 20 10:10 PM ET | UP 95% | 95¢ | skip | UP | Polymarket |
| Nov 20 10:05 PM ET | DOWN 90% | 84¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 20 10:00 PM ET | DOWN 86% | 82¢ | skip | DOWN | Polymarket |
| Nov 20 9:55 PM ET | DOWN 87% | 70¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 20 9:50 PM ET | DOWN 58% | 81¢ | skip | DOWN | Polymarket |
| Nov 20 9:45 PM ET | UP 88% | 87¢ | skip | UP | Polymarket |
| Nov 20 9:40 PM ET | DOWN 97% | 94¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
