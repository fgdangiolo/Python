
import numpy as np
import matplotlib.pyplot as plt


def v(t):
    return np.sin(2*np.pi*t)

t = np.arange(0.0, 6, 0.01)

plt.plot(t, v(t), 'r')

plt.title('Amplitud vs Frecuencia')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')

plt.grid(True)

plt.show()
