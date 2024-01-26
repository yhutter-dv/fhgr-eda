import numpy as np
import matplotlib.pyplot as plt

def show_data(x, bins):
	median = np.median(x)
	max_value = max(x)
	min_value = min(x)
	mean = np.mean(x)
	quant_25 = np.quantile(x, 0.25)
	quant_75 = np.quantile(x, 0.75)
	std = np.std(x)
	variance = np.var(x)

	print(f"Min: {min_value}")
	print(f"Max: {max_value}")
	print(f"Median: {median}")
	print(f"Mean: {mean}")
	print(f"Quantile 25: {quant_25}")
	print(f"Quantile 75: {quant_75}")
	print(f"Standard Deviation: {std}")
	print(f"Variance: {variance}")
	
	f, (ax1, ax2) = plt.subplots(ncols=1, nrows=2)
	ax1.plot(x)
	ax2.hist(x, bins=bins, edgecolor=(0, 0, 0))
	plt.grid(visible=True)	
	plt.show()

def vector_magnitude(x):
	return np.sqrt(sum(x ** 2))

def moving_average(a, n):
    l=len(a)
    s=int((n-1)/2)
    b=np.zeros(l)
    for i in range(s,l-1-s):
        b[i] = sum(a[i-s:i+s+1])/n
    return b

def scatter_with_linear_regression(a, b, xlabel, ylabel):
	plt.figure()
	plt.plot(a, b, 'o')
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.grid()

	rho = np.corrcoef(a, b)
	print(f"Correlation is: {rho[0,-1]}")

	bestimmtheitsmass = rho**2
	print(f"Bestimmtheitsmass is: {bestimmtheitsmass[0,-1]}")

	model = np.polyfit(a, b, 1)

	m, t = model

	plt.plot(a, a * m + t, 'r')

	plt.show()

if __name__ == "__main__":
	data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	show_data(data, 3)
	data_average = moving_average(data, 3)
	show_data(data_average, 3)

	vector = np.array([1, 2, 0])
	magnitude = vector_magnitude(vector)
	print(f"Magnitude of Vector {vector} is {magnitude}")

	feet_size = np.array([42, 44, 45, 39, 40, 42, 42, 38, 44, 46])
	height = np.array([1.8, 1.88, 1.92, 1.67, 1.74, 1.81, 1.78, 1.55, 1.86, 1.91])

	scatter_with_linear_regression(feet_size, height, "Schuhgrösse", "Körpergrösse")
