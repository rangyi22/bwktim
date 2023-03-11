#py08p04_scatter_polar.py
import matplotlib.pyplot as plt
import numpy as np

N = 150;  r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 10 * r**2;  colors = theta
fig = plt.figure(tight_layout=True)
ax1 = plt.subplot(1,3,1, projection='polar')
ax1.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.2)
ax2 = plt.subplot(1,3,2, polar=True)
ax2.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.6)
ax2.set_rorigin(-1)
ax2.set_theta_zero_location('W', offset=45) 
ax3 = plt.subplot(1,3,3, polar=True)
ax3.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=1)
ax3.set_thetamin(45);  ax3.set_thetamax(135))
plt.show()
