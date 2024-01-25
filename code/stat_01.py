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




if __name__ == "__main__":
	temp = np.array([2,2,4,1,8,7,8,8,10,2,2,4,3,5,5,6,4,7,10,12,12,11,3,4,6,6])
	show_data(temp, 5)

	visitors_swimming = np.array([12,22,14,8,13,109,132,99,117,14,21,8,7,11,12,111,112,100,18])
	show_data(visitors_swimming, 5)
