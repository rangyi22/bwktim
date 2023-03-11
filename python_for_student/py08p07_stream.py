#py08p07_stream.py
import matplotlib.pyplot as plt
import numpy as np

Y, X = np.mgrid[-2:2.1:0.25, -5:5.1:0.5]  # Grid arrays
U = 1-(X**2-Y**2)/((X**2+Y**2)**2 + 1e-10)
V = -2*X*Y/((X**2+Y**2)**2 + 1e-10)  # 식 (P8.7.1)
speed = np.sqrt(U**  +  **2) # 식 (P8.7.2)
# 속력을 선의 색깔과 두께에 실어서 (과장되게) 표시하기 위해
speed = np.clip(speed, 0.5, 3) # 0.5~3 범위로 제한시킨다.
lw = speed/speed.max() * 3 
strm = plt.streamplot(X, ,  ,V, color=speed, linewidth=lw)
plt.colorbar(strm.lines)
ths = np.arange(0, 6.29, 0.1) # 0~2pi
plt.plot(np.   (ths), np.sin(   ),'b:') # 단위원을 그린다.
plt.axis('equal')
plt.show()
