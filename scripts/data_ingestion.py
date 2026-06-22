import os
import pandas as pd

# Folder containing all raw datasets
DATA_FOLDER = "data/raw"

# Get all CSV files
csv_files = sorted([f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")])

print("=" * 100)
print(f"📂 Total CSV Files Found: {len(csv_files)}")
print("=" * 100)

for file in csv_files:

    file_path = os.path.join(DATA_FOLDER, file)

    print("\n" + "=" * 100)
    print(f"📄 Dataset : {file}")
    print("=" * 100)

    try:
        df = pd.read_csv(file_path)

        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        print("\nColumn Names")
        print(df.columns.tolist())

        print("\nData Types")
        print(df.dtypes)

        print("\nFirst 5 Records")
        print(df.head())

        print("\nMissing Values")
        print(df.isnull().sum())

        print("\nDuplicate Rows :", df.duplicated().sum())

        print("-" * 100)

    except Exception as e:

        print(f"❌ Error reading {file}")
        print(e)