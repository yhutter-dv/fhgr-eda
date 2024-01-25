import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
	height = np.loadtxt("./data/nba.csv", delimiter=",", usecols=(1), skiprows=1)
	weight = np.loadtxt("./data/nba.csv", delimiter=",", usecols=(2), skiprows=1)
	games_played = np.loadtxt("./data/nba.csv", delimiter=",", usecols=(3), skiprows=1)

	model = np.polyfit(height, weight, 1)
	m = model[0]
	t = model[1]

	corrcoeff = np.corrcoef(height, weight)
	print(corrcoeff[0, -1])

	plt.figure()
	plt.xlabel("Körpergrösse in cm")
	plt.ylabel("Gewicht in kg")
	plt.plot(height, weight, 'o', c="black")
	plt.plot(height, height * m + t, '-', c="black", linewidth=1)
	plt.grid(visible=True)
	plt.show()

