import numpy as np
import pandas as pd
import scipy.stats as stats

# df = pd.read_csv("test.csv")
#
# # print(df[["name", "family"]])
# # print(df['average'])
# # print(df.iloc[2])
#
# print(df.iloc[[1, 3, 2]])
# print(df[["family", "name"]].iloc[[1,2]])

# person_list = [{"name":"a", "age":20},{"name":"b", "age":27}]
#
# df = pd.DataFrame(person_list)
# print(df.values)
# print(df.shape)
#
# x = np.array([1,2,1,4,1,2,2])
# print(x.mean())
# print(np.median(x))
# print(stats.mode(x))

import yfinance as yf
from matplotlib import pyplot as plt


btc = yf.download("BTC-USD")


# print(btc.head())
#
# X = np.arange(len(btc))
#
# plt.plot(X, btc["Close"], label= "Close Price ")
#
# mean = btc["Close"].mean()
# var = np.var(btc["Close"])
# std = np.std(btc["Close"])
#
# plt.plot([0,X.max()],[mean,mean], "g--",label = "Mean")
# plt.plot([0,X.max()],[mean+std ,mean+std], "r--",label = "Mean+std")
# plt.plot([0,X.max()],[mean-std ,mean-std], "r--",label = "Mean-std")
#
#
# plt.legend()
# plt.show()


print(btc.describe())