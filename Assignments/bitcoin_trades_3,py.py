import yfinance as yf
import pandas as pd

# Download the data
data = yf.download("BTC-USD", start="2019-01-05", end="2024-08-01")
data.index = pd.to_datetime(data.index)

# Identify Saturdays and Wednesdays
is_saturday = data.index.to_series().dt.dayofweek == 5
is_wednesday = data.index.to_series().dt.dayofweek == 2

# Filter the data for Saturdays and Wednesdays
saturdays = data[is_saturday]
wednesdays = data[is_wednesday]

# Print some rows to verify
print("Filtered Saturdays DataFrame (first few rows):")
print(saturdays[['Open']].tail())

print("Filtered Wednesdays DataFrame (first few rows):")
print(wednesdays[['Close']].tail())

# Prepare DataFrames for merging
saturdays = saturdays[['Open']].rename(columns={'Open': 'Saturday_Open'})
wednesdays = wednesdays[['Close']].rename(columns={'Close': 'Wednesday_Close'})

# Merge the data on the index (date)
trades = pd.merge(saturdays, wednesdays, left_index=True, right_index=True, how='inner')

# Display the resulting trades DataFrame
print("Trades DataFrame:")
print(trades.head())