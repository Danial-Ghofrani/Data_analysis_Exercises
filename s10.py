import numpy as np
import matplotlib.pyplot as plt

# x = np.array([1,1,2,2,4,2,2,1,1,1,1.8,2.3,2,5,2.2,1.9,1,1]*5)
# x2= [1,1.8,2.3,2,5,2.2,1.9,1,1]
# plt.plot(x)
# plt.show()


#first we assume that we know te pattern and we want to find it on the data
# x = np.array([1,1,2,2,4,2,2,1,1]*5)
# n = len(x)
#
# pattern = np.array([1,1,2,2,4,2,2,1,1])
# pattern_len = len(pattern)
# pattern_sum = np.sum(pattern)
# coef = 0.9
#
# sse_list = []
#
# for i in range (n - pattern_len):
#     part = x[i:i + pattern_len]
#     sse = np.sum(np.power(part - pattern, 2))
#     sse_list.append(pattern_sum - sse)
#     if sse > pattern_sum *coef:
#         print(i)
#
# plt.subplot(2, 1, 1)
# plt.plot(x)
#
# plt.subplot(2, 1, 2)
# plt.plot(sse_list)
#
# plt.plot()
# plt.show()



#now we assume that we know the len of pattern and we want to find the pattern
vc