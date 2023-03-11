#py08p06a_contours.py
import matplotlib.pyplot as plt
import numpy as np

f = lambda x: [x[0]**2 + 4*x[1]**2 - 5,
               2*x[0]**2 -2*x[0] -3*x[1] -2.5] # 식 (8.6a.2)
x1 = np.arange(-3,3.05,0.1)
x2 = np.arange(-1.5,1.55,0.1)
X1, X2 = np.meshgrid(x1, x2)
Za,Zb = f([X1,X2])
levels = [ ]
plt.contour(X1, X2,   , levels)  # 그림 P8.6.1
plt.contour(X1,   , Zb,       )  # 그림 P8.6.1
plt.grid()
plt.show()
