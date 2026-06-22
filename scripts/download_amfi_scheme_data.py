import pandas as pd

url = "https://portal.amfiindia.com/DownloadSchemeData_Po.aspx?mf=0"

print("Downloading AMFI Scheme Data...")

df = pd.read_csv(url)

print("Download Successful!\n")

print("Shape :", df.shape)

print("\nColumns:")

print(df.columns)

df.to_csv("data/raw/amfi_scheme_data.csv", index=False)

print("\n✅ Saved as data/raw/amfi_scheme_data.csv")