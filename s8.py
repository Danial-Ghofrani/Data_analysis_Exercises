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
# print(df)
# df.describe()
# df.fillna(100, inplace=True)
# df.fillna(method="ffill",inplace=True )
# df.fillna(method="bfill", inplace=True )



from sklearn.impute import SimpleImputer, KNNImputer
import numpy as np

df = pd.read_csv("data.csv")
# impute = SimpleImputer(missing_values=11, strategy="mean")
# impute = SimpleImputer(missing_values=np.nan, strategy="median")
# impute = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
# impute = SimpleImputer(missing_values=np.nan, strategy="constant", fill_value=10)
#
# imput = KNNImputer(n_neighbors=5)
# print(impute.fit_transform(df))

# print(df)
#
# df.where(df["a"]>15, np.nan, inplace=True)
# impute = SimpleImputer(missing_values=np.nan, strategy="mean")
#
# print(impute.fit_transform(df))

# import numpy as np
# X = [1,2,3,4,5]
#
# print(np.mean(X))
# print(np.median(X))

import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# image_list = []
#
# for file in os.listdir("dataset"):
#     img = cv.imread(f"dataset/{file}", cv.IMREAD_GRAYSCALE)
#     image_list.append(img)
#
# image_list = np.array(image_list)
# np.savez_compressed("image_dataset.npz", images = image_list)

data = np.load("image_dataset.npz")
images = data["images"]



# print(images.shape)
# plt.imshow(images[17], cmap="gray")
# plt.show()
#
# for image in images:
#     result = np.zeros_like(image)
#     plt.subplot(1, 3, 2)
#     vector = np.ravel(image)
#     n = len(vector)
#     mean = np.mean(vector)
#     std = np.std(vector)
#     up_coef = 3
#     down_coef = 3
#     up_line = mean+std*up_coef
#     down_line = mean-std*down_coef
#
#     plt.plot(vector)
#     plt.plot([0, n], [mean,mean], 'g--')
#     plt.plot([0,n], [up_line, up_line], "r--")
#     plt.plot([0,n], [down_line, down_line ], "r--")
#
#
#     plt.subplot(1, 3, 1)
#     plt.imshow(image, cmap="gray")
#
#     plt.subplot(1, 3, 3)
#     result = np.ravel(result)
#     result[vector>up_line] = 255
#     result[vector<down_line] = 255
#     result = result.reshape(image.shape)
#     plt.imshow(result, cmap="gray")
#
#     plt.show()


# print(images.shape)
# plt.imshow(images[17], cmap="gray")
# plt.show()

for image in images:
    result = np.zeros_like(image)
    plt.subplot(1, 3, 2)
    vector = np.ravel(image)
    n = len(vector)
    # model = np.poly1d(np.polyfit(np.arange(len(vector)), vector, 1))
    # reg = model(vector)

    # std = np.std(vector)
    # up_coef = 3
    # down_coef = 3
    # up_line = reg+std*up_coef
    # down_line = reg-std*down_coef
    #
    # plt.plot(vector)
    # plt.plot([0, n], [reg,reg], 'g--')
    # plt.plot([0,n], [up_line, up_line], "r--")
    # plt.plot([0,n], [down_line, down_line ], "r--")
    #
    #
    # plt.subplot(1, 3, 1)
    # plt.imshow(image, cmap="gray")
    #
    # plt.subplot(1, 3, 3)
    # result = np.ravel(result)
    # result[vector>up_line] = 255
    # result[vector<down_line] = 255
    # result = result.reshape(image.shape)
    # plt.imshow(result, cmap="gray")
    #
    # plt.show()
    #



import numpy as np
import matplotlib.pyplot as plt

# x = [1,1,2,2,3,2,2,1,1]*5
#
# plt.plot(x)
# plt.show()


# x = np.array([6, 1, 4])
# print(np.tile(x, 10))
# print(np.repeat(x, 10))
# plt.plot(np.tile(x, 10))
# plt.plot(np.repeat(x, 10))
# plt.show()


# scores = np.asarray_chkfinite([-3, 8, 12, -19, 16, 22, 17, 24, 9])
# print(scores)

# scores[scores<0] = 0
# scores[scores>20] = 20

# print(np.clip(scores, 0, 20))


numbers = np.array([10, 12, 17])
print(np.pad(numbers, [3,5], mode="constant", constant_values=[2,4]))
print(np.pad(numbers, [3,5], mode="edge"))
print(np.pad(numbers, [3,5], mode="reflect"))
print(np.pad(numbers, [3,5], mode="linear_ramp"))

plt.plot(np.pad(numbers, [3,5], mode="linear_ramp"))
plt.show()






