#graph_log.py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(tight_layout=True) # create a canvas for plotting
plt.subplot(2,2,1)
x = np.logspace(-1,1,1001) # [10**-1, 10**1]=[0.1,10]구간내 1001개 점
y = abs(1j*x/(1+1j*x))  # x에 대한 어떤 복소수함수의 절대값(크기)
plt.plot(x, y)  # 그림 8.16(a)
plt.grid(True, which="both")  # Display grid
plt.subplot(2,2,2)
plt.semilogx(x, y)  # 그림 8.16(b)
plt.grid(True, which="both")  # Display grid
plt.subplot(2,2,3)
plt.semilogy(x, y)  # 그림 8.16(c)
plt.grid(True, which="both")  # Display grid
plt.subplot(2,2,4)
plt.loglog(x, y) # 그림 8.16(d)
plt.grid(True, which="both")  # Display grid
plt.show()
