import pandas as pd
from sqlalchemy import create_engine

print("=" * 60)
print("Creating SQLite Database...")
print("=" * 60)

# ==========================================
# Create Database Connection
# ==========================================

engine = create_engine("sqlite:///bluestock_mf.db")

print("Database Connected Successfully!")

# ==========================================
# Load Cleaned CSV Files
# ==========================================

datasets = {

    "dim_fund":
        "data/raw/01_fund_master.csv",

    "fact_nav":
        "data/processed/02_nav_history.csv",

    "fact_aum":
        "data/raw/03_aum_by_fund_house.csv",

    "fact_performance":
        "data/processed/07_scheme_performance.csv",

    "fact_transactions":
        "data/processed/08_investor_transactions.csv"

}

# ==========================================
# Load Tables
# ==========================================

for table_name, file_path in datasets.items():

    print(f"\nLoading {table_name}...")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} Loaded Successfully!")

    print(f"Rows Loaded : {len(df)}")

print("\n" + "=" * 60)
print("SQLite Database Created Successfully!")
print("=" * 60)