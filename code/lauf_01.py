import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
time_min = np.array([2, 3, 3, 3, 3, 3, 3, 3, 3, 3])
time_sec = np.array([58, 12, 1, 22, 11, 38, 28, 21, 19, 35])
time_sec_total = 60 * time_min + time_sec
time_sec_accumulated = time_sec_total.cumsum()

plt.figure(1)
plt.bar(x - 0.5, time_sec_total, edgecolor=(0, 0, 0), width=1)
plt.axis([0, 10, 0, 250])
plt.xticks(x)
plt.xlabel("Distance travelled in kilometer")
plt.ylabel("Time in Seconds")
plt.title("Alexander Schnell")
plt.savefig("./images/lauf_01.png")
plt.figure(2)
plt.axis([0, 10, 0, 2050])
plt.xticks(x)
plt.plot(x, time_sec_accumulated, "ro-")
plt.xlabel("Distance in kilometer")
plt.ylabel("Time in Seconds")
plt.title("Alexander Schnell")
plt.savefig("./images/lauf_02.png")
plt.show()
