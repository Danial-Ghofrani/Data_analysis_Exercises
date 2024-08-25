# import numpy as np
# import pandas as pd
# import yfinance as yf
#
#
# x = np.arange(1,100).reshape(-1,1)
# weights = np.array([1, 3, 4, 5, 6]).reshape(-1,1)
#
# data = pd.read_csv()
#
# df = pd.DataFrame(data, columns= ["Close", "OPEN"])
# df = pd
# my_list = list(df.rolling(5).mean())
#
#
# for item in my_list:
#     if len(item) == 5:
#         print(item.values)

from datetime import datetime, timedelta
import pandas as pd


# dt = datetime.now()
# print(dt)
#
# print(dt-timedelta(minutes=7))
#
#
# test = [{"Time":datetime(2019, 1, 18, 20, 16, 32)},
#          {"Time":datetime(2021, 1, 17, 20, 9, 32)},]
#
# def minus_7(date_time):
#     return date_time-timedelta(minutes=7)
#
# df = pd.DataFrame(test)
#
# df["Time"] = df["Time"].apply(minus_7)

#
# test = [{"Time": 1},
#          {"Time": 2},
#         {"Time": 3}]
#
# df = pd.DataFrame(test)
# df["now_time"] = df["Time"].apply(lambda p :datetime.now()- timedelta(minutes=p))
#
# print(df)
#
# df = pd.read_csv("data.csv")
#
# # df.fillna(method="ffill",inplace=True )
# # df.fillna(method="bfill", inplace=True )
# #
# #
# # print(df)
# # print(df.describe())
#
# from sklearn.impute import SimpleImputer, KNNImputer
# import numpy as np
#
# # imput = KNNImputer(n_neighbors=5)
# # print(imput.fit_transform(df))
# #
# # print(df)
#
# df.where(df["a"]>5, 0, inplace=True)
# impute = SimpleImputer(missing_values=np.nan, strategy="mean")
# print(impute.fit_transform(df))


import numpy as np
import matplotlib.pyplot as plt

x = [1,1,2,2,3,2,2,1,1]*5

plt.plot(x)
plt.show()