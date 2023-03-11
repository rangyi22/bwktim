#py08p08e_plot3D.py
import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot(1,2,1, projection='3d')
t = np.arange(0, 2.01, 0.01)
pi = np.pi;  pi2t = 2*pi*t
ax.plot3D(t, np.???(pi2t), np.sin(????)) # 그림 P8.8.5
ax.set_xlabel('t'); ax.set_ylabel('y'); ax.set_zlabel('z')
p = lambda t: (t, np.cos(2*pi*t), np.sin(2*pi*t))
T = lambda t: (1, -2*pi*np.sin(2*pi*t), 2*pi*np.cos(2*pi*t))
x1,y1,z1 = p(0.5);  u1,v1,w1 = T(0.5)
x2,y2,z2 = p(1);  u2,v2,w2 = T(1)
ax.quiver(x1,y1,z1,u1,v1,??,length=0.1) #arrow_length_ratio=0.3
ax.quiver(x2,y2,??,u2,v2,w2,length=0.1) #arrow_length_ratio=0.3
plt.show()
