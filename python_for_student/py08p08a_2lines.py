#py08p08a_2lines.py
import matplotlib.pyplot as plt
import numpy as np

p1, p2, p, d = [2,4,3], [2,0,0], [2,4,0], [0,1,0]
ax = plt.subplot(1,2,1, projection='3d')
t = [0, 5]
# 점 P2를 지나며 방향벡터가 d인 직선상의 두 점을 잡는다.
p2_0 = [p2n + dn*t[0] for p2n,dn in zip(p2,d)]
p2_1 = [p2n + dn*t[1] for p2n,dn in zip(p2,d)]
ax.plot3D([p2_0[0],p2_1[0]],[p2_0[ ],p2_1[1]],[p2_0[2],p2_1[ ]])                 
ax.plot3D([p1[0],p[0]], [p1[1],p[ ]], [p1[ ],p[2]])
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.text(2,4,3, r'$P_1$(2,4,3)', fontsize=10)
ax.text(2,0,0, r'$P_2$(2,0,0)', fontsize=10)
ax.text(2,4,0, r'P(2,4,0)', fontsize=10)
plt.show()
