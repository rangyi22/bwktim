#animate_dot_on_line.py
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

pi = np.pi  # 원주율
f = lambda x: np.sin(x) # 그래프 함수 정의
xl, xu, yl, yu = 0, 2*pi, -1.1, 1.1 # 그래프축의 좌/우한과 하/상한
fig, ax = plt.subplots()
x, y = [], []
line, = ax.plot(x, y, 'ro', markersize=4) # 빨갛고, 크기가 4인 원모양 점
xs = np.linspace(0, xu, 81) # 그래프의 x-값들
def init():
   ax.set_xlim(xl, xu*1.1)
   ax.set_ylim(yl, yu)
   line, = ax.plot(xs, f(xs), 'b:')
   return line, 
def animate(xn):
   x.append(xn) 
   y.append(f(xn)) 
   line.set_data(x, y)
   return line,
ani = FuncAnimation(fig, func=animate, frames=xs, \
                        init_func=init, interval=10)
#ani.save('animation_dot_on_line.gif', writer='imagemagick', fps=30)
plt.show()
