
import numpy as np
from math import cos, sin
import matplotlib.pyplot as plt


def nextPoint(point):

    a, b, c, d = 1.0, 0.5, -0.4, 0.4

    x = point[0]
    y = point[1]
    return (sin(x),
            cos(y))


def iterate(f, x):
    while True:
        yield x
        x = f(x)


for startPoint in np.random.uniform(0, 1, (50, 2)):
    points = iterate(nextPoint, startPoint)
    plt.plot([points.next() for i in range(50)])

plt.xlim([0, 1])
plt.ylim([0, 1])
plt.show()
