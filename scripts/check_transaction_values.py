import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("=" * 60)
print("Unique Transaction Types")
print("=" * 60)

print(df["transaction_type"].unique())

print("\n")

print("=" * 60)
print("Unique KYC Status")
print("=" * 60)

print(df["kyc_status"].unique())

print("\n")

print("=" * 60)
print("Minimum Amount")
print("=" * 60)

print(df["amount_inr"].min())

print("\n")

print("=" * 60)
print("Maximum Amount")
print("=" * 60)

print(df["amount_inr"].max())