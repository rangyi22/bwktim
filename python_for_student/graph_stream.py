#graph_stream.py
import matplotlib.pyplot as plt
import numpy as np

Y,X = np.mgrid[0:2:0.2, 0:2:0.2] # 부록 H의 표 H.3(2) 참조
U = 2*X;  V = -2*Y   # Stream의 x-성분과 y-성분
speed = np.sqrt(U**2 + V**2)
strm = plt.streamplot(X,Y, U,V, color=speed, cmap='autumn')
plt.colorbar(strm.lines)
plt.title('Stream plot with varying color')
plt.show()
