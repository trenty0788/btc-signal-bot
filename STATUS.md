# BTC 5-minute signal bot

Last update: **Nov 21 4:57 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**SKIP** for the window 4:55 AM to 5:00 AM

Bot leans UP 67%, UP costs 77¢, edge -12¢ after fees.

Called at 4:57 AM. The result is known at 5:00 AM. Reload this page for the next call.

## Summary

- Windows logged: **484**
- Result confirmed by Polymarket: **483** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **72%** of the last 100 windows
- Bot has learned from **2487** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (484)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 484 | 78% | -0.4¢ |
| +0¢ | 171 | 68% | +2.4¢ |
| +2¢ | 137 | 64% | +2.2¢ |
| +4¢ | 113 | 63% | +2.8¢ |
| +6¢ | 89 | 61% | +4.2¢ |
| +8¢ | 69 | 57% | +4.1¢ |

**Only windows whose result Polymarket confirmed (483)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 483 | 78% | -0.3¢ |
| +0¢ | 170 | 68% | +2.9¢ |
| +2¢ | 136 | 65% | +2.8¢ |
| +4¢ | 112 | 63% | +3.5¢ |
| +6¢ | 89 | 61% | +4.2¢ |
| +8¢ | 69 | 57% | +4.1¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **1**

## Limit order test

What if a skipped call had been turned into a limit buy on the bot's lean, placed at its fair price minus a margin? The bot checks Polymarket's price every 20 seconds and counts an order as filled if the lowest ask reached your price. That flatters the result, since a real order can sit unfilled even when the price touches it. Skipped windows tracked: **46**.

| Limit price | Windows | Filled | Fill rate | Won when filled | Avg per fill | Avg per window |
|---|---|---|---|---|---|---|
| Fair | 46 | 24 | 52% | 71% | -10.6¢ | -5.5¢ |
| Fair −2¢ | 46 | 19 | 41% | 63% | -13.8¢ | -5.7¢ |
| Fair −4¢ | 46 | 15 | 33% | 53% | -19.6¢ | -6.4¢ |
| Fair −6¢ | 46 | 14 | 30% | 50% | -21.0¢ | -6.4¢ |
| Fair −8¢ | 46 | 13 | 28% | 46% | -21.4¢ | -6.0¢ |

If "Won when filled" sits below the price you paid, the fills are catching windows that moved against you.

## Calibration

Across 2487 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 350 | 52% | 58% |
| 55-60% | 337 | 57% | 65% |
| 60-65% | 301 | 62% | 67% |
| 65-70% | 310 | 68% | 73% |
| 70-80% | 514 | 75% | 77% |
| 80-90% | 410 | 85% | 89% |
| 90%+ | 265 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 4:50 AM ET | DOWN 78% | 71¢ | DOWN | UP ✗ | Coinbase (close) |
| Nov 21 4:45 AM ET | DOWN 67% | 56¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 21 4:40 AM ET | UP 77% | 71¢ | UP | UP ✓ | Polymarket |
| Nov 21 4:35 AM ET | DOWN 57% | 50¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 21 4:30 AM ET | DOWN 74% | 72¢ | skip | DOWN | Polymarket |
| Nov 21 4:25 AM ET | UP 63% | 67¢ | skip | UP | Polymarket |
| Nov 21 4:20 AM ET | UP 95% | 95¢ | skip | UP | Polymarket |
| Nov 21 4:15 AM ET | UP 78% | 73¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 4:10 AM ET | UP 53% | 49¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 3:55 AM ET | DOWN 81% | 92¢ | skip | DOWN | Polymarket |
| Nov 21 3:50 AM ET | UP 78% | 85¢ | skip | DOWN | Polymarket |
| Nov 21 3:45 AM ET | UP 60% | 73¢ | skip | UP | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
