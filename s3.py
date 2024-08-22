# تابع های یک دستوری را با لامبدا می توان خلاصه نویسی کرد

# add = lambda a,b : a + b

number_list = [1,2,3,4,5]

y=[]
# for item in number_list:
#     y.append(item*5)
#
# def zarb(x):
#
# y=list(map(zarb,number_list))
#
# میشه تابع ضرب رو خلاصه تر نوشت با لامبد


# حالا فقط اعداد زوج رو بریز:
# y=list(filter(lambda x:x%2==0,number_list))
# print(y)
#
# # حاصل ضرب کل لیست:
# z = reduce(lambda a,b:a*b, number_list)


import multiprocessing


import numpy as np
import pandas as pd

x = np.array([1,2,3,4,5,6,7,8])
print(x>5)
print(x[(7>x) & (x>3)])
print(np.where(x>5))

y=np.array([[10 , 2, 3, 4], [5, 6, 7, 8]])
result = np.where(y < 5, 1, -1)
print(result)


# np.append(x, 100)

print(np.h.stack((x,y)))
print(np.vstack((x,y)))

z= np.array([1,2,3,None,4,5])
z= np.array([1,2,3,np.NaN,4,5])
#NaN is the same as none but it doesnt participate in operations so we will not get an error when we run z*5
print(z*5)

# df.dropna()
# df.dropna(inplace=True)
# print(df)
#
# df.fillna(100,inplace=True)

# print(df.duplicated())
# print(df.drop_duplicates())

from persiantools.digits import fa_to_en
from persiantools.jdatetime import JalaliDateTime
from datetime import datetime

# how to add features to dataframe!
# df["Benefit"] = df["Close"]-df["Open"]

# data_list = [date(2020,1,12) , date(2020,1,6)]
#
#
#
# df["day1"] = df["amount"].shift(-1)

# df["amount"].rolling[3]
#
# sma = simple_moving_average:
sma_3 = df["amount"].rolling(3).mean()