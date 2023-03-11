#animate_3Dline.py
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as ax3D  # 3D graph axes
from matplotlib.animation import FuncAnimation
import numpy as np

pi = np.pi  # 원주율
fig = plt.figure()
ax = ax3D.Axes3D(fig)
tl, tu, yl, yu, zl, zu = 0, 2, -1.2, 1.2, -1.2, 1.2
t, y, z = [], [], []
ax.set_xlabel('t'); ax.set_ylabel('y'); ax.set_zlabel('z')
line, = ax.plot3D(t, y, z, lw=2)
ts = np.linspace(0, tu, 200) # time vector

def init():
   ax.set_xlim(tl, tu*1.1)
   ax.set_ylim(yl, yu)
   ax.set_zlim(zl, zu)
   return line, # 출력인자가 tuple이 되도록

def animate(tn):
   ys = np.sin(2*pi*(ts + tn)) 
   zs = np.sin(2*pi*(ts + tn)) 
   ax.cla()  # 기존의 그래프를 지워
   ax.plot3D([0,ts[-1] *1.1], [0,0], [0,0],  'k', lw=1) #t-축 도시
   ax.plot3D(ts, np.zeros_like(ts), ??, lw=2)
   line, = ax.plot3D(ts, ??, np.zeros_like(ts), lw=2)
   return line, # 출력인자가 tuple이 되도록

ani = FuncAnimation(fig, animate, frames=ts, interval=10, \
                    init_func=init) 
plt.show()
