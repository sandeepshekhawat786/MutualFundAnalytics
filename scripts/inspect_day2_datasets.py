import pandas as pd

datasets = [
    "02_nav_history.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv"
]

for file in datasets:

    print("=" * 100)
    print(file)
    print("=" * 100)

    df = pd.read_csv(f"data/raw/{file}")

    print("\nShape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst 5 Rows")
    print(df.head())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\n")