import numpy as np
import matplotlib.pyplot as plt

t_min = np.array([[2, 3, 3, 3, 2],
                 [3, 3, 3, 3, 3],
                 [2, 2, 3, 3, 3],
                 [3, 3, 3, 3, 3],
                 [2, 3, 2, 2, 3],
                 [3, 3, 3, 3, 2],
                 [2, 2, 3, 3, 2]])


t_sec = np.array([[59, 12, 2, 2, 51],
                 [2, 1, 1, 1, 1],
                 [57, 57, 0, 2, 0],
                 [4, 1, 0, 0, 2],
                 [58, 0, 58, 59, 11],
                 [0, 12, 2, 3, 51],
                 [56, 57, 1, 1, 59]])

t_sec_total = 60 * t_min + t_sec

t_std_sec = np.std(t_sec_total, 1)
t_sum_sec = np.sum(t_sec_total, 1)

plt.plot(t_sum_sec / 60, t_std_sec, 'o')
plt.xlabel("Time in minutes")
plt.ylabel("Standard Deviation")
plt.title("Standard Deviation over Time")
plt.show()
