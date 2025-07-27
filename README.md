# 🔐 Wallet Risk Scoring Using Compound V2

This project assigns risk scores (0–1000) to 100 wallets based on their borrowing behavior on the Compound V2 protocol using on-chain data.

---

## ✅ Objective

- Fetch on-chain supply/borrow data for each wallet
- Extract features: borrow volume, utilization ratio, interest accrued
- Normalize data and assign a risk score (0 = low risk, 1000 = high risk)
- Export results as a CSV: `wallet_id, score`

---

## 📊 Features Used

| Feature | Description |
|--------|-------------|
| **Borrow Volume** | Total assets borrowed |
| **Utilization Ratio** | Borrow / Supply |
| **Interest Accrued** | Proxy for borrowing intensity & risk |

---

## 🧮 Scoring Formula

risk_score = (0.3 × borrow + 0.4 × utilization + 0.3 × interest) → scaled to 0–1000


