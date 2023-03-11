#graph_stem.py
import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1,2,1)
x0, xf, N = (0.1, 2*np.pi, 20) 
x = np.linspace(x0, xf, N)
y = np.sin(x)
plt.stem(x, y) # 그림 8.6(a)
plt.subplot(1,2,2)
plt.step(x, y) # 그림 8.6(b)
plt.plot([x0,xf],[0,0],'k') # x-축을 흑색(black)으로 그린다.
plt.show()
