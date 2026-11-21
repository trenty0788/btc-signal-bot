# BTC 5-minute signal bot

Last update: **Nov 20 11:32 PM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 11:30 PM to 11:35 PM

Bot leans UP 80%, UP costs 86¢, edge -8¢ after fees.

Called at 11:32 PM. The result is known at 11:35 PM. Reload this page for the next call.

## Summary

- Windows logged: **439**
- Result confirmed by Polymarket: **438** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **81%** of the last 100 windows
- Bot has learned from **2442** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (439)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 439 | 78% | -0.2¢ |
| +0¢ | 152 | 70% | +4.7¢ |
| +2¢ | 122 | 66% | +4.0¢ |
| +4¢ | 102 | 64% | +3.5¢ |
| +6¢ | 80 | 61% | +4.9¢ |
| +8¢ | 60 | 57% | +4.9¢ |

**Only windows whose result Polymarket confirmed (438)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 438 | 79% | -0.1¢ |
| +0¢ | 151 | 71% | +5.0¢ |
| +2¢ | 121 | 67% | +4.4¢ |
| +4¢ | 101 | 64% | +3.9¢ |
| +6¢ | 79 | 62% | +5.4¢ |
| +8¢ | 59 | 58% | +5.7¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **16**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 16 | 11 | 69% | 73% | -7.5¢ | -5.1¢ |
| Fair −2¢ | 16 | 9 | 56% | 67% | -7.3¢ | -4.1¢ |
| Fair −4¢ | 16 | 7 | 44% | 57% | -9.7¢ | -4.3¢ |
| Fair −6¢ | 16 | 7 | 44% | 57% | -7.7¢ | -3.4¢ |
| Fair −8¢ | 16 | 7 | 44% | 57% | -5.7¢ | -2.5¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2442 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 344 | 52% | 58% |
| 55-60% | 335 | 57% | 64% |
| 60-65% | 293 | 62% | 67% |
| 65-70% | 307 | 68% | 73% |
| 70-80% | 504 | 75% | 77% |
| 80-90% | 403 | 85% | 89% |
| 90%+ | 256 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 20 11:25 PM ET | UP 50% | 39¢ | UP | DOWN ✗ | Coinbase |
| Nov 20 11:20 PM ET | UP 55% | 41¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:15 PM ET | UP 51% | 27¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:10 PM ET | UP 70% | 76¢ | skip | UP | Polymarket |
| Nov 20 11:05 PM ET | DOWN 89% | 67¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 20 11:00 PM ET | UP 53% | 62¢ | skip | DOWN | Polymarket |
| Nov 20 10:55 PM ET | UP 74% | 81¢ | skip | UP | Polymarket |
| Nov 20 10:50 PM ET | DOWN 82% | 87¢ | skip | DOWN | Polymarket |
| Nov 20 10:45 PM ET | UP 73% | 80¢ | skip | UP | Polymarket |
| Nov 20 10:40 PM ET | UP 77% | 89¢ | skip | DOWN | Polymarket |
| Nov 20 10:35 PM ET | UP 76% | 89¢ | skip | UP | Polymarket |
| Nov 20 10:30 PM ET | DOWN 100% | 99¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
