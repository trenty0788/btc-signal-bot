# BTC 5-minute signal bot

Last update: **Nov 21 12:27 AM ET** (this job started Nov 20 9:40 PM ET)

## Latest call

**SKIP** for the window 12:25 AM to 12:30 AM

Bot leans UP 53%, UP costs 67¢, edge -16¢ after fees.

Called at 12:27 AM. The result is known at 12:30 AM. Reload this page for the next call.

## Summary

- Windows logged: **450**
- Result confirmed by Polymarket: **449** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **81%** of the last 100 windows
- Bot has learned from **2453** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (450)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 450 | 78% | -0.1¢ |
| +0¢ | 154 | 70% | +4.8¢ |
| +2¢ | 124 | 66% | +4.2¢ |
| +4¢ | 104 | 63% | +3.7¢ |
| +6¢ | 82 | 61% | +5.1¢ |
| +8¢ | 62 | 56% | +5.2¢ |

**Only windows whose result Polymarket confirmed (449)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 449 | 78% | -0.3¢ |
| +0¢ | 153 | 70% | +4.3¢ |
| +2¢ | 123 | 66% | +3.6¢ |
| +4¢ | 103 | 63% | +3.0¢ |
| +6¢ | 81 | 60% | +4.2¢ |
| +8¢ | 61 | 56% | +4.1¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **1**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **25**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 25 | 13 | 52% | 69% | -11.6¢ | -6.0¢ |
| Fair −2¢ | 25 | 11 | 44% | 64% | -11.8¢ | -5.2¢ |
| Fair −4¢ | 25 | 9 | 36% | 56% | -14.3¢ | -5.2¢ |
| Fair −6¢ | 25 | 9 | 36% | 56% | -12.3¢ | -4.4¢ |
| Fair −8¢ | 25 | 9 | 36% | 56% | -10.3¢ | -3.7¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2453 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 345 | 52% | 58% |
| 55-60% | 335 | 57% | 64% |
| 60-65% | 295 | 62% | 67% |
| 65-70% | 308 | 68% | 73% |
| 70-80% | 508 | 75% | 77% |
| 80-90% | 405 | 85% | 89% |
| 90%+ | 257 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 12:20 AM ET | UP 65% | 22¢ | UP | UP ✓ | Coinbase (close) |
| Nov 21 12:15 AM ET | UP 77% | 80¢ | skip | UP | Polymarket |
| Nov 21 12:10 AM ET | UP 75% | 78¢ | skip | DOWN | Polymarket |
| Nov 21 12:05 AM ET | DOWN 78% | 85¢ | skip | DOWN | Polymarket |
| Nov 21 12:00 AM ET | UP 89% | 95¢ | skip | UP | Polymarket |
| Nov 20 11:55 PM ET | DOWN 65% | 83¢ | skip | DOWN | Polymarket |
| Nov 20 11:50 PM ET | UP 86% | 93¢ | skip | UP | Polymarket |
| Nov 20 11:45 PM ET | UP 97% | 97¢ | skip | UP | Polymarket |
| Nov 20 11:40 PM ET | UP 64% | 46¢ | UP | DOWN ✗ | Polymarket |
| Nov 20 11:35 PM ET | UP 62% | 83¢ | skip | UP | Polymarket |
| Nov 20 11:30 PM ET | UP 80% | 86¢ | skip | UP | Polymarket |
| Nov 20 11:25 PM ET | UP 50% | 39¢ | UP | DOWN ✗ | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
