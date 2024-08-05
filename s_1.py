# مراحل تحلیل داده

# 1.Data extraction  2.Data cleaning 3.Data normalization(scaling) 4.analysis 5.feature extraction 6.process with AI model  & visualization in all stages

# students = [
#     ["ali" , 12, 15]
#     ["reza"]
#     ["mohsen"]
# ]

# what we defined above is not an array and is just a python list because the numbers of columns doesnt match with each other


import pandas as pd
import matplotlib
# pd.read_csv()
# pd.read_excel()
# pd.read_json()
# pd.read_clipboard()
# pd.read_html()

data = pd.read_csv("pokemon_data.csv")

# import yfinance as yf
#
# BTC = yf.download(tickers:"BTC-USD", start="2024-07-1", interval="30m")

print(data.head())
print(data["Type 1"])
data_file= data["Speed"]
plt.plot(data_file)

# plt.legand()
# plt.show()