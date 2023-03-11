#py08p05_errorbar.py
# plots errorbar graphs.
import matplotlib.pyplot as plt
import numpy as np
# x에 대해 측정된 두 개의 데이터 y1과 y2 
x = np.arange(0, 4, 0.25)
y1 = 1 - np.exp(-x)
y2 = 1.1 - np.exp(-x)
# y1과 y2가 가진 오차크기의 최대치 
y1err = 0.1*np.sqrt(y1) # Error bound for y1
y2err = 0.1*np.sqrt(y2) # Error bound for y2 
fig = plt.figure(tight_layout=True)
plt.subplot(1,2,1) 
plt.errorbar(x,   , yerr=y1err) # fmt: Format specifier
plt.errorbar(x, y2, yerr=     )  # 그림 P8.5(a)
plt.title('Vertical errorbar A', fontsize=10)
plt.subplot(1,2,2)
plt.errorbar(x, y1, yerr=     , errorevery=( ,2)) # 그림 P8.5(b)
plt.errorbar(x,   , yerr=y2err, errorevery=(1, )) plt.title('Vertical errorbar B', fontsize=10)
plt.show()
