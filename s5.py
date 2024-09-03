import re

import matplotlib.pyplot as plt
# import pandas as pd
# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(response)
#
#
# data = response.json()
#
# for d in data:
#     print(d["userId"], d["title"])
#
# data = pd.read_json(response.json())

import yfinance as yf
import plotly.graph_objs as go
import streamlit as st
# btc = yf.download("BTC-USD")

# go.Figure(data=[go.Candlestick(
#     x = btc,
#     open = btc.Open,
#     close = btc.Close,
#     high = btc.High,
#     low = btc.Low,
# )])
#
#
# st.plotly_chart(btc, use_container_width=True)

import numpy as np
import yfinance as yf

# feature1 =[1,2,3,4,5]
# feature2 = [1,2,3,4,5]
# feature3 = [5,4,3,2,1]
# feature4= [100, -1, 2000, -178]
# print(np.cov(feature1, feature3))

# btc = yf.download("BTC-USD")
# print(btc.corr())

from sklearn.datasets import load_diabetes
import seaborn as sns

# X,y = load_diabetes(as_frame=True, return_X_y=True)
# X["diabetes"] = y
# print(X.columns)
# print(X.corr())
#
# sns.heatmap(X.corr() , cmap="coolwarm", annot=True, fmt=".4f")
# plt.show()


from sklearn.preprocessing import StandardScaler,MinMaxScaler,LabelEncoder
from matplotlib import pyplot as plt
import yfinance as yf

# btc = yf.download('BTC-USD', start='2021-01-01')
# eth = yf.download('ETH-USD', start='2021-01-01')
#
# btc_close = btc["Close"].values.reshape(-1, 1)
# eth_close = eth["Close"].values.reshape(-1, 1)
#
# #(x- mean ) / std   mean = 0 , std = 1
#
# # scaler = StandardScaler()
# scaler = MinMaxScaler(feature_range=(0,50))
#
# btc_close = scaler.fit_transform(btc_close)
# eth_close = scaler.fit_transform(eth_close)
#
#
# plt.plot(btc_close)
# plt.plot(eth_close)
# plt.show()

# result = ["bimar", "salem", "mashkook", "salem", "salem", "bimar", "bimar", "bimar", "mashkook"]
# encoder = LabelEncoder()
# encoder.fit(result)
#
# t_result = encoder.transform(result)
#
# print(t_result)
# encoder.inverse_transform([2])

import pandas as pd

# X1 = [{"id":1, "name":"ali", "age":20}, {"id":2, "name":"reza", 'age':17},{"id":3, "name":'mohsen', "age":22}]
# X2 = [{"id":1, "name":'ali', "age":20}, {"id":10, "name":"ahmad", "age":25}]
#
# df1 = pd.DataFrame(X1)
# df2 = pd.DataFrame(X2)
#
# new_df = pd.concat([df1, df2], axis = 1)
# new_df.columns = list("abcdef")
#
# new_df.reset_index(inplace = True)
# print(new_df.drop(columns=['index']))



# X1 = [{"id":1, "name":"ali", "age":20}, {"id":2, "name":"reza", 'age':17},{"id":3, "name":'mohsen', "age":22}]
# X2 = [{"id":1, "math": 18, "art": 18}, {"id": 3, "math": 18, "art": 18}, {"id": 4, "math": 18, "art": 18}]
#
# df1 = pd.DataFrame(X1)
# df2 = pd.DataFrame(X2)
#
# # left brings all of the data in the first data, and right does the same for the second one
# new_df = pd.merge(df1, df2, on = "id", how = "inner")
# # new_df = pd.merge(df1, df2, on = "id", how = "outer")
# # new_df = pd.merge(df1, df2, on = "id", how = "left")
# # new_df = pd.merge(df1, df2, on = "id", how = "right")
# # new_df = pd.merge(df1, df2, on = "id", how = "cross")
#
# new_df.reset_index(inplace=True)
# print(new_df.drop(columns=['index']))

# X = [{"id":1, "name":"ali", "age":20}, {"id":2, "name":"reza", 'age':17},{"id":3, "name":'mohsen', "age":22}]
# df = pd.DataFrame(X)
#
# df["name"].str.replace(",","")
# df["Data"].dt.

# btc = yf.download("BTC-USD", start = "2021-01-01")
# btc["Date"] = btc.index
#
# print(btc["Date"].dt.weekday)

# y = np.array([1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,1])
y = np.random.randint(1, 10, 1000)

X = np.arange(len(y))
# kernel = [4, 5, 4]
kernel = np.random.randint(1,10,10)

kernel_size = len(kernel)
rate = 0.7

plt.plot(X, y)

for i in range(0, len(y) - kernel_size):
    print(y[i:i + kernel_size] - kernel)
    sa = np.sum(np.abs(y[i:i + kernel_size] - kernel))
    ss = np.sum(np.power(y[i:i + kernel_size] - kernel, 2))
    similarity = np.sum(kernel) - sa
    if similarity > np.sum(kernel) * rate:
        plt.plot(X[i:i+kernel_size], kernel, "r--")

plt.show()

