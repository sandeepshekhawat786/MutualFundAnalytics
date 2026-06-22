import requests
import pandas as pd
import os



# Mutual Fund Scheme Codes
schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Download data for each scheme
for fund_name, scheme_code in schemes.items():

    print(f"Downloading {fund_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        history = pd.DataFrame(data["data"])

        history.to_csv(
            f"data/raw/{fund_name}.csv",
            index=False
        )

        print(f"✅ Saved {fund_name}.csv")

    else:

        print(f"❌ Failed to fetch {fund_name}")

print("\n🎉 All Mutual Fund data downloaded successfully!")