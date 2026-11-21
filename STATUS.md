# BTC 5-minute signal bot

Last update: **Nov 20 11:42 PM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**▲ BET UP** for the window 11:40 PM to 11:45 PM

Bot leans UP 64%, UP costs 46¢, edge +16¢ after fees.

Called at 11:42 PM. The result is known at 11:45 PM. Reload this page for the next call.

## Summary

- Windows logged: **441**
- Result confirmed by Polymarket: **440** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **80%** of the last 100 windows
- Bot has learned from **2444** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (441)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 441 | 78% | -0.4¢ |
| +0¢ | 152 | 70% | +4.7¢ |
| +2¢ | 122 | 66% | +4.0¢ |
| +4¢ | 102 | 64% | +3.5¢ |
| +6¢ | 80 | 61% | +4.9¢ |
| +8¢ | 60 | 57% | +4.9¢ |

**Only windows whose result Polymarket confirmed (440)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 440 | 78% | -0.2¢ |
| +0¢ | 152 | 70% | +4.7¢ |
| +2¢ | 122 | 66% | +4.0¢ |
| +4¢ | 102 | 64% | +3.5¢ |
| +6¢ | 80 | 61% | +4.9¢ |
| +8¢ | 60 | 57% | +4.9¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **18**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 18 | 11 | 61% | 73% | -7.5¢ | -4.6¢ |
| Fair −2¢ | 18 | 9 | 50% | 67% | -7.3¢ | -3.6¢ |
| Fair −4¢ | 18 | 7 | 39% | 57% | -9.7¢ | -3.8¢ |
| Fair −6¢ | 18 | 7 | 39% | 57% | -7.7¢ | -3.0¢ |
| Fair −8¢ | 18 | 7 | 39% | 57% | -5.7¢ | -2.2¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2444 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 345 | 52% | 58% |
| 55-60% | 335 | 57% | 64% |
| 60-65% | 293 | 62% | 67% |
| 65-70% | 307 | 68% | 73% |
| 70-80% | 505 | 75% | 77% |
| 80-90% | 403 | 85% | 89% |
| 90%+ | 256 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 20 11:35 PM ET | UP 62% | 83¢ | skip | DOWN | Coinbase |
| Nov 20 11:30 PM ET | UP 80% | 86¢ | skip | UP | Polymarket |
| Nov 20 11:25 PM ET | UP 50% | 39¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:20 PM ET | UP 55% | 41¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:15 PM ET | UP 51% | 27¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:10 PM ET | UP 70% | 76¢ | skip | UP | Polymarket |
| Nov 20 11:05 PM ET | DOWN 89% | 67¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 20 11:00 PM ET | UP 53% | 62¢ | skip | DOWN | Polymarket |
| Nov 20 10:55 PM ET | UP 74% | 81¢ | skip | UP | Polymarket |
| Nov 20 10:50 PM ET | DOWN 82% | 87¢ | skip | DOWN | Polymarket |
| Nov 20 10:45 PM ET | UP 73% | 80¢ | skip | UP | Polymarket |
| Nov 20 10:40 PM ET | UP 77% | 89¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
