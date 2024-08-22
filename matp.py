from matplotlib import pyplot as plt
x = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
y1 = [10, 5, 7, 9, 12 , 14, 8]
scale = [700, 1500, 1400, 13000, 18000, 1200, 100]

plt.scatter(x, y1, color="green", label="company A", s= scale, alpha=0.5)

plt.show()