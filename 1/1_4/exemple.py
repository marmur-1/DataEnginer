import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(-10,10,0.1)
# y = np.exp(np.arange(-10,10,0.1))

# plt.scatter(x,y) #график точек
# plt.plot(x,y) #график линий
# plt.grid()
# plt.show()


import time
from IPython import display
for k in range(-50,50):
    x = np.arange(-10,10)
    y = np.arange(-10,10) * k
    plt.plot(x,y)
    display.display(plt.gcf())
    display.clear_output(wait=True)
    time.sleep(1)