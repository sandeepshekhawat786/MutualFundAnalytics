# Data Dictionary

## dim_fund

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | INTEGER | Unique AMFI Scheme Code |
| scheme_name | TEXT | Mutual Fund Scheme Name |
| fund_house | TEXT | AMC Name |
| category | TEXT | Fund Category |
| sub_category | TEXT | Fund Sub Category |
| plan | TEXT | Growth/Direct etc. |
| benchmark | TEXT | Benchmark Index |
| expense_ratio_pct | REAL | Expense Ratio |
| fund_manager | TEXT | Fund Manager |
| risk_category | TEXT | Risk Category |

---

## fact_nav

| Column | Type | Description |
|---------|------|-------------|
| amfi_code | INTEGER | Fund Code |
| full_date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

---

## fact_transactions

| Column | Type | Description |
|---------|------|-------------|
| investor_id | TEXT | Investor ID |
| transaction_date | DATE | Transaction Date |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction Amount |
| state | TEXT | Investor State |
| city | TEXT | Investor City |
| payment_mode | TEXT | Payment Method |
| kyc_status | TEXT | KYC Status |

---

## fact_performance

Contains annual returns, Sharpe Ratio, Alpha, Beta, Expense Ratio, Drawdown and Ratings.

---

## fact_aum

Stores Assets Under Management for fund houses.

Source:
- Bluestock Capstone Dataset
- MFAPI
- AMFI India