import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

cursor = conn.cursor()

tables = [
    "dim_fund",
    "fact_nav",
    "fact_aum",
    "fact_performance",
    "fact_transactions"
]

print("=" * 50)
print("DATABASE ROW COUNT")
print("=" * 50)

for table in tables:

    cursor.execute(f"SELECT COUNT(*) FROM {table}")

    count = cursor.fetchone()[0]

    print(f"{table:<25} {count}")

conn.close()