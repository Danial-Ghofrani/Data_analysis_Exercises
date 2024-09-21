import numpy as np
import pandas as pd
import yfinance as yf
import datetime
import matplotlib.pyplot as plt

# df = yf.download("BTC-USD")
#
# df["Date"] = pd.to_datetime(df.index)
# df["Month"] = df["Date"].dt.month
# # print(df.groupby("Month").mean())
#
# # plt.subplot(1, 2, 1)
# # plt.plot(df["Close"])
# # plt.subplot(1, 2, 2)
# # plt.hist(df["Close"])
#
# print(df.describe())
# df.boxplot(column = "Close", by = "Month")
#
#
# plt.show()


import cv2 as cv

# img = cv.imread("01.bmp")
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
# # Thresholding
# gray[gray>50] = 255
# gray[gray<=50] = 0
#
# contours, hierarchy = cv.findContours(gray, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
#
#
# for contour in contours:
#
#
#
#     z = np.zeros_like(img)
#     z = cv.drawContours(z, contour, -1, (255,255,255), cv.FILLED)
#
#
#     # img = cv.drawContours(img, contour, -1, (0,255,0), 2)
#     # print(cv.contourArea(contour))
#     # cv.imshow("Image", img)
#
#     cv.imshow("Image", z)
#     cv.waitKey(0)



img = cv.imread("brain.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# # Thresholding
# gray[gray>50] = 255
# gray[gray<=50] = 0

contours, hierarchy = cv.findContours(gray, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

i = 1
for contour in contours:
    x,y,w,h = cv.boundingRect(contour)

    z= gray[y:y+h, x:x+w]
    z = cv.resize(z, (50,50))

    # img = cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    img = cv.drawContours(img, contour, -1, (0,255,0), 1)
    # print(cv.contourArea(contour))
    # cv.imshow("Image", img)

    # cv.imshow("Contour", z)
    cv.imshow("Image", img)
    # cv.imwrite(f"Contour{i}.jpg", z)
    cv.waitKey(1)
    i += 1
