# WalletGuard

A data pipeline that queries live Compound V2 lending data per wallet address via The Graph's GraphQL API, then computes a heuristic risk score from three normalized features.

## What this actually is

- Reads a list of wallet addresses from a CSV.
- Queries The Graph's Compound V2 subgraph for each wallet's token balances, borrow amounts, and interest.
- Computes `score = 0.3 * normalized_borrow + 0.4 * normalized_utilization + 0.3 * normalized_interest`, scaled to 0-1000.
- Exports the scored wallets to `wallet_risk_scores.csv`.

## Honest scope — no evaluation metric, and here's why

This is a hand-weighted heuristic formula, not a trained or validated model. There is no ground truth for "wallet risk" here (no labeled set of wallets that actually defaulted or didn't), so there is nothing to measure precision/recall/accuracy against, and no evaluation metric is reported because none can be honestly computed. The 0.3/0.4/0.3 weighting is a reasonable-looking guess, not a fitted or backtested parameter.

Two other real limitations, stated plainly:
- The notebook uses Google Colab-specific interactive widgets (`google.colab.files.upload()` / `.download()`), so it does not run as-is outside Colab.
- The Graph's hosted service (`api.thegraph.com`, the endpoint this notebook queries) was fully shut down on June 12, 2024 — confirmed via [The Graph's own announcement](https://thegraph.com/blog/sunsetting-hosted-service/). The query in this notebook no longer works at all without migrating to The Graph's paid decentralized network.

This is what it is: a working data-pipeline sketch for a heuristic scoring idea, not a validated credit-risk model.
