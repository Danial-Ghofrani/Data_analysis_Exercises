import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from sympy import diff, symbols
import seaborn as sns

df = yf.download("BTC-USD")

# sns.heatmap(df.corr(), annot = True, fmt = "0.6f")
# sns.pairplot(df, hue="Close")
# plt.show()

# learning_rate = 0.001
#
# x = np.array([100, 110, 190, 200, 220, 300, 320, 350, 400, 420]).reshape(-1, 1)
# y = np.array([80, 100, 160, 170, 250, 265, 330, 340, 370, 400]).reshape(-1,1)

# theta = np.array([[0,0]])
# bias_x = np.c_[np.ones_like(x).reshape(-1,1),x]
#
# for epochs in range(1000):
#
#     h = x.dot(theta)
#     error = h - y
#
#     gradient = x.T.dot(error) / len(x)
#     theta = theta - learning_rate * gradient
#
#
#
# plt.scatter(x, y)
# plt.plot(x, h)
# plt.show()



# x = np.array([100, 110, 190, 200, 220, 300, 320, 350, 400, 420])
# y = np.array([80, 100, 160, 170, 250, 265, 330, 340, 370, 400])
#
# model = np.poly1d(np.polyfit(x,y, 1))
#
# h = model(x)
#
# print(model(270))
#
# plt.scatter(x,y)
# plt.plot(x,h)
# plt.show()


df = yf.download("BTC-USD")

x = np.arange(len(df))
y = df["Close"]

# cost_function = []
#
# for i in range(1,20):
#     model = np.poly1d(np.polyfit(x, y, i))
#     h = model(x)
#     print(model(270))
#     # plt.plot(x, h, label = str(i))
#     root_mean_squard_error = np.sqrt(np.mean(np.power(h-y,2)))
#     print(i, root_mean_squard_error)
#     cost_function.append(root_mean_squard_error)
#
# plt.scatter(np.arange(1,20),cost_function)
# plt.legend()
# plt.show()

# from the above scatter plot we find out that a 16 degree line would solve the exercise properly:
# plt.plot(x, y)
# model = np.poly1d(np.polyfit(x, y, 16))
# h = model(x)
# plt.plot(x,h)
#
# plt.legend()
# plt.show()


from sklearn.linear_model import LinearRegression

df = yf.download("BTC-USD")
df["Tomorrow"] = df["Close"].shift(-1)

df.dropna(inplace = True)

x = df[["Open", "Close", "Low", "High"]]
y = df["Tomorrow"]

model = LinearRegression()
model.fit(x,y)

plt.plot(np.arange(len(x)),y)

prediction = model.predict(x)
plt.plot(np.arange(len(x)), prediction, "g--")


print(model.predict([[150, 160, 140, 200]]))
plt.legend()
plt.show()


# os.setnv("D:\programming\chrome_driver\chromedriver-win64/chromedriver")