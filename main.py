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

def DisplaySquare(startX, startY, startZ, direction, col = 'k'):
    x, y = 0, 0
    if direction == "x":
        x = np.meshgrid([startX, startX + 1])
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
    ax.plot_surface(x, y, z, antialiased = False, linewidth = 0, color = col)
    

def DisplayRubiksCube(cubeArray):
    for c in range(0, 6):
        for a in range(0, 3):
            for b in range(0, 3):
                if c == 0:
                    DisplaySquare(a, b, 3, "z", cubeArray[b, a + c * 3])
                elif c == 1:
                    DisplaySquare(0, a, b, "y", cubeArray[b, a + c * 3])
                elif c == 2:
                    DisplaySquare(a, 0, b, "x", cubeArray[b, a + c * 3])
                elif c == 3:
                    DisplaySquare(3, a, b, "y", cubeArray[b, a + c * 3])
                elif c == 4:
                    DisplaySquare(a, 3, b, "x", cubeArray[b, a + c * 3])
                else:
                    DisplaySquare(a, b, 0, "z", cubeArray[b, a + c * 3])

def SpinCube(cubeArray, direction):
    if direction == "U1": #Rotate front 
        

#ax.plot(x, y, z, label = "Kubas lol", zdir = 'z')

cubeArray = np.empty((3, 18), dtype = str)
colorArray =["w", "c", "g", "r" ,"y", "b"]
for a in range(0, 6):
    for x in range(0, 3):
        for y in range(0, 3):
            cubeArray[y, x + a * 3] = colorArray[a]

SpinCube(cubeArray, "M")

DisplayOrientationLines();
DisplayRubiksCube(cubeArray);

ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 5)

plt.show()


