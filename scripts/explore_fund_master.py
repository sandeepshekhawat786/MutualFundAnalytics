import pandas as pd

# Load Fund Master
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 80)
print("FUND MASTER OVERVIEW")
print("=" * 80)

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nFirst 5 Rows")
print(df.head())

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

# Show unique values for important columns (if present)
important_columns = [
    "fund_house",
    "category",
    "sub_category",
    "risk_category"
]

for column in important_columns:

    print("\n" + "=" * 60)
    print(f"Unique Values in {column}")
    print("=" * 60)

    print(df[column].unique())