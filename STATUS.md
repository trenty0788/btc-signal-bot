# BTC 5-minute signal bot

Last update: **Nov 21 7:12 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 7:10 AM to 7:15 AM

Bot leans UP 86%, UP costs 87¢, edge -3¢ after fees.

Called at 7:12 AM. The result is known at 7:15 AM. Reload this page for the next call.

## Summary

- Windows logged: **511**
- Result confirmed by Polymarket: **510** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **75%** of the last 100 windows
- Bot has learned from **2514** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (511)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 511 | 78% | -0.4¢ |
| +0¢ | 178 | 67% | +2.0¢ |
| +2¢ | 142 | 64% | +2.0¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

**Only windows whose result Polymarket confirmed (510)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 510 | 78% | -0.4¢ |
| +0¢ | 178 | 67% | +2.0¢ |
| +2¢ | 142 | 64% | +2.0¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **68**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 68 | 40 | 59% | 72% | -5.3¢ | -3.1¢ |
| Fair −2¢ | 68 | 30 | 44% | 63% | -9.7¢ | -4.3¢ |
| Fair −4¢ | 68 | 26 | 38% | 58% | -11.7¢ | -4.5¢ |
| Fair −6¢ | 68 | 24 | 35% | 54% | -13.1¢ | -4.6¢ |
| Fair −8¢ | 68 | 23 | 34% | 52% | -12.0¢ | -4.1¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2514 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 353 | 52% | 58% |
| 55-60% | 339 | 57% | 64% |
| 60-65% | 307 | 62% | 67% |
| 65-70% | 314 | 68% | 74% |
| 70-80% | 518 | 75% | 77% |
| 80-90% | 414 | 85% | 89% |
| 90%+ | 269 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 7:05 AM ET | UP 72% | 70¢ | skip | UP | Coinbase (close) |
| Nov 21 7:00 AM ET | DOWN 67% | 77¢ | skip | DOWN | Polymarket |
| Nov 21 6:55 AM ET | UP 64% | 83¢ | skip | UP | Polymarket |
| Nov 21 6:50 AM ET | UP 61% | 58¢ | skip | DOWN | Polymarket |
| Nov 21 6:45 AM ET | UP 54% | 64¢ | skip | UP | Polymarket |
| Nov 21 6:40 AM ET | UP 52% | 65¢ | skip | DOWN | Polymarket |
| Nov 21 6:35 AM ET | DOWN 84% | 95¢ | skip | DOWN | Polymarket |
| Nov 21 6:30 AM ET | UP 100% | 98¢ | skip | UP | Polymarket |
| Nov 21 6:25 AM ET | UP 51% | 59¢ | skip | UP | Polymarket |
| Nov 21 6:20 AM ET | UP 69% | 82¢ | skip | UP | Polymarket |
| Nov 21 6:15 AM ET | DOWN 98% | 96¢ | skip | DOWN | Polymarket |
| Nov 21 6:10 AM ET | UP 62% | 80¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
