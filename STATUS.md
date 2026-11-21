# BTC 5-minute signal bot

Last update: **Nov 20 11:07 PM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**▼ BET DOWN** for the window 11:05 PM to 11:10 PM

Bot leans DOWN 89%, DOWN costs 67¢, edge +20¢ after fees.

Called at 11:07 PM. The result is known at 11:10 PM. Reload this page for the next call.

## Summary

- Windows logged: **434**
- Result confirmed by Polymarket: **433** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **82%** of the last 100 windows
- Bot has learned from **2437** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (434)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 434 | 79% | -0.1¢ |
| +0¢ | 148 | 72% | +5.3¢ |
| +2¢ | 118 | 68% | +4.8¢ |
| +4¢ | 98 | 65% | +4.4¢ |
| +6¢ | 76 | 63% | +6.2¢ |
| +8¢ | 56 | 59% | +6.8¢ |

**Only windows whose result Polymarket confirmed (433)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 433 | 79% | +0.1¢ |
| +0¢ | 148 | 72% | +5.3¢ |
| +2¢ | 118 | 68% | +4.8¢ |
| +4¢ | 98 | 65% | +4.4¢ |
| +6¢ | 76 | 63% | +6.2¢ |
| +8¢ | 56 | 59% | +6.8¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **15**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 15 | 11 | 73% | 73% | -7.5¢ | -5.5¢ |
| Fair −2¢ | 15 | 9 | 60% | 67% | -7.3¢ | -4.4¢ |
| Fair −4¢ | 15 | 7 | 47% | 57% | -9.7¢ | -4.5¢ |
| Fair −6¢ | 15 | 7 | 47% | 57% | -7.7¢ | -3.6¢ |
| Fair −8¢ | 15 | 7 | 47% | 57% | -5.7¢ | -2.7¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2437 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 342 | 52% | 59% |
| 55-60% | 334 | 57% | 65% |
| 60-65% | 293 | 62% | 67% |
| 65-70% | 307 | 68% | 73% |
| 70-80% | 503 | 75% | 77% |
| 80-90% | 402 | 85% | 89% |
| 90%+ | 256 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 20 11:00 PM ET | UP 53% | 62¢ | skip | DOWN | Coinbase |
| Nov 20 10:55 PM ET | UP 74% | 81¢ | skip | UP | Polymarket |
| Nov 20 10:50 PM ET | DOWN 82% | 87¢ | skip | DOWN | Polymarket |
| Nov 20 10:45 PM ET | UP 73% | 80¢ | skip | UP | Polymarket |
| Nov 20 10:40 PM ET | UP 77% | 89¢ | skip | DOWN | Polymarket |
| Nov 20 10:35 PM ET | UP 76% | 89¢ | skip | UP | Polymarket |
| Nov 20 10:30 PM ET | DOWN 100% | 99¢ | skip | DOWN | Polymarket |
| Nov 20 10:25 PM ET | UP 67% | 71¢ | skip | DOWN | Polymarket |
| Nov 20 10:20 PM ET | UP 63% | 73¢ | skip | UP | Polymarket |
| Nov 20 10:15 PM ET | DOWN 88% | 93¢ | skip | DOWN | Polymarket |
| Nov 20 10:10 PM ET | UP 95% | 95¢ | skip | UP | Polymarket |
| Nov 20 10:05 PM ET | DOWN 90% | 84¢ | DOWN | DOWN ✓ | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
