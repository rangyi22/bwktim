#graph_polar.py
import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1,2,1, projection='polar')
th = np.linspace(0,2*np.pi,401)
r1 = abs(np.sin(th));   r2 = abs(np.sin(2*th))
plt.polar(th, r1, color='blue', lw=1, label='Polar plot A')
plt.plot(th, r2, color='red', ls='--', lw=2, label='Polar plot B')
# lw: linewidth, ls=linestyle
plt.legend()
plt.subplot(1,2,2, projection='polar')
r = np.arange(0, 2, 0.01)
th1 = np.pi*r ;   th2 = 2*np.pi*r
plt.polar(th1, r, color='blue', lw=1, label='Polar plot A')
plt.plot(th2, r, color='red', ls='--', lw=2, label='Polar plot B')
plt.legend()
plt.show()
