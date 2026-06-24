import sqlite3

print("=" * 60)
print("Creating Database using schema.sql")
print("=" * 60)

# Connect to SQLite
conn = sqlite3.connect("bluestock_mf.db")

cursor = conn.cursor()

# Read schema.sql
with open("sql/schema.sql", "r") as file:
    schema = file.read()

# Execute all CREATE TABLE statements
cursor.executescript(schema)

conn.commit()

print("Database Created Successfully!")

conn.close()