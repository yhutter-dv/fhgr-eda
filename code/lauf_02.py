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

	km_h = np.round(1000 / seconds_total * 3.6, 2)

	seconds_total_sum = seconds_total.cumsum(1)

	for i, name in enumerate(names):
		plt.figure()
		plt.title(name),
		plt.axis([0, 5, 0, 200])
		plt.xlabel("Anzahl Kilometer")
		plt.ylabel("Zeitinterval in Sekunden")
		plt.bar(km - 0.5, seconds_total[i], width=1, edgecolor=(0, 0, 0))
		plt.savefig(f"./images/{name}_Zwischenzeit.png")

	for i, name in enumerate(names):
		plt.figure()
		plt.title(name),
		plt.axis([0, 5, 17, 22])
		plt.xlabel("Anzahl Kilometer")
		plt.ylabel("Mittlere Geschwindigkeit in km/h")
		plt.plot(km - 0.5, km_h[i], "ro-")
		plt.savefig(f"./images/{name}_Mittlere_Geschwindigkeit.png")

	plt.figure()
	plt.title("Zwischenzeiten aller Läufer")
	plt.xlabel("Anzahl Kilometer")
	plt.ylabel("Zwischenzeit in Minuten aufsummiert")
	plt.axis([-1, 6, -1, 17])
	for i, name in enumerate(names):
		plt.plot(np.append(0, km), np.append(0, seconds_total_sum[i] / 60.0), "o-")

	plt.legend(names, loc="center left")
	plt.grid(visible=True)
	plt.savefig(f"./images/Zwischenzeiten_Läufer_aufsummiert.png")

	plt.figure()
	plt.title("Zwischenzeiten aller Läufer")
	plt.xlabel("Anzahl Kilometer")
	plt.ylabel("Durchschnittsgeschwindigkeit in km/h")
	plt.axis([0, 5, 18.5, 21.5])
	print(km_h)
	for i, name in enumerate(names):
		plt.plot(km - 0.5, km_h[i], "o-")
	plt.legend(names, loc="center left")
	plt.grid(visible=True)
	plt.savefig(f"./images/Geschwindigkeiten_Läufer.png")






