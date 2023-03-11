#py08p08b_2planes.py
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # 3D graph 관련 module

planes = [[2, -3, 4, 1], # 평면방정식들의 계수 벡터
          [1, -1, -1, 5]]
p1 = [-14,-15,-4] # 점 P1의 3D 직각 좌표
d = [7, 6, 1] # 방향벡터
ax = plt.subplot(1,2,2, projection='3d')
Y, X = np.mgrid[-20:20.1:1, -10:10.1:0.5]
for i in range(0,len(planes)):
   a, b, c, r = planes[i]
   if c==0:  continue
   Z = (r - a*X - b*Y)/c
   ax.plot_surface( ,Y,Z, alpha=0.6)  
ax.quiver(p1[0],p1[ ],p1[2], d[0], [1],d[2], \
          length=4, arrow_length_ratio=0.1)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
plt.show()
