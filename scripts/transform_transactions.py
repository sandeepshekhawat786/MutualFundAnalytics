import pandas as pd
import os

print("=" * 60)
print("Loading Investor Transactions...")
print("=" * 60)

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print(f"Original Shape : {df.shape}")

# =====================================
# Convert Date
# =====================================

print("\nConverting transaction_date to datetime...")

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# =====================================
# Standardize Transaction Types
# =====================================

print("Standardizing transaction types...")

df["transaction_type"] = (
    df["transaction_type"]
      .str.strip()
      .str.title()
)

# =====================================
# Validate Amount
# =====================================

invalid_amount = df[df["amount_inr"] <= 0]

print(f"Invalid Amount Records : {len(invalid_amount)}")

# =====================================
# Validate KYC Status
# =====================================

valid_kyc = ["Verified", "Pending"]

invalid_kyc = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print(f"Invalid KYC Records : {len(invalid_kyc)}")

# =====================================
# Remove Duplicates
# =====================================

duplicates = df.duplicated().sum()

df = df.drop_duplicates()

print(f"Duplicates Removed : {duplicates}")

# =====================================
# Save
# =====================================

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/08_investor_transactions.csv",
    index=False
)

print("\nDataset saved successfully!")

print(f"Final Shape : {df.shape}")

print("=" * 60)
print("Transaction Cleaning Completed")
print("=" * 60)