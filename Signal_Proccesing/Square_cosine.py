# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


# Frecuency

T = 2*np.pi # T = 2pi

wo = 2*np.pi/T # wo = 1

# time

t = np.arange(0,10,0.1) # time "t"

# cos and cos²

cosine = np.cos(2*np.pi*1/T*t)  # cos(wo.t)

square_cosine = cosine * cosine  # cos²(t) = cos(t) * cos(t) 

# Graphics

plt.subplot(3, 1, 1)
plt.plot(t, cosine, 'o-')
plt.title('Fourier Series')
plt.ylabel('Cos(t)')

plt.subplot(3, 1, 2)
plt.plot(t, cosine, 'o-')
plt.ylabel('Cos(t)')

plt.subplot(3, 1, 3)
plt.plot(t, square_cosine, '.-')
plt.xlabel('time (s)')
plt.ylabel('Cos(t)*Cos(t)')


plt.grid(True)

plt.show()
