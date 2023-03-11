#animate_pendulum2.py
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G, L1, M1, L2, M2 = 9.8, 1, 1, 1, 1

def dxdt(x, t):
   th1, w1, th2, w2 = x 
   s1, s2, s12 = np.sin([th1, th2, th1-th2])
   c12 = np.cos(th1-th2)
   dx = np.zeros_like(x)
   dx[0], dx[2] = w1, w2
   A = [[L1*(M1+M2), L2*M2*c12], [L1*M2*c12, L2*M2]] # 식 (P9.14.3)
   b = [-L2*M2*s12*w2**2 -G*(M1+M2)*s1, L1*M2*s12*w1**2 -G*M2*s2]
   dx[1], dx[3] = np.linalg.solve(A,b)
   return dx

dt = 0.05
t = np.arange(0, 20, dt) # time vector
th1, w1, th2, w2 = 120, 0, -10, 0
x0 = np.radians([th1, w1, th2, w2]) # Initial values
# To solve the ODE
x = odeint(dxdt, x0, t)
x1 = L1*np.sin(x[:,?])
y1 = -L1*np.cos(x[?,0])
x2 = L2*np.sin(x[:,?]) + x1
y2 = -L2*np.cos(x[?,2]) + y1
fig = plt.figure()
ax = plt.subplot(1,2,1, xlim=(-2, 2), ylim=(-2, 2)) ax.set_aspect('equal')
line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def animate(i):
   xx = [0, x1[i], x2[i]]
   yy = [0, y1[i], y2[i]]
   line.set_data(xx, yy)
   time_text.set_text(time_template %(i*dt))
   return line, time_text

ani = FuncAnimation(fig, animate, range(1,len(x)), interval=10) plt.show()
