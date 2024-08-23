# تابع های یک دستوری را با لامبدا می توان خلاصه نویسی کرد

# add = lambda a,b : a + b

# number_list = [1,2,3,4,5]
# y=[]
#
# # for item in number_list:
# #     y.append(item*5)
# # print(y)
#
#
# ## map function will do the above operation much faster and easier
# def zarb(x):
#     return x*5
# y=list(map(zarb, number_list))
# print(y)
#
#
# # میشه تابع ضرب رو خلاصه تر نوشت با لامبد
# zarb = lambda x: x*5
#
# y = list(map(lambda x: x*5, number_list))
# print(y)
#
#
#
# # حالا فقط اعداد زوج رو بریز:
# for item in number_list:
#     if item % 2 == 0:
#         y.append(item)
#
# print(y)
#
# # we can use filter to add a if statement :
# y=list(filter(lambda x:x%2==0,number_list))
# print(y)
#
#
#
# z = 1
# number_list = [1,2,3,4,5]
# for item in number_list:
#     z = z*item
# print(z)
#
# from functools import reduce
# z = reduce(lambda a,b : a * b , number_list)
# print(z)




# import multiprocessing
# def a():
#     for i in range(1,1001):
#         print("+++", i)
#
# def b():
#     for i in range(1,1001):
#         print("---", i)
#
# process1 = multiprocessing.Process(target=a)
# process2 = multiprocessing.Process(target=b)
#
# if __name__ == "__main__":
#     process1.start()
#     process2.start()





import numpy as np
import pandas as pd

# x = np.array([[1, 2, 3, 4],
#               [5, 6, 7, 8],
#               [9, 10, 11, 12]])
#
# # Slice for 2D data:
# # x[:: , ::]
# print(x[1:3:,1:3:])
# print(x[:2:, ::2])



# x = np.array([[10, 2, 3, 4],
#               [5, 6, 7, 8]])
# print(x>5)
# mask = x > 5
# print(x[mask])
# print(x[(7>x) & (x>3)])
# print(x[(7>x) | (x>3)])
#
#
# print(np.where(x>5))
#
# y=np.array([[10 , 2, 3, 4], [5, 6, 7, 8]])
# result = np.where(y < 5)
#
# print(list(zip(result[0], result[1])))
#
# result = np.where(y < 5, 1, -1)
# print(result)


# x = np.array([10, 2, 3, 4, 5, 6, 2, 8])
# np.append(x, 100)

# x = np.array([10, 2, 3, 4])
# y = np.array([100, 200, 300, 400])
# np.append(x, 100)
# print(np.hstack((x,y)))
# print('-------------------------------')
# print(np.vstack((x,y)))


# this code will show you an error:
# x = np.array([1,2,3,None,4,5])
# print(x*5)

#instead we should use NaN that doesnt participate in operations!
# x = np.array([1,2,3,np.NaN,4,5])
# print(x*5)


# df = pd.read_csv("data.csv")
# df.info()
# print(df.isna())
# print(df.dropna(inplace=True))
# df.fillna(100, inplace=True)
# print(df)
# print(df.duplicated())
#np.unique(x)
# df.drop_duplicates()


# df["b"] = pd.to_numeric(df["b"], errors="raise")
# df["b"] = pd.to_numeric(df["b"],errors="ignore")
# df["b"] = pd.to_numeric(df["b"],errors="coerce", downcast="float")
#
# df.info()

# df["b"] = pd.to_datetime(df["b"])
# df.info()
# print(df)


import yfinance as yf
import pandas as pd
import numpy as np
from persiantools.digits import fa_to_en
from persiantools.jdatetime import JalaliDateTime
# from datetime import datetime
#
# date_time = "۱۴۳۰۳-۰۵-۱۵"
# # print(fa_to_en(date_time))
# print(datetime.now())
# print(JalaliDateTime(datetime.now()))
#
# print(JalaliDateTime(1403, 5, 15))
# print(JalaliDateTime(1403, 5, 15).to_gregorian())
#
# print(JalaliDateTime(1403, 5, 15).isoweekday())
#
# print(JalaliDateTime.is_leap(1403))
# print(JalaliDateTime.days_in_month(12, 1403))


import pandas as pd
from persiantools.jdatetime import JalaliDate

# df = pd.read_csv("BTC-USD.CSV")
# df["Date"] = pd.to_datetime(df["Date"])
# df["Benefit"] = df["Close"] - df["Open"]
# df["Tolerance"] = df["High"] - df["Low"]
#
# df["JalaliDate"] = df["Date"].apply(lambda d: JalaliDate(d))
# df["JalaliMonth"] = df["Date"].apply(lambda d:JalaliDateTime(d).month)
# df["JalaliWeekDay"] = df["Date"].apply(lambda d:JalaliDateTime(d).isoweekday())
#
# print(df)





# data_list = [date(2020,1,12) , date(2020,1,6)]
#
#
df = pd.read_csv("BTC-USD.CSV")

# df["day1"] = df["amount"].shift(-1)
# df["amount"].rolling[3]
# sma = simple_moving_average:
# sma_3 = df["amount"].rolling(3).mean()


df["sma_21"] = df["Close"].rolling(21).mean()
df["ema_21"] = df["Close"].ewm(span=28).mean()

df.to_excel("result.xlsx")


import matplotlib.pyplot as plt

plt.plot(df["Close"], label="Close")
plt.plot(df["sma_21"], label="sma")
plt.plot(df["ema_21"], label="ema")


plt.legend()
plt.show()