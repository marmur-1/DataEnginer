# Сгенерировать выборку с распределением Рэлэя ( https://ru.wikipedia.org/wiki/Распределение_Рэлея ) используя numpy и scipy 
# и построить на основе ее кривую плотности распределения на основе гистограммы из Matplotlib.

import numpy as np
from scipy.stats import rayleigh
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

mean, var, skew, kurt = rayleigh.stats(moments='mvsk')

x = np.arange(0,10,0.2)

ax.grid()
ax.plot(x, rayleigh.cdf(x,scale=0.5),'b', lw=1, alpha=0.9, label='scale=0.5')
ax.plot(x, rayleigh.cdf(x,scale=1),'k', lw=1, alpha=0.9, label='scale=1')
ax.plot(x, rayleigh.cdf(x,scale=2),'g', lw=1, alpha=0.9, label='scale=2')
ax.plot(x, rayleigh.cdf(x,scale=3),'r', lw=1, alpha=0.9, label='scale=3')
ax.plot(x, rayleigh.cdf(x,scale=4),'m', lw=1, alpha=0.9, label='scale=4')
ax.legend(loc='best', frameon=False)

plt.show()