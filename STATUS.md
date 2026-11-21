# BTC 5-minute signal bot

Last update: **Nov 21 7:02 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 7:00 AM to 7:05 AM

Bot leans DOWN 67%, DOWN costs 77¢, edge -12¢ after fees.

Called at 7:02 AM. The result is known at 7:05 AM. Reload this page for the next call.

## Summary

- Windows logged: **509**
- Result confirmed by Polymarket: **508** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **75%** of the last 100 windows
- Bot has learned from **2512** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (509)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 509 | 78% | -0.5¢ |
| +0¢ | 178 | 67% | +2.0¢ |
| +2¢ | 142 | 64% | +2.0¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

**Only windows whose result Polymarket confirmed (508)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 508 | 78% | -0.5¢ |
| +0¢ | 178 | 67% | +2.0¢ |
| +2¢ | 142 | 64% | +2.0¢ |
| +4¢ | 117 | 62% | +2.4¢ |
| +6¢ | 93 | 60% | +3.6¢ |
| +8¢ | 72 | 57% | +4.2¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **66**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 66 | 38 | 58% | 71% | -7.1¢ | -4.1¢ |
| Fair −2¢ | 66 | 28 | 42% | 61% | -12.6¢ | -5.4¢ |
| Fair −4¢ | 66 | 24 | 36% | 54% | -15.4¢ | -5.6¢ |
| Fair −6¢ | 66 | 23 | 35% | 52% | -15.2¢ | -5.3¢ |
| Fair −8¢ | 66 | 22 | 33% | 50% | -14.4¢ | -4.8¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2512 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 353 | 52% | 58% |
| 55-60% | 339 | 57% | 64% |
| 60-65% | 306 | 62% | 67% |
| 65-70% | 313 | 68% | 73% |
| 70-80% | 518 | 75% | 77% |
| 80-90% | 414 | 85% | 89% |
| 90%+ | 269 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 6:55 AM ET | UP 64% | 83¢ | skip | UP | Coinbase |
| Nov 21 6:50 AM ET | UP 61% | 58¢ | skip | DOWN | Polymarket |
| Nov 21 6:45 AM ET | UP 54% | 64¢ | skip | UP | Polymarket |
| Nov 21 6:40 AM ET | UP 52% | 65¢ | skip | DOWN | Polymarket |
| Nov 21 6:35 AM ET | DOWN 84% | 95¢ | skip | DOWN | Polymarket |
| Nov 21 6:30 AM ET | UP 100% | 98¢ | skip | UP | Polymarket |
| Nov 21 6:25 AM ET | UP 51% | 59¢ | skip | UP | Polymarket |
| Nov 21 6:20 AM ET | UP 69% | 82¢ | skip | UP | Polymarket |
| Nov 21 6:15 AM ET | DOWN 98% | 96¢ | skip | DOWN | Polymarket |
| Nov 21 6:10 AM ET | UP 62% | 80¢ | skip | DOWN | Polymarket |
| Nov 21 6:05 AM ET | DOWN 58% | 42¢ | DOWN | UP ✗ | Polymarket |
| Nov 21 6:00 AM ET | DOWN 82% | 84¢ | skip | DOWN | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
