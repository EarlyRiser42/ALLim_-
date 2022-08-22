from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-1, 1, step = 0.1)

plt.plot(x, x + np.sin(x) - 1, label = 'A=1')
plt.plot(x, 10*x+np.sin(x)-1, label = 'A=10')
plt.plot(x, 20*x+np.sin(x)-1, label = 'A=20')

plt.hlines(0, -1, 1, color='black', linestyle='-', linewidth=1)
plt.vlines(0, -20, 20, color='black', linestyle='-', linewidth=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()