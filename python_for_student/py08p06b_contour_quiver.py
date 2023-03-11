#py08p06b_contour_quiver.py
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,4,0.2); y=np.arange(0,4,0.2)
X, Y = np.meshgrid(x, y)
Z1 = 5*np.cos(X-2.5)*np.cos(Y-2.9)
Z2 = X**4-12*X**2-4*X +Y**4-16*Y**2-5*Y
Z = Z1-Z2  # 식 (P8.6b.1)
plt.subplot(2,2,1)
levels = np.arange(0, 120, 10)
CS = plt.contour(X, Y, Z,       )  # 그림 P8.6(a)
plt.clabel(CS, fontsize=10)
plt.subplot(2,2,2)
# Gradient 함수 식 (P8.6b.2)
(gradZx,gradZy)=(-5*np.sin(X-2.5)*np.cos(Y-2.9)-4*X**3+24*X +4,
                 -5*np.cos(X-2.5)*np.sin(Y-2.9)-4*Y**3+32*Y +5) 
plt.quiver( ,Y, gradZx,      )  # 그림 P8.6(b)
plt.show()
