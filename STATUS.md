# BTC 5-minute signal bot

Last update: **Nov 21 12:07 AM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 12:05 AM to 12:10 AM

Bot leans DOWN 78%, DOWN costs 85¢, edge -9¢ after fees.

Called at 12:07 AM. The result is known at 12:10 AM. Reload this page for the next call.

## Summary

- Windows logged: **446**
- Result confirmed by Polymarket: **445** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **81%** of the last 100 windows
- Bot has learned from **2449** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (446)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 446 | 78% | -0.2¢ |
| +0¢ | 153 | 70% | +4.3¢ |
| +2¢ | 123 | 66% | +3.6¢ |
| +4¢ | 103 | 63% | +3.0¢ |
| +6¢ | 81 | 60% | +4.2¢ |
| +8¢ | 61 | 56% | +4.1¢ |

**Only windows whose result Polymarket confirmed (445)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 445 | 78% | -0.2¢ |
| +0¢ | 153 | 70% | +4.3¢ |
| +2¢ | 123 | 66% | +3.6¢ |
| +4¢ | 103 | 63% | +3.0¢ |
| +6¢ | 81 | 60% | +4.2¢ |
| +8¢ | 61 | 56% | +4.1¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **22**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 22 | 12 | 55% | 75% | -6.1¢ | -3.3¢ |
| Fair −2¢ | 22 | 10 | 45% | 70% | -5.5¢ | -2.5¢ |
| Fair −4¢ | 22 | 8 | 36% | 62% | -6.9¢ | -2.5¢ |
| Fair −6¢ | 22 | 8 | 36% | 62% | -4.9¢ | -1.8¢ |
| Fair −8¢ | 22 | 8 | 36% | 62% | -2.9¢ | -1.1¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2449 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 345 | 52% | 58% |
| 55-60% | 335 | 57% | 64% |
| 60-65% | 295 | 62% | 67% |
| 65-70% | 308 | 68% | 73% |
| 70-80% | 505 | 75% | 77% |
| 80-90% | 404 | 85% | 89% |
| 90%+ | 257 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 12:00 AM ET | UP 89% | 95¢ | skip | UP | Coinbase |
| Nov 20 11:55 PM ET | DOWN 65% | 83¢ | skip | DOWN | Polymarket |
| Nov 20 11:50 PM ET | UP 86% | 93¢ | skip | UP | Polymarket |
| Nov 20 11:45 PM ET | UP 97% | 97¢ | skip | UP | Polymarket |
| Nov 20 11:40 PM ET | UP 64% | 46¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:35 PM ET | UP 62% | 83¢ | skip | UP | Polymarket |
| Nov 20 11:30 PM ET | UP 80% | 86¢ | skip | UP | Polymarket |
| Nov 20 11:25 PM ET | UP 50% | 39¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:20 PM ET | UP 55% | 41¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:15 PM ET | UP 51% | 27¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:10 PM ET | UP 70% | 76¢ | skip | UP | Polymarket |
| Nov 20 11:05 PM ET | DOWN 89% | 67¢ | DOWN | DOWN ✓ | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
