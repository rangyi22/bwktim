#graph_circle.py
import matplotlib.pyplot as plt
import numpy as np

# 반경이 1인 원을 그린다.
ths = np.linspace(0,2*np.pi,201) # Angles in [0,2*pi]
r = 1  # 원의 반경
c=r*np.exp(1j*ths)
xs,ys = np.real(c),np.imag(c) # 복소수 이용해든지 
# xs, ys = r*np.cos(ths), r*np.sin(ths) # 또는 이렇게 해도 마찬가지
plt.subplot(1,2,1)
plt.plot(xs, ys) # 그림 P8.1(a)
plt.title('may looks like an ellipse', fontsize=10)
plt.subplot(1,2,2)
plt.plot(xs, ys)  # 그림 P8.1(b)
plt.axis('     ') # x-축과 y-축의 scale을 똑같이 해, equal 또는 scaled
plt.plot([-1.5,1.5], [0, ?], 'k', linewidth=0.5) # x-축을 그려넣어
plt.plot([?, 0], [-1.2,1.2], 'k', linewidth=0.5) # y-축을 그려넣어
plt.text(0, ?, '?') # 원점에 O를 표시해
plt.title('equal, looks like a circle', fontsize=10)
plt.show()
