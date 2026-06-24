import pandas as pd
import os

# ==========================
# Load Dataset
# ==========================

print("=" * 60)
print("Loading NAV History Dataset...")
print("=" * 60)

df = pd.read_csv("data/raw/02_nav_history.csv")

print(f"Original Shape : {df.shape}")

# ==========================
# Convert Date
# ==========================

print("\nConverting date column to datetime...")

df["date"] = pd.to_datetime(df["date"])

# ==========================
# Sort Data
# ==========================

print("Sorting by AMFI Code and Date...")

df = df.sort_values(
    by=["amfi_code", "date"]
)

# ==========================
# Remove Duplicates
# ==========================

duplicates_before = df.duplicated().sum()

df = df.drop_duplicates()

duplicates_after = df.duplicated().sum()

print(f"Duplicates Removed : {duplicates_before}")

# ==========================
# Forward Fill Missing NAV
# ==========================

missing_before = df["nav"].isnull().sum()

df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

missing_after = df["nav"].isnull().sum()

print(f"Missing NAV Before : {missing_before}")
print(f"Missing NAV After  : {missing_after}")

# ==========================
# Validate NAV
# ==========================

invalid_nav = df[df["nav"] <= 0]

print(f"Invalid NAV Records : {len(invalid_nav)}")

# ==========================
# Save Clean Dataset
# ==========================

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/02_nav_history.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")

print(f"Final Shape : {df.shape}")

print("=" * 60)
print("NAV Cleaning Completed")
print("=" * 60)