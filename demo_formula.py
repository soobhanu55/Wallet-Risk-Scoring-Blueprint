"""Illustrates the real heuristic scoring formula on small synthetic
wallet data. NOT live on-chain data -- The Graph's hosted service this
notebook depends on was fully shut down June 12, 2024 (see README), so
there is no live data source to demo against anymore. This is the real
formula from the notebook, run on hand-built example numbers, clearly
labeled as synthetic rather than presented as if it were a live run.
"""

wallets = [
    {"id": "0xAAA...111", "borrow": 500, "utilization": 0.2, "interest": 10},
    {"id": "0xBBB...222", "borrow": 8000, "utilization": 0.9, "interest": 400},
    {"id": "0xCCC...333", "borrow": 0, "utilization": 0.05, "interest": 0},
]


def normalize(values):
    lo, hi = min(values), max(values)
    return [(v - lo) / (hi - lo + 1e-9) for v in values]


def main():
    print("=== WalletGuard: heuristic formula on synthetic example wallets ===")
    print("(SYNTHETIC data -- the real on-chain API this depends on has been dead since June 2024)")
    print()

    borrows = normalize([w["borrow"] for w in wallets])
    utils = normalize([w["utilization"] for w in wallets])
    interests = normalize([w["interest"] for w in wallets])

    raw_scores = [
        0.3 * b + 0.4 * u + 0.3 * i
        for b, u, i in zip(borrows, utils, interests)
    ]
    lo, hi = min(raw_scores), max(raw_scores)
    scaled = [(s - lo) / (hi - lo + 1e-9) * 1000 for s in raw_scores]

    print(f"{'Wallet':16s} {'Borrow':>8s} {'Util':>6s} {'Interest':>9s}  {'Score (0-1000)'}")
    for w, score in zip(wallets, scaled):
        print(f"{w['id']:16s} {w['borrow']:8.0f} {w['utilization']:6.2f} {w['interest']:9.0f}  {score:7.1f}")

    print()
    print("Higher borrow/utilization/interest -> higher (riskier) score by this")
    print("heuristic's own definition -- not validated against real default outcomes.")


if __name__ == "__main__":
    main()
