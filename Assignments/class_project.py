import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the tickers
tickers = ['CL=F', 'DX-Y.NYB', 'BTC-USD', 'GC=F']

# Download data
data = yf.download(tickers, start='2014-09-09', end='2024-09-09')

# Normalize prices based on the price of the Dollar (DX-Y.NYB)
normalized_data = data.copy()
for column in ['CL=F', 'BTC-USD', 'GC=F']:
    normalized_data[column] = data[column]['Close'] / data['DX-Y.NYB']['Close']

# Plot the normalized prices
plt.figure(figsize=(14, 7))
plt.plot(normalized_data.index, normalized_data['CL=F'], label='Oil')
plt.plot(normalized_data.index, normalized_data['BTC-USD'], label='Bitcoin')
plt.plot(normalized_data.index, normalized_data['GC=F'], label='Gold')

plt.title('Normalized Prices of Oil, Bitcoin, and Gold Based on the US Dollar')
plt.xlabel('Date')
plt.ylabel('Normalized Price')
plt.legend()
plt.grid(True)
plt.show()