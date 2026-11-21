# BTC 5-minute signal bot

Last update: **Nov 20 11:57 PM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 11:55 PM to 12:00 AM

Bot leans DOWN 65%, DOWN costs 83¢, edge -20¢ after fees.

Called at 11:57 PM. The result is known at 12:00 AM. Reload this page for the next call.

## Summary

- Windows logged: **444**
- Result confirmed by Polymarket: **443** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **81%** of the last 100 windows
- Bot has learned from **2447** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (444)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 444 | 78% | -0.2¢ |
| +0¢ | 153 | 70% | +4.3¢ |
| +2¢ | 123 | 66% | +3.6¢ |
| +4¢ | 103 | 63% | +3.0¢ |
| +6¢ | 81 | 60% | +4.2¢ |
| +8¢ | 61 | 56% | +4.1¢ |

**Only windows whose result Polymarket confirmed (443)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 443 | 78% | -0.3¢ |
| +0¢ | 153 | 70% | +4.3¢ |
| +2¢ | 123 | 66% | +3.6¢ |
| +4¢ | 103 | 63% | +3.0¢ |
| +6¢ | 81 | 60% | +4.2¢ |
| +8¢ | 61 | 56% | +4.1¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **20**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 20 | 11 | 55% | 73% | -7.5¢ | -4.1¢ |
| Fair −2¢ | 20 | 9 | 45% | 67% | -7.3¢ | -3.3¢ |
| Fair −4¢ | 20 | 7 | 35% | 57% | -9.7¢ | -3.4¢ |
| Fair −6¢ | 20 | 7 | 35% | 57% | -7.7¢ | -2.7¢ |
| Fair −8¢ | 20 | 7 | 35% | 57% | -5.7¢ | -2.0¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2447 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 345 | 52% | 58% |
| 55-60% | 335 | 57% | 64% |
| 60-65% | 295 | 62% | 67% |
| 65-70% | 307 | 68% | 73% |
| 70-80% | 505 | 75% | 77% |
| 80-90% | 403 | 85% | 89% |
| 90%+ | 257 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 20 11:50 PM ET | UP 86% | 93¢ | skip | UP | Coinbase (close) |
| Nov 20 11:45 PM ET | UP 97% | 97¢ | skip | UP | Polymarket |
| Nov 20 11:40 PM ET | UP 64% | 46¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:35 PM ET | UP 62% | 83¢ | skip | UP | Polymarket |
| Nov 20 11:30 PM ET | UP 80% | 86¢ | skip | UP | Polymarket |
| Nov 20 11:25 PM ET | UP 50% | 39¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:20 PM ET | UP 55% | 41¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:15 PM ET | UP 51% | 27¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:10 PM ET | UP 70% | 76¢ | skip | UP | Polymarket |
| Nov 20 11:05 PM ET | DOWN 89% | 67¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 20 11:00 PM ET | UP 53% | 62¢ | skip | DOWN | Polymarket |
| Nov 20 10:55 PM ET | UP 74% | 81¢ | skip | UP | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
