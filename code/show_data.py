import numpy as np
import matplotlib.pyplot as plt


def show_data(x, number_of_bins):
    print("Number of Elements: ", len(x))
    print("Max: ", max(x))
    print("Min: ", min(x))
    print("Mean: ", np.round(np.mean(x), 2))
    print("Std: ", np.round(np.std(x), 2))
    print("Quantil 25: ", np.quantile(x, 0.25))
    print("Quantil 75: ", np.quantile(x, 0.75))
    plt.figure()
    # First number of figures in height then to the right then the cell where the figure should be plotted
    plt.subplot(211)
    plt.grid()
    plt.plot(x, 'o')

    plt.subplot(212)
    plt.hist(x, bins=number_of_bins)
    plt.show()


x = np.array([12.1, 12.5, 12.4, 11.9, 12.5, 12.8, 12.3,
             12.5, 12.2, 12.9, 13.1, 12.5, 12.8, 12.3])

if __name__ == "__main__":
    show_data(x, 5)
