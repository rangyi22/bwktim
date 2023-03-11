#py08p08d_surface.py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(tight_layout=True)
ax = plt.subplot(1,2,1, projection='3d')
Y, X = np.mgrid[-2:2.05:0.1, -2:2.05:0.1]
Q=1;  d=2;  EPS=1e-10
R1 = np.sqrt(X**2+(Y-d/2)**2) +EPS
R2 = np.sqrt(X**2+(Y+d/2)**2) +EPS 
Z = Q/R1 - Q/R2  # 식 (P8.8b.1)
ax.plot_surface(X,Y, ) #rstride=2,cstride=2)  # 그림 8.8.4(a)
ax.contour(X, ,Z, zdir=' ', offset=-1/EPS) # 그림 P8.8.4(a)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax = plt.subplot(1,2,2)
Ex = X/R1**3 - X/R2**3
Ey = (Y-d/2)/R1**3 - (Y+d/2)/R2**3  # 식 (P8.8b.2)
Ex = np.sign(Ex)*(1-np.exp(-np.abs(Ex))) # 마사지를 위한 포화
Ey = np.sign(Ey)*(1-np.exp(-np.abs(Ey)))
ax.quiver(X, ,   ,Ey)  # 그림 P8.8.4(b)
ax.plot(0,-1,'bo', 0,1,'ro')
ax.axis('equal')
plt.show()
