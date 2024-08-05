import matplotlib
from matplotlib import pyplot as plt

# x=["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
# y1=[10,5,7,9,12,14,8]
# scale=[700,15000,1400,13000,18000,1200,500]
# plt.scatter(x,y1,color="green", label="")

x=[1,2,3,4,5]
y=[1,2,3,4,5]
z=[10,7,12,14,9]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111,projection="3d")
plt.show()