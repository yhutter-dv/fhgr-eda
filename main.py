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

def moving_average(a, n):
    l=len(a)
    s=int((n-1)/2)
    b=np.zeros(l)
    for i in range(s,l-1-s):
        b[i] = sum(a[i-s:i+s+1])/n
    return b

if __name__ == "__main__":
	data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	show_data(data, 3)
	data_average = moving_average(data, 3)
	show_data(data_average, 3)