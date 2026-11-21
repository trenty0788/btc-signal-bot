# BTC 5-minute signal bot

Last update: **Nov 21 4:47 AM ET** (this job started Nov 21 3:15 AM ET)

## Latest call

**▼ BET DOWN** for the window 4:45 AM to 4:50 AM

Bot leans DOWN 67%, DOWN costs 56¢, edge +9¢ after fees.

Called at 4:47 AM. The result is known at 4:50 AM. Reload this page for the next call.

## Summary

- Windows logged: **482**
- Result confirmed by Polymarket: **481** (other windows use Coinbase's result until Polymarket's settles)
- Polymarket prices captured: **50 of the last 50** windows
- Bot's lean was right in **73%** of the last 100 windows
- Bot has learned from **2485** windows
- Settings: signal 2 min in, minimum edge 2¢, fee allowance 2¢

## Versus Polymarket prices

Replays logged windows with a minimum edge, after the fee allowance. A few hundred bets are needed before this means much.

**All windows with a price (482)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 482 | 78% | -0.3¢ |
| +0¢ | 169 | 68% | +2.6¢ |
| +2¢ | 135 | 64% | +2.5¢ |
| +4¢ | 111 | 63% | +3.1¢ |
| +6¢ | 88 | 60% | +3.8¢ |
| +8¢ | 68 | 56% | +3.6¢ |

**Only windows whose result Polymarket confirmed (481)**

| Min edge | Bets | Win rate | Avg per bet |
|---|---|---|---|
| Every call | 481 | 78% | -0.4¢ |
| +0¢ | 168 | 68% | +2.5¢ |
| +2¢ | 134 | 64% | +2.3¢ |
| +4¢ | 111 | 63% | +3.1¢ |
| +6¢ | 88 | 60% | +3.8¢ |
| +8¢ | 68 | 56% | +3.6¢ |

Unconfirmed close calls (Coinbase moved under $50) among bets at your minimum edge: **0**

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

Across 2485 windows the bot claimed 71% on average and was right 75%.

| Bot said | Windows | Avg said | Right |
|---|---|---|---|
| 50-55% | 350 | 52% | 58% |
| 55-60% | 337 | 57% | 65% |
| 60-65% | 301 | 62% | 67% |
| 65-70% | 309 | 68% | 73% |
| 70-80% | 513 | 75% | 77% |
| 80-90% | 410 | 85% | 89% |
| 90%+ | 265 | 94% | 94% |

## Recent windows

| Window | Bot | Price | Bet | Result | Source |
|---|---|---|---|---|---|
| Nov 21 4:40 AM ET | UP 77% | 71¢ | UP | UP ✓ | Coinbase |
| Nov 21 4:35 AM ET | DOWN 57% | 50¢ | DOWN | DOWN ✓ | Polymarket |
| Nov 21 4:30 AM ET | DOWN 74% | 72¢ | skip | DOWN | Polymarket |
| Nov 21 4:25 AM ET | UP 63% | 67¢ | skip | UP | Polymarket |
| Nov 21 4:20 AM ET | UP 95% | 95¢ | skip | UP | Polymarket |
| Nov 21 4:15 AM ET | UP 78% | 73¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 4:10 AM ET | UP 53% | 49¢ | UP | DOWN ✗ | Polymarket |
| Nov 21 3:55 AM ET | DOWN 81% | 92¢ | skip | DOWN | Polymarket |
| Nov 21 3:50 AM ET | UP 78% | 85¢ | skip | DOWN | Polymarket |
| Nov 21 3:45 AM ET | UP 60% | 73¢ | skip | UP | Polymarket |
| Nov 21 3:30 AM ET | DOWN 78% | 81¢ | skip | DOWN | Polymarket |
| Nov 21 3:25 AM ET | UP 59% | 74¢ | skip | UP | Polymarket |

Signals are advice only. No trades are placed. Not financial advice.
