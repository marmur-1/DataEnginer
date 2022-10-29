# Сгенерировать массивы по функции (x^2 + y^2 - 1)^3 - x^2 y^3 = 0 и построить на основе них график.

# (x^2 + y^2 - 1)^3 - x^2 y^3 = 0 
# (x^2 + y^2 – 1)^3 = x^2y^3.
# x^2 + y^2 – 1 = x^2 / 3^y
# y^2 - x^2 / 3^y + x^2 - 1 = 0

from cmath import exp, log , sqrt, nan
import numpy as np
import matplotlib.pyplot as plt

# fig, ax = plt.subplots(1, 1)

x = np.arange(-1.2,1.2,0.001)

def funcY(x):
    a = 1
    b = -exp((2/3)* log(x).real).real
    c = x**2 - 1

    d = b**2-(4*a*c)

    y1 = nan
    y2 = nan
    if d>0:
        y1 = (-b+(sqrt(d).real))/(2*a)
        y2 = (-b-(sqrt(d).real))/(2*a)
        print('D>0 x='+str(x)+' y1='+str(y1)+' y2='+str(y2))
    elif d==0:
        y1 = y2 = -(b/(2*a))
        print('D=0  x='+str(x)+' y1='+str(y1)+' y2='+str(y2))
    else:
        print('D<0  x='+str(x)+' y1='+str(y1)+' y2='+str(y2))
    return [y1,y2]



plt.grid()
y1 = []
y2 = []
for el in x:
    y = funcY(el)
    y1.append(y[0])
    y2.append(y[1])

plt.plot(x, y1,'b')
plt.plot(x, y2,'r')


plt.show()