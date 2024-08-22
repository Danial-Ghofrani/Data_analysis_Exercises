from matplotlib import pyplot as plt

x = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
y1 = [10, 5, 7, 9, 12 , 14, 8]
y2 = [7, 15, 14, 13, 18, 12, 1]


plt.subplot(1,2,1)
plt.plot(x, y1, color="red",linestyle="dashed",marker="o", label = "company A")
# plt.scatter(x,y)
# plt.bar(x,y)
plt.title("Title")
plt.xlabel("Days")
plt.ylabel("Total")
plt.legend()
plt.grid()


plt.subplot(1,2,2)  # if you change the first number to 2, and the second to 1, the plots will be in 2 rows!
plt.plot(x, y2,"g--o", label = "company B")
plt.title("Title")
plt.xlabel("Days")
plt.ylabel("Total")
plt.legend()
plt.grid()
plt.show()

# plt.savefig("test.png")