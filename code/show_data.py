import numpy as np
import matplotlib.pyplot as plt


def show_data(x=[], number_of_bins=5, title="", x_axis_title="", y_axis_title=""):
    number_of_elements = len(x)
    max_value = np.round(max(x), 2)
    min_value = np.round(min(x), 2)
    mean = np.round(np.mean(x), 2)
    median = np.round(np.median(x), 2)
    std = np.round(np.std(x), 2)
    variance = np.round(np.var(x), 2)
    quant_25 = np.round(np.quantile(x, 0.25), 2)
    quant_75 = np.round(np.quantile(x, 0.75), 2)

    plt.figure()

    # First number of figures in height then to the right then the cell where the figure should be plotted
    plt.subplot(211)

    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis_title)
    plt.title(title)

    plt.grid()
    plt.plot(x, 'o')

    # Create textbox with useful information.
    # see https://matplotlib.org/stable/gallery/text_labels_and_annotations/placing_text_boxes.html
    ax = plt.gca()
    props = dict(boxstyle='round', facecolor='white')
    content = '\n'.join([
        f"Number of Elements: {number_of_elements}",
        f"Max: {max_value}",
        f"Mean: {mean}",
        f"Median: {median}",
        f"Min: {min_value}"
    ])
    ax.text(0.05, 0.95, content, transform=ax.transAxes,
            fontsize=14, verticalalignment='top', bbox=props)

    plt.subplot(212)

    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis_title)
    plt.title(title)

    plt.hist(x, bins=number_of_bins)

    ax = plt.gca()
    content = '\n'.join([
        f"Variance : {variance}",
        f"Standard Deviation: {std}",
        f"Quantile 25: {quant_25}",
        f"Quantile 75: {quant_75}"
    ])
    ax.text(0.05, 0.95, content, transform=ax.transAxes,
            fontsize=14, verticalalignment='top', bbox=props)

    plt.show()


if __name__ == "__main__":
    x = np.array([12.1, 12.5, 12.4, 11.9, 12.5, 12.8, 12.3,
                 12.5, 12.2, 12.9, 13.1, 12.5, 12.8, 12.3])
    show_data(x, 5)
