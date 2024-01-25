import numpy as np
import matplotlib.pyplot as plt

def scatter_vs(a, b, title, legend_a, legend_b):
	# f, (ax1, ax2) = plt.subplots(ncols=1, nrows=2)
	# ax1.set_title(title_a)
	# ax1.plot(a, 'o')

	# ax2.set_title(title_b)
	# ax2.plot(b, 'o')
	plt.figure()
	plt.title(title)
	plt.plot(a, 'o')
	plt.plot(b, 'o')
	plt.legend([legend_a, legend_b])

	model = np.polyfit(a, b, 1)
	m = model[0]
	t = model[1]
	print(f"Steigung: {m}")
	print(f"Achsenabschnitt: {t}")
	plt.plot(a, m*a + t, "-r")

	plt.show()

if __name__ == "__main__":
	chur = np.array([2,2,4,1,8,7,8,8,10,2,2,4,3,5,5,6,4,7,10,12,12,11,3,4,6,6])
	post = np.array([2,3,4,2,8,8,8,9,10,3,2,4,4,5,6,6,4,8,10,12,13,11,4,4,7,6])
	genf = np.array([4,4,8,6,12,12,8,6,4,4,1,4,5,6,8,8,10,12,8,7,7,7,8,5,7,6])

	scatter_vs(chur, post, "Chur Bahnhof vs. Chur Post", "Bahnhof", "Post")


