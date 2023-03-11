#graph_contour_quiver.py
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

delta = 0.25 # Grid interval
x = np.arange(-2.5, 2.5, delta)
y = np.arange(-2.5, 2.5, delta)
X,Y = np.meshgrid(x, y)  # Grid 행렬들 (그림 8.18(a)), 표 H.3(1) 참조
Z1 = np.exp(-(X-1)**2 - (Y-1)**2)
Z2 = np.exp(-(X+1)**2 - (Y+1)**2)
Z = Z1-Z2 # 식 (8.1)
plt.subplot(2,2,1)
levels = np.arange(-1, 1, 0.2)
CS = plt.contour(X,Y,Z, levels) # , cmap=cm.gray  그림 8.18(b)
#CB = plt.colorbar(CS, shrink=0.8, extend='both') # colorbar
plt.clabel(CS, fontsize=10);  plt.grid()
plt.title('Simplest default contour with labels')
plt.subplot(2,2,2)
(U,V) = (-2*(X-1)*Z1+2*(X+1)*Z2,-2*(Y-1)*Z1+2*(Y+1)*Z2) # 식 (8.2)
plt.quiver(X,Y, U,V)  # 그림 8.18(c)
plt.grid()
plt.show()
