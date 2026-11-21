# BTC 5-minute signal bot

Last update: **Nov 20 11:27 PM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**▲ BET UP** for the window 11:25 PM to 11:30 PM

Bot leans UP 50%, UP costs 39¢, edge +9¢ after fees.

Called at 11:27 PM. The result is known at 11:30 PM. Reload this page for the next call.

## Summary

- Windows logged: **438**
- Result confirmed by Polymarket: **437** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **81%** of the last 100 windows
- Bot has learned from **2441** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (438)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 438 | 79% | -0.1¢ |
| +0¢ | 151 | 71% | +5.0¢ |
| +2¢ | 121 | 67% | +4.4¢ |
| +4¢ | 101 | 64% | +3.9¢ |
| +6¢ | 79 | 62% | +5.4¢ |
| +8¢ | 59 | 58% | +5.7¢ |

**Only windows whose result Polymarket confirmed (437)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 437 | 79% | -0.0¢ |
| +0¢ | 150 | 71% | +5.3¢ |
| +2¢ | 120 | 68% | +4.8¢ |
| +4¢ | 100 | 65% | +4.4¢ |
| +6¢ | 78 | 63% | +6.1¢ |
| +8¢ | 58 | 59% | +6.6¢ |

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

Across 2441 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 344 | 52% | 58% |
| 55-60% | 334 | 57% | 65% |
| 60-65% | 293 | 62% | 67% |
| 65-70% | 307 | 68% | 73% |
| 70-80% | 504 | 75% | 77% |
| 80-90% | 403 | 85% | 89% |
| 90%+ | 256 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 20 11:20 PM ET | UP 55% | 41¢ | UP | DOWN ✗ | Coinbase |
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
| Nov 20 10:25 PM ET | UP 67% | 71¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
