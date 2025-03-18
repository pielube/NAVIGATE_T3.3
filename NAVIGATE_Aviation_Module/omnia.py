# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 16:35:41 2025

@author: ucbvplu
"""

import pandas as pd
import matplotlib.pyplot as plt

# Define the list of years to filter
years_omnia = [2019, 2023, 2025, 2030, 2035, 2040, 2045, 2050, 2060, 2070, 2080, 2090, 2100]

# Load the CSV file into a pandas DataFrame
file_path = "./output_byregion_SSP2_t2_1.csv"
df = pd.read_csv(file_path)

# Extract the required columns and filter by the specified years
filtered_df = df[df['Year'].isin(years_omnia)][['Year', 'Region', 'Domestic_RPK', 'International_RPK']]

# Set 'Year' and 'Region' as the index
filtered_df.set_index(['Year', 'Region'], inplace=True)

plot_df = filtered_df.reset_index()

# Create the plot
plt.figure(figsize=(12, 6))
for region in plot_df['Region'].unique():
    subset = plot_df[plot_df['Region'] == region]
    plt.plot(subset['Year'], subset['International_RPK'], label=region)

# Customize the plot
plt.xlabel('Year')
plt.ylabel('Domestic RPK')
plt.title('Domestic RPK Over Time by Region')
plt.legend(title="Region", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

# Show the plot
plt.show()
