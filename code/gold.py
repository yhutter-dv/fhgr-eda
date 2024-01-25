import numpy as np
import matplotlib.pyplot as plt

def moving_average(a, n):
    l=len(a)
    s=int((n-1)/2)
    b=np.zeros(l)
    for i in range(s,l-1-s):
        #print(i,a[i-s:i+s+1],sum(a[i-s:i+s+1])/n)
        b[i] = sum(a[i-s:i+s+1])/n
    return b


if __name__ == "__main__":
	price_str = np.loadtxt("./data/gold.csv", usecols=1, skiprows=10, delimiter=";", dtype="U")
	none_empty_values_indices = np.where(price_str != ".")
	number_of_indices = len(none_empty_values_indices[0])
	price = np.zeros(number_of_indices)

	for i in range(number_of_indices):
		index = none_empty_values_indices[0][i]
		price[i] = float(price_str[index])

	price_average = moving_average(price, 15)
	plt.plot(price, '.', markersize=1)
	plt.plot(price_average, 'r-', markersize=1)
	plt.show()
