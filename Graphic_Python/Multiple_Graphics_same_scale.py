
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,1,0.01) 

Y1 = np.sin(2*np.pi*t)
Y2 = np.cos(2*np.pi*2*t)

fig = plt.figure()

ax1 = fig.add_subplot(211)
plt.title('Money on the month')
plt.xlabel('time [s]')
plt.grid(True)

ax2 = fig.add_subplot(212,sharex=ax1)
plt.title('Money on the year')
plt.xlabel('time [s]')
plt.grid(True)

ax1.plot(t,Y1)

ax2.plot(t,Y2)

plt.show()

