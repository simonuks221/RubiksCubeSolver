import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

def DisplayOrientationLines():
    ax.quiver(0, 0, 0, 1, 0, 0, color = 'r', length = 5, arrow_length_ratio = 0.01)
    ax.quiver(0, 0, 0, 0, 1, 0, color = 'g', length = 5, arrow_length_ratio = 0.01)
    ax.quiver(0, 0, 0, 0, 0, 1, color = 'b', length = 5, arrow_length_ratio = 0.01)
    ax.text(4.5, 0, 0, "X", (1, 0, 0), color = 'r')
    ax.text(0, 4.5, 0, "Y", (0, 1, 0), color = 'g')
    ax.text(0, 0, 4.5, "Z", (0, 0, 1), color = 'b')

def DisplaySquare(startX, startY, startZ, direction):
    x, y = 0, 0
    if direction == "x":
        y = np.meshgrid([startY, startY])
        z = np.array([[startZ],[startZ + 1]])
    elif direction == "y":
        x = np.meshgrid([startX, startX])
        y = np.meshgrid([startY, startY + 1])
        z = np.array([[startZ],[startZ + 1]])
    elif direction == "z":
        x = np.array([[startX, startX], [startX + 1, startX + 1]])
        y = np.array([[startY, startY + 1], [startY, startY + 1]])
        z = np.array([[startZ],[startZ]])
    ax.plot_surface(x, y, z, antialiased = False, linewidth = 0, color = 'r')
    

def DisplayRubiksCube():
    x = [0,3, 5]
    y = [0, 1, 3]

    print(x)

    xx = np.meshgrid(x)
    yy = np.meshgrid(y)
    zz = np.array([[3], [5]])
    
    for a in range(1, 4):
        for b in range(1, 4):  
            DisplaySquare(a, 1, b, "x")
            DisplaySquare(a, 4, b, "x")
            DisplaySquare(1, a, b, "y")
            DisplaySquare(4, a, b, "y")
            DisplaySquare(a, b, 1, "z")
            DisplaySquare(a, b, 4, "z")
            



#ax.plot(x, y, z, label = "Kubas lol", zdir = 'z')

DisplayOrientationLines();
DisplayRubiksCube();

ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 5)

plt.show()


