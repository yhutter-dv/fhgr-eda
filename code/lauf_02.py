
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
t_min = np.array([[2, 3, 3, 3, 2],
                 [3, 3, 3, 3, 3],
                 [2, 2, 3, 3, 3],
                 [3, 3, 3, 3, 3],
                 [2, 3, 2, 2, 3],
                 [3, 3, 3, 3, 2],
                 [2, 2, 3, 3, 2]])


t_sec = np.array([[59, 12, 2, 2, 51],
                 [2, 1, 1, 1, 1],
                 [57, 57, 0, 2, 0],
                 [4, 1, 0, 0, 2],
                 [58, 0, 58, 59, 11],
                 [0, 12, 2, 3, 51],
                 [56, 57, 1, 1, 59]])


t_sec_total = 60 * t_min + t_sec
velocity_km_h = 1000 / t_sec_total * 3.6


names = ["Urs Meier", "Adrian Lippuner", "Corsin Gmüer", "Ralf Münsing",
         "Alexander Schnell", "Rainer Uebel", "Sebastian Frisch"]

"""
Für jeden Läufer sollen die Zeitintervalle auf der Webseite grafisch dargestellt werden. Schreiben Sie ein Skript und erzeugen Sie mit matplotlib für jeden Läufer einen Bar-Plot mit den gemessenen Zeitintervallen und speichern Sie diesen mit einem aussagekräftigen Namen ab. Verwenden Sie eine FOR-Schleife.
"""

for runner in range(7):
    plt.figure(runner)
    name = names[runner]
    plt.axis([0, 5, 0, 250])
    plt.xlabel("Distance travelled in kilometer")
    plt.ylabel("Time in Seconds")
    plt.title(f"Runner {name}")
    plt.bar(x - 0.5, t_sec_total[runner], 1, edgecolor=(0, 0, 0))
    plt.savefig(f"./images/{name}_timeinterval.png")


"""
Berechnen Sie für jeden Läufer die mittleren Geschwindigkeiten (in km/h) in den Streckenabschnitten. Schreiben Sie ein Skript und erzeugen Sie mit matplotlib für jede Läufer einen Linien-Plot mit den berechneten Geschwindigkeiten und speichern Sie diesen mit einem aussagekräftigen Namen ab. Stellen Sie automatisch die Skalierung der
Geschwindigkeitsachse so ein, dass das Geschwindigkeitsprofil sehr gut zu erkennen ist. Verwenden Sie eine FOR-Schleife.
"""
plt.figure(8)
for runner in range(7):
    plt.plot(x - 0.5, velocity_km_h[runner], "o-")
    plt.axis([0.5, 4.5, 18, 21.5])
    plt.xlabel("Distance in kilometers")
    plt.ylabel("Velocity in kilometers per hour")
    plt.title("Velocities of Runners")
    plt.legend(names)
    plt.grid()
plt.savefig("./images/lauf_02_velocity.png")
