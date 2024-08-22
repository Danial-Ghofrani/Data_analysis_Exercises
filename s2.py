from matplotlib import pyplot as plt

x = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
y = [10, 5, 7, 9, 12 , 14, 8]

plt.plot(x,y)
plt.scatter(x,y)
plt.bar(x,y)


plt.show()

plt.savefig("test.png")