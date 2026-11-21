# BTC 5-minute signal bot

Last update: **Nov 21 6:52 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 6:50 AM to 6:55 AM

Bot leans UP 61%, UP costs 58¢, edge +1¢ after fees.

Called at 6:52 AM. The result is known at 6:55 AM. Reload this page for the next call.

## Summary

- Windows logged: **507**
- Result confirmed by Polymarket: **506** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **73%** of the last 100 windows
- Bot has learned from **2510** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (507)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 507 | 78% | -0.6¢ |
| +0¢ | 177 | 68% | +2.4¢ |
| +2¢ | 142 | 64% | +2.0¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

**Only windows whose result Polymarket confirmed (506)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 506 | 78% | -0.5¢ |
| +0¢ | 177 | 68% | +2.4¢ |
| +2¢ | 142 | 64% | +2.0¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **64**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 64 | 36 | 56% | 69% | -9.5¢ | -5.3¢ |
| Fair −2¢ | 64 | 27 | 42% | 59% | -14.5¢ | -6.1¢ |
| Fair −4¢ | 64 | 23 | 36% | 52% | -17.8¢ | -6.4¢ |
| Fair −6¢ | 64 | 22 | 34% | 50% | -17.9¢ | -6.1¢ |
| Fair −8¢ | 64 | 21 | 33% | 48% | -17.2¢ | -5.6¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2510 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 352 | 52% | 58% |
| 55-60% | 339 | 57% | 64% |
| 60-65% | 305 | 62% | 67% |
| 65-70% | 313 | 68% | 73% |
| 70-80% | 518 | 75% | 77% |
| 80-90% | 414 | 85% | 89% |
| 90%+ | 269 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 6:45 AM ET | UP 54% | 64¢ | skip | DOWN | Coinbase (close) |
| Nov 21 6:40 AM ET | UP 52% | 65¢ | skip | DOWN | Polymarket |
| Nov 21 6:35 AM ET | DOWN 84% | 95¢ | skip | DOWN | Polymarket |
| Nov 21 6:30 AM ET | UP 100% | 98¢ | skip | UP | Polymarket |
| Nov 21 6:25 AM ET | UP 51% | 59¢ | skip | UP | Polymarket |
| Nov 21 6:20 AM ET | UP 69% | 82¢ | skip | UP | Polymarket |
| Nov 21 6:15 AM ET | DOWN 98% | 96¢ | skip | DOWN | Polymarket |
| Nov 21 6:10 AM ET | UP 62% | 80¢ | skip | DOWN | Polymarket |
| Nov 21 6:05 AM ET | DOWN 58% | 42¢ | DOWN | UP ✗ | Polymarket |
| Nov 21 6:00 AM ET | DOWN 82% | 84¢ | skip | DOWN | Polymarket |
| Nov 21 5:55 AM ET | DOWN 75% | 83¢ | skip | DOWN | Polymarket |
| Nov 21 5:50 AM ET | UP 64% | 76¢ | skip | UP | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
