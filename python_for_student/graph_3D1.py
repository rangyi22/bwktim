#graph_3D1.py
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # 3D graph 관련 module
from matplotlib import cm  # Color map 관련 module

ax = plt.subplot(1,2,1, projection='3d')
x = np.arange(-3,3,0.05) # Grid along the x-axis
y = np.arange(-3,3,0.05) # Grid along the y-axis
X,Y = np.meshgrid(x,y) # Grid on the x-y plane
Z = np.cos(X/2)*np.sin(Y)
ax.plot_surface(X,Y,Z, rstride=1, cstride=1, alpha=1,
                   cmap=cm.coolwarm)
ax.contour(X,Y,Z, zdir='x', offset=-3, cmap=cm.coolwarm)
ax.contour(X,Y,Z, zdir='y', offset=3, cmap=cm.coolwarm)
ax.contour(X,Y,Z, zdir='z', offset=-1, cmap=cm.coolwarm)
ax = plt.subplot(1,2,2, projection='3d')
# Make the grid for a 3D quiver plot
x = y = np.arange(-0.8,1,0.15)
z = np.arange(-0.8,1,0.8)
X,Y,Z = np.meshgrid(x, y, z)
# Make a 3D vector field
U = np.sin(np.pi*X) * np.cos(np.pi*Y) * np.cos(np.pi*Z)
V = -np.cos(np.pi*X) * np.sin(np.pi*Y) * np.cos(np.pi*Z)
W = np.cos(np.pi*X) * np.cos(np.pi*Y) * np.sin(np.pi*Z)
ax.quiver(X,Y,Z, U,V,W, length=0.15)
plt.show()
