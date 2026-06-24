import sqlite3
import pandas as pd

print("=" * 60)
print("Loading Data into SQLite Database")
print("=" * 60)

conn = sqlite3.connect("bluestock_mf.db")

datasets = {
    "dim_fund": "data/raw/01_fund_master.csv",
    "fact_nav": "data/processed/02_nav_history.csv",
    "fact_aum": "data/raw/03_aum_by_fund_house.csv",
    "fact_performance": "data/processed/07_scheme_performance.csv",
    "fact_transactions": "data/processed/08_investor_transactions.csv"
}

for table, path in datasets.items():

    print(f"\nLoading {table}...")

    df = pd.read_csv(path)

    df.to_sql(
        table,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"{table} Loaded")
    print(f"Rows : {len(df)}")

conn.close()

print("\nDatabase Loaded Successfully!")