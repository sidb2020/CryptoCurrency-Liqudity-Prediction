# -*- coding: utf-8 -*-
"""Feature Engineering ML Project Sid.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1upjA-7BrBhrT1S0EBv3dCU8QbJR05JsK
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

# Mount path
input_path = "/content/drive/MyDrive/PW Assignments/merged_cleaned_crypto_data.csv"
output_path = "/content/drive/MyDrive/PW Assignments/engineered_crypto_data.csv"

# Load the dataset
df = pd.read_csv(input_path)

# Strip column names (remove leading/trailing spaces)
df.columns = df.columns.str.strip()

# Show the columns
print("Available columns:\n", df.columns.tolist())

# Rename columns to match standard names
df = df.rename(columns={
    'price': 'current_price',
    '24h_volume': 'total_volume',
    'mkt_cap': 'market_cap',
    '24h': 'price_change_percentage_24h'
})

# Feature Engineering

# 1. Liquidity Ratio
df['liquidity_ratio'] = df['total_volume'] / df['market_cap']

# 2. Volatility Range — not available → skipping
df['volatility_range'] = 0  # Placeholder since high/low prices not available

# 3. Price Change Ratio
df['price_change_ratio'] = df['price_change_percentage_24h'] / df['current_price']

# 4. Cap per Supply — 'circulating_supply' not available → skipping
df['cap_per_supply'] = 0  # Placeholder if missing

# 5. Liquidity Level (target)
df['liquidity_level'] = pd.qcut(df['liquidity_ratio'], q=3, labels=['Low', 'Medium', 'High'])

# Final cleanup
df = df.replace([float("inf"), -float("inf")], pd.NA).dropna().reset_index(drop=True)

# Save
df.to_csv(output_path, index=False)

# Summary
print("Feature engineering complete.")
print("Saved to:", output_path)
print("Shape:", df.shape)
print("Liquidity level distribution:\n", df['liquidity_level'].value_counts())