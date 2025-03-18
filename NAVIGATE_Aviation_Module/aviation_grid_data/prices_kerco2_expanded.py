# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 15:29:19 2025

@author: ucbvplu
"""

import pandas as pd

# Step 1: Define the range of years and the 28 alternative regions
years = list(range(2005, 2101))  # From 2005 to 2100
regions = [
    "AFE", "AFN", "AFW", "AFZ", "NIG", "RUS", "ASC", "ASE", "CHN", "IDN",
    "IND", "ASO", "JPN", "SKT", "ANZ", "USA", "CAN", "LAM", "BRA", "MEX",
    "CHL", "ENE", "ENW", "EUE", "EUW", "EUM", "MEA", "MDA", "UK"
]

# Step 2: Create a consistent index for each region
region_index_mapping = {region: index for index, region in enumerate(regions)}

# Step 3: Generate all combinations of Year and Region
expanded_data = []
for year in years:
    for region in regions:
        expanded_data.append([year, region, region_index_mapping[region]])

# Create a DataFrame
expanded_df = pd.DataFrame(expanded_data, columns=["Year", "Region", "RegionIndex"])

# Step 4: Load the original Prices_KerCO2.csv file
prices_kerco2_df = pd.read_csv("Prices_KerCO2.csv")

# Step 5: Define the OMNIA to Alternative Region mapping
region_mapping = {
    "AFR": ["AFE", "AFN", "AFW", "AFZ", "NIG"],
    "AUS": ["ANZ"],
    "CAN": ["CAN"],
    "CSA": ["LAM", "BRA", "MEX", "CHL"],
    "CHI": ["CHN"],
    "EEU": ["ENE", "ENW"],
    "FSU": ["RUS"],
    "IND": ["IND"],
    "JPN": ["JPN"],
    "MEX": ["MEX"],
    "MEA": ["MEA", "MDA"],
    "ODA": ["ASC","ASE", "ASO", "IDN"],
    "SKO": ["SKT"],
    "UK": ["UK"],
    "USA": ["USA"],
    "WEU": ["EUE", "EUW", "EUM"]
}

# Step 6: Create a dictionary for price lookups
prices_dict = {}
for _, row in prices_kerco2_df.iterrows():
    year = row["Year"]
    original_region = row["Region"]
    ker_price = row["KER_price ($/kg)"]
    co2_price = row["CO2_price ($/kgCO2)"]
    
    # Get mapped alternative regions
    mapped_regions = region_mapping.get(original_region, [original_region])
    
    for mapped_region in mapped_regions:
        prices_dict[(year, mapped_region)] = (ker_price, co2_price)

# Step 7: Assign the prices based on the mapping
expanded_df["KER_price ($/kg)"] = expanded_df.apply(
    lambda row: prices_dict.get((row["Year"], row["Region"]), (None, None))[0], axis=1)
expanded_df["CO2_price ($/kgCO2)"] = expanded_df.apply(
    lambda row: prices_dict.get((row["Year"], row["Region"]), (None, None))[1], axis=1)

# Step 8: Save the updated file
expanded_df.to_csv("Prices_KerCO2_2.csv", index=False)