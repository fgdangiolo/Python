# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def v(t):
    return np.sin(2*np.pi*t)

# T and wo

T = 2*np.pi # T = 2pi

wo = 2*np.pi/T # wo = 1

# Variable "t"

t = np.arange(0,10,0.1)

# cos y cos²

cos = np.cos(2*np.pi*1/T*t)  # cos(wo.t)

square_cos = cos * cos  # cos²(t) = cos(t) * cos(t) 

# Gráfico de coseno cuadrado

plt.subplot(3, 1, 1)
plt.plot(t, cos, 'o-')
plt.title('Signals')
plt.ylabel('Cos(t)')

plt.subplot(3, 1, 2)
plt.plot(t, cos, 'o-')
plt.ylabel('Cos(t)')

plt.subplot(3, 1, 3)
plt.plot(t, square_cos, '.-')
plt.xlabel('time (s)')
plt.ylabel('Cos(t)*Cos(t)')


plt.grid(True)

plt.show()
