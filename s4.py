import random as rd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# x = np.random.random(1000)
# x= np.random.randn(100000)
# x = np.random.normal(loc = 175 , scale= 25 , size= 10000)
# x = np.random.uniform(low=0, high=10, size=10000)
# x = np.random.binomial(6,0.1,size = 100000)
#
#
# plt.hist(x, bins=50)
# plt.show()
# x = [7, 2, 5, 6, 7, 8, 9, 11]
# x_range = max(x) - min(x)
# img = plt.imread("japan.png")
#
# print(img)
# print(type(img))
# print(img.shape)
# print(img.dtype)
# print(img.ndim)
#
# plt.imshow(img)
# plt.show()


# img = plt.imread("three_colors.png")
#
# plt.subplot(1,3,1)
# plt.title("red")
# plt.imshow(img[:,:,0], cmap="gray")
#
# plt.subplot(1,3,2)
# plt.title("green")
# plt.imshow(img[:,:,1], cmap="gray")
#
# plt.subplot(1,3,3)
# plt.title("blue")
# plt.imshow(img[:,:,2], cmap="gray")
#
# plt.show()


# img = plt.imread("images.jpg")
#
# plt.subplot(1,3,1)
# plt.title("red")
# plt.imshow(img[:,:,0], cmap="gray")
#
# plt.subplot(1,3,2)
# plt.title("green")
# plt.imshow(img[:,:,1], cmap="gray")
#
# plt.subplot(1,3,3)
# plt.title("blue")
# plt.imshow(img[:,:,2], cmap="gray")
#
# plt.show()


import cv2
img = cv2.imread("images.jpg")
# print(img)
# print(type(img))
# print(img.shape)
# print(img.dtype)
# print(img.ndim)
#
# cv2.imshow("Aks", img)
# # cv2.waitKey(2000)
# cv2.waitKey(0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img, cmap="gray")
plt.show()
print(img.shape)
print(img.size)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img, cmap="gray")
plt.show()
print(img.shape)
print(img.size)
#
# df =pd.read_csv("Cities_data.CSV")
# print(df.head())
#
# x=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# x_range = max(x) - min(x)
#
# img = plt.imread("")
# print(img)
# print(type(img))
#
# print(img.shape)
# print(img.dtype)
# print(img.)
#
#
# plt.subplot(1,3,1)
# plt.title("red")
# plt.imshow(img[:,:,0])



