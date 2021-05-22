import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

def DisplayOrientationLines():
    ax.quiver(0, 0, 0, 1, 0, 0, color = 'r', length = 5, arrow_length_ratio = 0.01)
    ax.quiver(0, 0, 0, 0, 1, 0, color = 'g', length = 5, arrow_length_ratio = 0.01)
    ax.quiver(0, 0, 0, 0, 0, 1, color = 'b', length = 5, arrow_length_ratio = 0.01)

x = np.linspace(0, 10, 2)
y = np.linspace(0, 10, 2)
z = 0

#ax.plot(x, y, z, label = "Kubas lol", zdir = 'z')

DisplayOrientationLines();


ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 5)

plt.show()


