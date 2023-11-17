import numpy as np
import matplotlib.pyplot as plt

"""
Übertragen Sie die Messwerte in 1D-Arrays in Python. Es hat sich vermutlich ein Datenübertragungs- oder Mess-Fehler eingeschlichen. Korrigieren Sie diesen mit Hilfe einer sinnvollen
Annahme.
"""
distance = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
time_min = np.array([2, 3, 3, 3, 3, 3, 3, 3, 3, 3])
time_sec = np.array([58, 12, 1, 22, 11, 38, 28, 21, 19, 35])
time_sec_total = 60 * time_min + time_sec
time_sec_accumulated = time_sec_total.cumsum()

"""
Erzeugen Sie mit matplotlib den exakt selben, wie untenstehenden, Bar-Plot mit
den Zeitintervallen
"""
plt.figure(1)
plt.bar(distance - 0.5, time_sec_total, edgecolor=(0, 0, 0), width=1)
plt.axis([0, 10, 0, 250])
plt.xticks(distance)
plt.xlabel("Distance travelled in kilometer")
plt.ylabel("Time in Seconds")
plt.title("Alexander Schnell")
plt.savefig("./images/lauf_01_bar.png")


"""
Erzeugen Sie mit matplotlib den exakt selben, wie untenstehenden, Linien-Plot
mit den aufsummierten Zwischenzeiten.
"""
plt.figure(2)
plt.axis([0, 10, 0, 2050])
plt.xticks(distance)
plt.plot(distance, time_sec_accumulated, "ro-")
plt.xlabel("Distance in kilometer")
plt.ylabel("Time in Seconds")
plt.title("Alexander Schnell")
plt.savefig("./images/lauf_02_line.png")

"""
Berechnen Sie die mittleren Geschwindigkeiten auf jedem Streckenabschnitt. Stellen Sie diese als Linienplot dar. Wählen Sie die Skalierung der Achsen geeignet. Speichern Sie die
Grafik als png-file ab.
"""

plt.figure(3)
distance_m = distance * 1000
velocities_m_per_second = distance_m / time_sec_accumulated
plt.axis([0, 10500, velocities_m_per_second.min() - 0.2 , velocities_m_per_second.max() + 0.2])
plt.xticks(distance_m)
plt.plot(distance_m, velocities_m_per_second, "ro-")
plt.xlabel("Distance in meters")
plt.ylabel("Velocity in meter per seconds")
plt.title("Alexander Schnell")
plt.savefig("./images/lauf_02_line_velocity.png")


"""
Erzeugen Sie Histogramm mit 6 bins und speichern dieses ab.
"""
plt.figure(4)
plt.hist(velocities_m_per_second, bins=6, edgecolor=(0, 0, 0))
plt.savefig("./images/lauf_02_hist_velocity.png")
plt.show()
