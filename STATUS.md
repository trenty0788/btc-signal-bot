# BTC 5-minute signal bot

Last update: **Nov 21 1:47 AM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 1:45 AM to 1:50 AM

Bot leans UP 90%, UP costs 89¢, edge -1¢ after fees.

Called at 1:47 AM. The result is known at 1:50 AM. Reload this page for the next call.

## Summary

- Windows logged: **466**
- Result confirmed by Polymarket: **465** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **75%** of the last 100 windows
- Bot has learned from **2469** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (466)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 466 | 78% | -0.4¢ |
| +0¢ | 163 | 68% | +2.7¢ |
| +2¢ | 130 | 65% | +2.8¢ |
| +4¢ | 109 | 62% | +2.5¢ |
| +6¢ | 87 | 60% | +3.5¢ |
| +8¢ | 67 | 55% | +3.2¢ |

**Only windows whose result Polymarket confirmed (465)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 465 | 78% | -0.5¢ |
| +0¢ | 162 | 68% | +2.7¢ |
| +2¢ | 130 | 65% | +2.8¢ |
| +4¢ | 109 | 62% | +2.5¢ |
| +6¢ | 87 | 60% | +3.5¢ |
| +8¢ | 67 | 55% | +3.2¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **35**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 35 | 17 | 49% | 65% | -15.1¢ | -7.4¢ |
| Fair −2¢ | 35 | 15 | 43% | 60% | -15.2¢ | -6.5¢ |
| Fair −4¢ | 35 | 11 | 31% | 45% | -24.5¢ | -7.7¢ |
| Fair −6¢ | 35 | 11 | 31% | 45% | -22.5¢ | -7.1¢ |
| Fair −8¢ | 35 | 11 | 31% | 45% | -20.5¢ | -6.4¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2469 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 349 | 52% | 58% |
| 55-60% | 335 | 57% | 64% |
| 60-65% | 299 | 62% | 67% |
| 65-70% | 309 | 68% | 73% |
| 70-80% | 509 | 75% | 77% |
| 80-90% | 407 | 85% | 89% |
| 90%+ | 261 | 94% | 93% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 1:40 AM ET | UP 93% | 90¢ | skip | UP | Coinbase |
| Nov 21 1:35 AM ET | UP 51% | 40¢ | UP | UP ✓ | Polymarket |
| Nov 21 1:30 AM ET | UP 61% | 61¢ | skip | UP | Polymarket |
| Nov 21 1:25 AM ET | UP 72% | 80¢ | skip | UP | Polymarket |
| Nov 21 1:20 AM ET | DOWN 80% | 58¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 21 1:15 AM ET | DOWN 100% | 89¢ | DOWN | UP ✗ | Polymarket |
| Nov 21 1:10 AM ET | UP 90% | 61¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 1:05 AM ET | UP 63% | 51¢ | UP | UP ✓ | Polymarket |
| Nov 21 1:00 AM ET | UP 52% | 49¢ | skip | DOWN | Polymarket |
| Nov 21 12:55 AM ET | UP 54% | 48¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 12:50 AM ET | DOWN 69% | 79¢ | skip | DOWN | Polymarket |
| Nov 21 12:45 AM ET | UP 61% | 64¢ | skip | UP | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
