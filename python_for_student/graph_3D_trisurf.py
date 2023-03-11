#graph_3D_trisurf.py
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
n_r = 8;  n_a = 24
rs = np.linspace(0.125, 1, n_r) # 중복을 피하기 위해 r=0을 제외한다.
angles = np.linspace(0, 2*np.pi, n_a, endpoint=False) # (24,)
angles = np.repeat(angles[:, np.newaxis], n_r, axis=1) # 24x8
# 극좌표 (r, angles)를 직각좌표 (x, y)로 변환하는데
# 제8행에서 제외했던 r=0(원점)을 넣어주기 위해 여기서 (0,0)을 삽입한다.
x = np.append(0, (rs*np.cos(angles)).flatten()) # (1+24x8=193,)
y = np.append(0, (rs*np.sin(angles)).flatten()) # (1+24x8=193,)
z = np.sin(-x*y)  # (1+24x8=193,)
my_cmap = plt.get_cmap('autumn') # summer
ax.plot_trisurf(x, y, z, linewidth=1, antialiased=True, cmap=my_cmap)
plt.show()
