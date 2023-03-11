#graph_3D.py
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # 3D graph 관련 module
from matplotlib import cm  # Color map 관련 module

x = np.arange(-5,5,0.25) # Grid along the x-axis
y = np.arange(-5,5,0.25) # Grid along the y-axis
X,Y = np.meshgrid(x,y) # Grid on the x-y plane
Z = X**2 + Y**2
ax = plt.subplot(2,2,1, projection='3d')
ax.plot_surface(X,Y,Z, rstride=1, cstride=4, cmap=cm.viridis)
 # <https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html> 
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.set_title('plot_surface(X,Y,Z)', fontsize=10)
ax = plt.subplot(2,2,2, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=4, cstride=1)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.set_title('plot_wireframe(X, Y, Z)', fontsize=10)

ax = plt.subplot(2,2,3, projection='3d')
zline = np.linspace(0, 15, 1001)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.set_title('plot3D(xline, yline, zline)', fontsize=10)
ax = plt.subplot(2,2,4, projection='3d')
N = 100 # Number of 3 random sequences to be generated
xs = 23 + 9*np.random.rand(N)
ys = 100*np.random.rand(N)
zs = -50 + 25*np.random.rand(N)
ax.scatter(xs,ys,zs, c='b', marker='o')
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.set_title('scatter(xs,ys,zs)', fontsize=10)

plt.show()
