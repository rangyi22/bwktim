#py09p17_curvefit.py
import numpy as np
from scipy import optimize as opt
import matplotlib.pyplot as plt

np.random.seed(0) # Seed the random number generator
N = 201  # Number of data points
xdata = np.linspace(0, 6, num=N)
noise = np.random.normal(size=N)
ydata = 10*np.exp(-((xdata-3)/1)**2) + noise
g=lambda x,a,b,c: a*np.exp(-((x-b)/c)**2) # Model function
po, po_cov = opt.curve_fit(g, xdata, ydata)
ao, bo, co = po  # a와 b의 추정치
print(f'ao={ao:9.4f}, bo={bo:9.4f}, co={co:9.4f} with N={N:5d}')
plt.scatter(xdata, ydata, s=6, label='Data', color='red')
plt.plot(xdata, g(xdata, ao, bo, co), label='Fitted function')
plt.legend(loc='best')
plt.show()
