import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
	km = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	time_minutes = np.array([2, 3, 3, 3, 3, 3, 3, 3, 3, 3])
	time_seconds = np.array([58, 12, 1, 22, 11, 38, 28, 21, 19, 35])
	time_seconds_total = time_minutes * 60 + time_seconds
	time_seconds_total_sum = time_seconds_total.cumsum()
	m = km * 1000.0
	m_s = m / time_seconds_total

	plt.figure(1)
	plt.title("Alexander Schnell")
	plt.axis([0, 10, 0, 250])
	plt.bar(km - 0.5, time_seconds_total, edgecolor=(0, 0, 0), width=1)
	plt.xticks(km)
	plt.xlabel("Strecke in km")
	plt.ylabel("Zwischenzeit in s")
	plt.show()

	plt.figure(2)
	plt.axis([0, 11, 0, 35])
	plt.xticks(km)
	plt.plot(km - 0.5, time_seconds_total_sum / 60, "ro-")
	plt.xlabel("Strecke in km")
	plt.ylabel("Zeit in min")
	plt.show()

	plt.figure(3)
	plt.axis([0, 11, 0, 50])
	plt.xticks(km)
	plt.plot(km, m_s, "ro-")
	plt.xlabel("Strecke in km")
	plt.ylabel("Geschwindigkeit in m/s")
	plt.savefig("./images/durchschnittsgeschwindigkeit.png")

	plt.figure(4)
	plt.hist(m_s, bins=6, edgecolor=(0, 0, 0))
	plt.savefig("./images/durchschnittsgeschwindigkeit_histogramm.png")
	plt.show()



