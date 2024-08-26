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

