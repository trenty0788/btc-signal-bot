# BTC 5-minute signal bot

Last update: **Nov 20 10:12 PM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 10:10 PM to 10:15 PM

Bot leans UP 95%, UP costs 95¢, edge -2¢ after fees.

Called at 10:12 PM. The result is known at 10:15 PM. Reload this page for the next call.

## Summary

- Windows logged: **423**
- Result confirmed by Polymarket: **422** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **83%** of the last 100 windows
- Bot has learned from **2426** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (423)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 423 | 79% | +0.3¢ |
| +0¢ | 148 | 72% | +5.3¢ |
| +2¢ | 118 | 68% | +4.8¢ |
| +4¢ | 98 | 65% | +4.4¢ |
| +6¢ | 76 | 63% | +6.2¢ |
| +8¢ | 56 | 59% | +6.8¢ |

**Only windows whose result Polymarket confirmed (422)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 422 | 79% | +0.2¢ |
| +0¢ | 147 | 71% | +5.3¢ |
| +2¢ | 117 | 68% | +4.8¢ |
| +4¢ | 97 | 65% | +4.3¢ |
| +6¢ | 76 | 63% | +6.2¢ |
| +8¢ | 56 | 59% | +6.8¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **4**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 4 | 4 | 100% | 100% | +15.9¢ | +15.9¢ |
| Fair −2¢ | 4 | 4 | 100% | 100% | +17.9¢ | +17.9¢ |
| Fair −4¢ | 4 | 2 | 50% | 100% | +29.3¢ | +14.6¢ |
| Fair −6¢ | 4 | 2 | 50% | 100% | +31.3¢ | +15.6¢ |
| Fair −8¢ | 4 | 2 | 50% | 100% | +33.3¢ | +16.6¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2426 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 342 | 52% | 59% |
| 55-60% | 334 | 57% | 65% |
| 60-65% | 292 | 62% | 67% |
| 65-70% | 306 | 68% | 73% |
| 70-80% | 499 | 75% | 77% |
| 80-90% | 400 | 85% | 89% |
| 90%+ | 253 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 20 10:05 PM ET | DOWN 90% | 84¢ | DOWN | DOWN ✓ | Coinbase |
| Nov 20 10:00 PM ET | DOWN 86% | 82¢ | skip | DOWN | Polymarket |
| Nov 20 9:55 PM ET | DOWN 87% | 70¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 20 9:50 PM ET | DOWN 58% | 81¢ | skip | DOWN | Polymarket |
| Nov 20 9:45 PM ET | UP 88% | 87¢ | skip | UP | Polymarket |
| Nov 20 9:40 PM ET | DOWN 97% | 94¢ | skip | DOWN | Polymarket |
| Nov 20 9:30 PM ET | DOWN 73% | 82¢ | skip | DOWN | Polymarket |
| Nov 20 9:25 PM ET | DOWN 69% | 75¢ | skip | DOWN | Polymarket |
| Nov 20 9:20 PM ET | DOWN 69% | 75¢ | skip | DOWN | Polymarket |
| Nov 20 9:15 PM ET | DOWN 77% | 85¢ | skip | DOWN | Polymarket |
| Nov 20 9:10 PM ET | UP 89% | 84¢ | UP | UP ✓ | Polymarket |
| Nov 20 9:05 PM ET | UP 86% | 92¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
