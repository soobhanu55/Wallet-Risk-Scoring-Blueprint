# Wallet-Risk-Scoring-Blueprint

1. Data Collection:
   Used The Graph’s Compound V2 subgraph to query wallet-level account summaries.

2. Feature Selection:
   a) borrowBalanceUnderlying: measures exposure.
   b) utilization: calculated as borrow/supply, indicates liquidation risk.
   c) interestAccrued: a proxy for exposure duration and cost.

3. Normalization:
   Min-max normalization used for fair comparison.

Scoring:
Final score = Weighted sum of normalized features, scaled to a 0–1000 range:
       Borrow (30%), Utilization (40%), Interest (30%).
