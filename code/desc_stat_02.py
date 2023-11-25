import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    schuhgroesse = np.array([42, 44, 45, 39, 40, 42, 42, 38, 44, 46])
    koerperlaenge = np.array(
        [1.8, 1.88, 1.92, 1.67, 1.74, 1.81, 1.78, 1.55, 1.86, 1.91])

    plt.figure()
    plt.plot(schuhgroesse, koerperlaenge, 'o')
    plt.xlabel('Schuhgrösse')
    plt.ylabel('Körperlänge')
    plt.grid()

    rho = np.corrcoef(schuhgroesse, koerperlaenge)
    print(f"Correlation is: {rho}")

    bestimmtheitsmass = rho**2
    print(f"Bestimmtheitsmass is: {bestimmtheitsmass}")

    # 1 means we search for a linear model
    model = np.polyfit(schuhgroesse, koerperlaenge, 1)

    # t = offset
    m, t = model

    plt.plot(schuhgroesse, schuhgroesse * m + t, 'r')

    plt.show()
