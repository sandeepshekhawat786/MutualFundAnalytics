import pandas as pd
import os

print("=" * 60)
print("Loading Scheme Performance Dataset...")
print("=" * 60)

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print(f"Original Shape : {df.shape}")

# =====================================
# Columns to Validate
# =====================================

numeric_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

print("\nChecking numeric columns...")

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# =====================================
# Check Missing Values
# =====================================

missing = df[numeric_columns].isnull().sum().sum()

print(f"Missing Numeric Values : {missing}")

# =====================================
# Expense Ratio Validation
# =====================================

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print(f"Expense Ratio Anomalies : {len(invalid_expense)}")

# =====================================
# Return Anomaly Check
# =====================================

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

print("\nChecking Return Value Anomalies...")

for col in return_columns:

    anomalies = df[
        (df[col] < -100) |
        (df[col] > 200)
    ]

    print(f"{col}: {len(anomalies)} anomalies")

# =====================================
# Remove Duplicates
# =====================================

duplicates = df.duplicated().sum()

df = df.drop_duplicates()

print(f"\nDuplicates Removed : {duplicates}")

# =====================================
# Save
# =====================================

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/07_scheme_performance.csv",
    index=False
)

print("\nDataset saved successfully!")

print(f"Final Shape : {df.shape}")

print("=" * 60)
print("Scheme Performance Cleaning Completed")
print("=" * 60)