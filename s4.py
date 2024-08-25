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
# img = cv2.imread("images.jpg")
# print(img)
# print(type(img))
# print(img.shape)
# print(img.dtype)
# print(img.ndim)
#
# cv2.imshow("Aks", img)
# # cv2.waitKey(2000)
# cv2.waitKey(0)

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img, cmap="gray")
# plt.show()
# print(img.shape)
# print(img.size)
#
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# plt.imshow(img, cmap="gray")
# plt.show()
# print(img.shape)
# print(img.size)

# img = cv2.imread("three_colors.png")
# cv2.imshow("Image", img)
# cv2.imshow("image1", img[500:,500:,:])
# cv2.waitKey()

# img = cv2.imread("images.jpg")
# r , g , b = cv2.split(img)
#
# plt.subplot()
# plt.hist(np.ravel(r),color="red", bins=256)
# plt.hist(np.ravel(g),color="green", bins=256)
# plt.hist(np.ravel(b),color="blue", bins=256)
# plt.show()
# cv2.imshow("image", img)
# cv2.waitKey(0)

import cv2
from matplotlib import pyplot as plt

# img = cv2.imread("face.png", cv2.IMREAD_GRAYSCALE)
#
# plt.subplot(2, 2, 1)
# plt.imshow(img, cmap="gray")
#
# plt.subplot(2,2,3)
# plt.hist(img.ravel(), bins=256)
#
#
# plt.subplot(2, 2, 4)
# img = cv2. equalizeHist(img)
#
# plt.hist(img.ravel(), bins=256)
#
# plt.subplot(2, 2, 2)
# plt.imshow(img, cmap="gray")
#
# plt.show()

# video_reader = cv2.VideoCapture("my_vid.mp4")
# ret , frame = video_reader.read()
#
# while ret:
#     ret, frame = video_reader.read()
#
#     frame = cv2.resize(frame, (640,480))
#     edge = cv2.Canny(frame, 20, 200)
#
#     cv2.imshow("Live Video", frame)
#     cv2.imshow("Live Edge", edge)
#     if cv2.waitKey(100) ==27:
#         break


# face_path = r"C:\Users\Danial\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"
# eye_path = r"C:\Users\Danial\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2\data\haarcascade_eye.xml"
#
# face_detector = cv2.CascadeClassifier(face_path)
# eye_detector = cv2.CascadeClassifier(eye_path)
#
#
# video_reader = cv2.VideoCapture(0)
# ret , frame = video_reader.read()
#
# while ret:
#     ret, frame = video_reader.read()
#     faces = face_detector.detectMultiScale(frame, 1.3, 5)
#     eyes = eye_detector.detectMultiScale(frame)
#
#     for (x,y,w,h) in faces:
#         cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
#     for (x,y,w,h) in eyes:
#         cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),2)
#
#
#     # frame = cv2.resize(frame, (640,480))
#     # edge = cv2.Canny(frame, 20, 200)
#
#     cv2.imshow("Live Video", frame)
#     # cv2.imshow("Live Edge", edge)
#
#     if cv2.waitKey(100) ==27:
#         break

import yfinance as yf
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database

# cennection_string = "mysql+pymysql://root:root123@localhost:3306/crypto"
#
# create_database(cennection_string)
# engine = create_engine(cennection_string)
#
# btc = yf.download("BTC-USD", timeout=20)
# btc.to_sql("btc_table", engine, if_exists="replace")

# host = "localhost"
# port = "3306"
# database = "crypto"
# user = "root"
# password = "@root123"


import pandas as pd

# df = pd.read_excel("sells.xlsx")
# df.index = df["days"]
# df.drop(columns=["days"], inplace=True)
# print(df.loc["mon"])

# df = pd.read_excel("sells.xlsx", index_col="days")
# print(df)

import yfinance as yf

# btc = yf.download("BTC-USD")
# btc.info()
# btc["Date"] = btc.index
# print(btc.head())

import pandas as pd
# sell_df = pd.read_excel("sells.xlsx")
# customer_df =pd.read_excel("customers.xlsx")
#
# sell_df["customers"] = customer_df["customers"]
# print(sell_df)
# above operation is puting the customers data into the wrong day because of inapropriate index!

# sell_df = pd.read_excel("sells.xlsx", index_col="days")
# customer_df =pd.read_excel("customers.xlsx", index_col="days")
# sell_df["customers"] = customer_df["customers"]
# print(sell_df)


btc = yf.download("BTC-USD", start="2024-01-10", end="2024-01-20")
eth = yf.download("ETH-USD", start="2024-01-10", end="2024-01-15")

btc.index = np.arange(len(btc))
eth.index = np.arange(len(eth))

btc["ETH_CLOSE"] = eth["Close"]

print("btc")
btc.to_excel("btc.xlsx")
# the above code puts the ETH close in a wrong order!
# the starting dates of two data were different so it should use date as the index!+


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


