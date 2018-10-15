
import numpy as np
import matplotlib.pyplot as plt


def v(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 7.0, 0.1)
t2 = np.arange(0.0, 7.0, 0.01)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, v(t1), 'bo', t2, v(t2), 'k')
plt.ylabel('Velocidad [m/s]')


plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.grid(True)
plt.xlabel('Tiempo [s]')
plt.ylabel('Desplazamiento [m]')

plt.show()
