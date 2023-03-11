#py08p08c_surface.py
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm  # Color map 관련 module

ax = plt.subplot(1,2,1, projection='3d')
Y, X = np.mgrid[-3:3.1:0.2, -1:5.1:0.2]
Z = (X**2-Y)/4   # 식 (P8.8c.1) 
ax.plot_surface( ,Y,Z, cmap=cm.coolwarm)  # 그림 P8.8.3
ax.contour(X,Y,Z, zdir='z', offset=-1, cmap=cm.coolwarm)
p = [2, 0, 1] # A point on the curved surface
gradf = [4, -1, -4]  # 식 (P8.8c.2)
ax.quiver(p[0], [1],p[2],gradf[0],    [1],gradf[2],length=0.2)
plt.show()
