import requests
import pandas as pd

def get_senator(address):
    url = "https://geocoding.geo.census.gov/geocoder/geographies/address"
    params = {
        #"street": address,
        "city": "Paia",
        "state": "HI",
        "zip": "96779",
        "benchmark": "4",
        "vintage" : "422",
        "format": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        upper = data["result"]["addressMatches"][0]["geographies"]["2022 State Legislative Districts - Upper"][0]["NAME"]
        lower = data["result"]["addressMatches"][0]["geographies"]["2022 State Legislative Districts - Lower"][0]["NAME"]
        #'2022 State Legislative Districts - Lower': [{'GEOID': '15013', 'CENTLAT': '+20.8951431', 'SLDL': '013', 'AREAWATER': 2737860658, 'STATE': '15', 'BASENAME': '13', 'OID': '2135231807733831', 'LSADC': 'LL', 'FUNCSTAT': 'N', ...}]
        return {
            "senate" : upper,
            "house" : lower
        }
    except (KeyError, IndexError):
        return "Unable to determine the State Senator for the given address."


def update() :
    # Read the CSV file
    df = pd.read_csv('input.csv')

    # Iterate over each address column
    for column in df.columns:
        if 'address' in column.lower():
            # Update the new column with the address values
            df['new_column'] = df[column]

    # Save the updated DataFrame to a new CSV file
    df.to_csv('output.csv', index=False)


address = "22 Hoku Place"
result = get_senator(address)
print(f"The Hawaii State Senator for {address} is {senator}.")


