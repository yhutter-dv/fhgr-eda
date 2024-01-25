import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
	km = np.array([1, 2, 3, 4, 5])
	names = ["Urs Meier", "Adrian Lippuner", "Corsin Gmüer", "Ralf Münsing", "Alexander Schnell", "Rainer Uebel", "Sebastian Frisch"]
	minutes = np.array([
		[2, 3, 3, 3, 2],
		[3, 3, 3, 3, 3],
		[2, 2, 3, 3, 3],
		[3, 3, 3, 3, 3],
		[2, 3, 2, 2, 3],
		[3, 3, 3, 3, 2],
		[2, 2, 3, 3, 2],
	])
	seconds = np.array([
		[59, 12, 2, 2, 51],
		[2, 1, 1, 1, 1],
		[57, 57, 0, 2, 0],
		[4, 1, 0, 0, 2],
		[58, 0, 58, 59, 11],
		[0, 12, 2, 3, 51],
		[56, 57, 1, 1, 59],
	])

	seconds_total = minutes * 60 + seconds
	seconds_total_sum = seconds_total.cumsum(1)

	seconds_total_varriance = np.var(seconds_total, 1)
	seconds_total_per_runner = seconds_total_sum[:, 4]
	seconds_total_standard_deviation = np.sqrt(seconds_total_varriance)

	plt.figure()
	plt.plot(seconds_total_per_runner, seconds_total_standard_deviation, 'o')
	plt.xlabel("Endzeit in s")
	plt.ylabel("Standardabweichung in s")
	plt.grid(visible=True)
	plt.savefig("./images/Laufzeit_über_Varianz.png")

	y_model = np.polyfit(seconds_total_per_runner, seconds_total_standard_deviation, 1)
	m = y_model[0]
	t = y_model[1]
	plt.plot(seconds_total_per_runner, m * seconds_total_per_runner + t, 'r')
	plt.show()

	correlation_matrix = np.corrcoef(seconds_total)
	plt.figure()
	plt.pcolor(correlation_matrix)
	plt.pcolor(correlation_matrix > 0.95)
	plt.show()

	def difference(a, b):
		result = (a - b) ** 2
		result = sum(result)
		result = np.sqrt(result)/len(b)
		return result

	matrix = np.zeros((7, 7))
	for i in range(len(names)):
		for j in range(len(names)):
			matrix[i, j] = difference(seconds_total[i], seconds_total[j])
	plt.figure()
	plt.pcolor(matrix)
	plt.pcolor(matrix < 0.3)
	plt.show()






