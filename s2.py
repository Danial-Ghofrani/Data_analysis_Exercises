from matplotlib import pyplot as plt
import numpy as np

# x = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
# y1 = [10, 5, 7, 9, 12 , 14, 8]
# y2 = [7, 15, 14, 13, 18, 12, 1]
#
#
# plt.subplot(1,2,1)
# plt.plot(x, y1, color="red",linestyle="dashed",marker="o", label = "company A")
# # plt.scatter(x,y)
# # plt.bar(x,y)
# plt.title("Title")
# plt.xlabel("Days")
# plt.ylabel("Total")
# plt.legend()
# plt.grid()
#
#
# plt.subplot(1,2,2)  # if you change the first number to 2, and the second to 1, the plots will be in 2 rows!
# plt.plot(x, y2,"g--o", label = "company B")
# plt.title("Title")
# plt.xlabel("Days")
# plt.ylabel("Total")
# plt.legend()
# plt.grid()
# plt.show()

# plt.savefig("test.png")

# x = [1, 2, 3, 4, 5]
# y = [1, 2, 3, 4, 5]
# z = [10, 7, 12, 14, 9]
#
# fig = plt.figure(figsize=(10,6))
# ax = fig.add_subplot(111, projection = "3d")
#
# ax.scatter(x,y,z)
# plt.show()

# print(np.pi)
# print(np.e)
# print(np.abs(-1))
# print(np.power(10,3))
# print(np.round(np.pi,6))
# print(np.sin(90))
# print(np.sin(np.radians(90)))
# print(np.log(1000))
# print(np.floor(1.1))
# print(np.ceil(1.9))

# x = [10, 7, 15, 9, 16]
# # we cant do math operations on python list!
#
# # but we can change it to numpy array and do whatever!
# z = np.array(x)
# print(z*3)
# print(z/3)
# print(z+2)
# print(z-4)
#
# py_list = [[1,2,3,],[4,5,6]]
# print(py_list)
# print(len(py_list))
# print(type(py_list))
#
# n_array = np.array(py_list)
# print(n_array)
# print(n_array.shape)
# print(n_array.ndim)
# print(n_array.size)
# print(n_array.dtype)


# z = np.zeros((3,4,2 ))
# print(z)
#
# o = np.ones((2, 3, 4))
# print(o)
# print(o.ndim)
#
# f = np.full((2,4), 12.7)
# print(f)
# print(f.ndim)

# x = np.array([[1, 2, 3], [8, 9, 10]])
# print(x)
# z = np.zeros(x.shape)
# print(z)
#
# f = np.full_like(x, 7)
# print(f)

x = np.array([[1, 2, 3], [4, 5, 6]])
# print(x)
# print(x.T)
#
#
# print(x.min(axis=0))
# print(x.max())
# print(x.sum())
# print(x.mean())

## flattening : reducing 2D to 1D
# print(np.ravel(x))

# x = np.array([[1, 7, 9],
#              [4, 2, 6]])
# print(x.shape)
# print(x.reshape(3, 2))
#
# x = np.array([[1, 7, 9],
#              [4, 2, 6]])\
#     .astype(np.float32)\
#     .reshape(1,-1)
# print(x)
#
# print(np.random.random((3, 4)))
# print(np.random.randint(12, 18, (5,6)))

# x = np.arange(1, 5, 0.2)
# print(x)
#
# y = np.linspace(12, 39, 8)
# print(y)

# z = np.arange(100,1300,100).reshape((3,4))
# print(z)

# x = np.array([5, 3, 4, 1, 5, 1, 5, 8])
# diff = np.diff(x)
# print(diff)


import yfinance as yf
btc = yf.download("BTC-USD")

print(btc)
print(btc.columns)