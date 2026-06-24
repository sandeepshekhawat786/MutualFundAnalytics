import pandas as pd
import os

print("=" * 70)
print("PROCESSING REMAINING DATASETS")
print("=" * 70)

raw_folder = "data/raw"
processed_folder = "data/processed"

os.makedirs(processed_folder, exist_ok=True)

# These datasets were already cleaned separately
already_processed = [
    "02_nav_history.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv"
]

files = [f for f in os.listdir(raw_folder) if f.endswith(".csv")]

for file in files:

    if file in already_processed:
        continue

    print(f"\nProcessing {file}")

    df = pd.read_csv(os.path.join(raw_folder, file))

    print(f"Original Shape : {df.shape}")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()

    df = df.drop_duplicates()

    print(f"Duplicates Removed : {duplicates}")

    # Display missing values
    missing = df.isnull().sum().sum()

    print(f"Missing Values : {missing}")

    # Save cleaned dataset
    output_path = os.path.join(processed_folder, file)

    df.to_csv(output_path, index=False)

    print("Saved Successfully")

print("\n" + "=" * 70)
print("ALL REMAINING DATASETS PROCESSED")
print("=" * 70)