import numpy as np


def vector_length(x):
    a = x ** 2
    b = sum(a)
    c = np.sqrt(b)
    return c


if __name__ == "__main__":
    a = np.array([1, 2])
    b = np.array([-1, 0])
    c = np.array([1, 0.5, -1])
    d = np.array([0, 1, 1])
    e = np.array([0, 1, 1.5, -0.5, 0])
    f = np.array([1, -1, 2, 0, 0])

    print(vector_length(a))
