# import numpy as np
#
# print(np.pi)
# print(np.e)
#
# print(np.abs(-1))
# print(np.power(10,3))
# print(np.round(np.pi,decimals=6))
#
#
# print(np.sin(np.radians(90)))
#
# print(np.log(100))
#
# print(np.floor(1.1))
# print(np.ceil(1.1))

#####Arrays in pandas
import numpy as np
import pandas as pd

## below operations wont be possible because it is a list
# x=[10,7,15,9,16]
# print(x*3)
# print(x/2)
# print(x+1)
# print(x-2)

#
# z=np.array(x)
# print(z*3)
# print(z/2)
# print(z+1)
# print(z-2)


# x = np.array(object:[1,200,3,4],dtype=np.byte16)


# w=np.zeros((2,3,4,2))
# print(w)
# x = np.array(([[1,2]]))
# z=np.zeros_like(x)
# f = np.full_like(x,7)
# print(f"f is : {f}")
#
# x = np.array([[1,7,9],
#               [4,2,6]])
# # print(x)
# # print(x.T)
#
#
#
# x.max()
# x.max()
# x.sum()
# x.min()
# print(x.min(axis=0))
#
#
#
# # how to Flatten our array:
# print(np.ravel(x))
#
# #reshaping:
# print(x.reshape(6,1))
#
# #-1 here is used when you dont know exactly how many cols or rows we have!!
# print(x.reshape(1,-1))
#

# x=np.random.random((3,4))
# x=np.random.randint(12,18,(5,6))
#
# print(x)


# x = np.arange(1.1 , 5 , 0.2)
# x= np.linspace(12,37,6)
# print(x)

# x = np.arange(1,13).reshape(3,4) *100

# x = np.array([5, 3, 4, 1, 5, 1, 5, 8])
# diff = np.diff(x)
# print(diff)
#
#
# diff2 = np.diff(x,2)
# print(diff2)


# working with data frame
# df = pd.read_csv("students.CSV")
# # df.info()
# # df["enzebat"] = df["average"] + 1
# # print(df)
#
# print(df[["name","family"]].iloc[[1,2]])
#
#
# # converting lists to df:
# person_list = [{"name":"a", "age":20}, {"name":"b", "age":27}]
#
#

x = np.array([1, 2, 3, 4, 5])

print(x.mean())
print(np.median(x))

import scipy.stats as stats
print(stats.mode(x))



