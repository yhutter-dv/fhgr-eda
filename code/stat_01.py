from show_data import show_data
import numpy as np

if __name__ == "__main__":
    temp_chur_bahnhof = np.array([2,2,4,1,8,7,8,8,10,2,2,4,3,5,5,6,4,7,10,12,12,11,3,4,6,6])
    show_data(temp_chur_bahnhof, number_of_bins=5, title="Temperature at Railroad Station Chur", y_axis_title = "Temperatur in Celsius")

    number_of_customers = np.array([12,22,14,8,13,109,132,99,117,14,21,8,7,11,12,111,112,100,18])
    show_data(number_of_customers, number_of_bins=5, title="Number of Customers at Railroad Station Chur", y_axis_title = "Number of Customers per Day")
