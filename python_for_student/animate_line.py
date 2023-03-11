#animate_line.py
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

pi = np.pi  # 원주율
f = lambda t: np.sin(t)  # 그래프 함수 정의
fig, ax = plt.subplots()
tl, tu, yl, yu = 0, 1, -1.2, 1.2  # 그래프 축의 좌/우한과 하/상한 눈금
t, y = [], []
line, = ax.plot(t, y, lw=2) # 그래프 선의 두께(linewidth) 설정
ts = np.linspace(0, tu, 501) # 그래프의 x-값들
def init():
   ax.set_xlim(tl, tu*1.1) # x-축 범위 지정
   ax.set_ylim(yl, yu)     # y-축 범위 지정
   return line, 
def animate(tn):
   ys = f(2*pi*(ts + tn)) # - tn)) 오른쪽으로 이동시키려면 부호를 minus로
   line.set_data(ts, ys) # 그래프의 x-값들 ts와 그에 대한 y값들 ys 지정 
   return line,
ani = FuncAnimation(fig, func=animate, frames=ts, \
                        init_func=init, interval=10)
plt.show()
