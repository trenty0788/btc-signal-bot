# BTC 5-minute signal bot

Last update: **Nov 21 12:37 AM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 12:35 AM to 12:40 AM

Bot leans DOWN 92%, DOWN costs 88¢, edge +2¢ after fees.

Called at 12:37 AM. The result is known at 12:40 AM. Reload this page for the next call.

## Summary

- Windows logged: **452**
- Result confirmed by Polymarket: **451** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **80%** of the last 100 windows
- Bot has learned from **2455** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (452)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 452 | 78% | -0.3¢ |
| +0¢ | 154 | 69% | +4.1¢ |
| +2¢ | 124 | 65% | +3.4¢ |
| +4¢ | 104 | 62% | +2.7¢ |
| +6¢ | 82 | 60% | +3.9¢ |
| +8¢ | 62 | 55% | +3.6¢ |

**Only windows whose result Polymarket confirmed (451)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 451 | 78% | -0.3¢ |
| +0¢ | 154 | 69% | +4.1¢ |
| +2¢ | 124 | 65% | +3.4¢ |
| +4¢ | 104 | 62% | +2.7¢ |
| +6¢ | 82 | 60% | +3.9¢ |
| +8¢ | 62 | 55% | +3.6¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **27**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 27 | 13 | 48% | 69% | -11.6¢ | -5.6¢ |
| Fair −2¢ | 27 | 11 | 41% | 64% | -11.8¢ | -4.8¢ |
| Fair −4¢ | 27 | 9 | 33% | 56% | -14.3¢ | -4.8¢ |
| Fair −6¢ | 27 | 9 | 33% | 56% | -12.3¢ | -4.1¢ |
| Fair −8¢ | 27 | 9 | 33% | 56% | -10.3¢ | -3.4¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2455 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 346 | 52% | 58% |
| 55-60% | 335 | 57% | 64% |
| 60-65% | 296 | 62% | 67% |
| 65-70% | 308 | 68% | 73% |
| 70-80% | 508 | 75% | 77% |
| 80-90% | 405 | 85% | 89% |
| 90%+ | 257 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 12:30 AM ET | DOWN 94% | 95¢ | skip | DOWN | Coinbase |
| Nov 21 12:25 AM ET | UP 53% | 67¢ | skip | UP | Polymarket |
| Nov 21 12:20 AM ET | UP 65% | 22¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 12:15 AM ET | UP 77% | 80¢ | skip | UP | Polymarket |
| Nov 21 12:10 AM ET | UP 75% | 78¢ | skip | DOWN | Polymarket |
| Nov 21 12:05 AM ET | DOWN 78% | 85¢ | skip | DOWN | Polymarket |
| Nov 21 12:00 AM ET | UP 89% | 95¢ | skip | UP | Polymarket |
| Nov 20 11:55 PM ET | DOWN 65% | 83¢ | skip | DOWN | Polymarket |
| Nov 20 11:50 PM ET | UP 86% | 93¢ | skip | UP | Polymarket |
| Nov 20 11:45 PM ET | UP 97% | 97¢ | skip | UP | Polymarket |
| Nov 20 11:40 PM ET | UP 64% | 46¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:35 PM ET | UP 62% | 83¢ | skip | UP | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
