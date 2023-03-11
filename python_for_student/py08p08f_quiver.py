#py08p08f_quiver.py
import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot(1,2,1, projection='3d')
x = np.arange(-1.5, 1.6, 0.5)
y = np.arange(-1.5, 1.6, 0.5)
z = np.arange(-1.5, 1.6, 0.5)
X,Y,Z = np.meshgrid(x, y, z)  # Grid 행렬들
R = np.sqrt(X**2 + Y**2 + Z**2) +1e-10
Q = 1;  a = 1
U = Q/a**3*X*(R<=a) + Q/R**3*X*(R>a) # 식 (P8.8f.1)
V = Q/a**3*Y*(R<=a) + Q/R**3*Y*(R>a)
W = Q/a**3*Z*(R<=a) + Q/R**3*Z*(R>a)
ax.set_xlabel('t'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.quiver(X,?,Z, ?,V,W, length=0.5)  # 그림 P8.8.6
plt.show()
