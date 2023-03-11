#graph_linedot.py
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(tight_layout=True) # 그림창(canva) 생성
f = lambda t: np.exp(-t)*np.cos(2*np.pi*t) # 도시할 함수
t1 = np.arange(0, 2, 0.1) # 0~2(미만), 0.1 간격의 (듬성듬성한) 수열
t2 = np.arange(0, 2, 0.01) # 0~2(미만), 0.01 간격의 (촘촘한) 수열
plt.subplot(2,2,1)
plt.plot(t1, f(t1), 'o', markersize=4) # (청색) 원형 점 그래프
plt.title('Plot 1' , fontsize=10)
plt.subplot(2,2,2)
plt.plot(t2, f(t2), '-') # (청색) 실선(solid line) 그래프
plt.title('Plot 2' , fontsize=10)
plt.subplot(2,1,2)
plt.plot(t1, f(t1), 'o', label='f(t1)') # (청색) 원형 점 그래프
plt.plot(t2, f(t2), '-', label='f(t2)') # 실선 그래프
plt.xlabel('time t[s]');  
plt.ylabel('f(t)') 
plt.title('Plot 3' , fontsize=10) 
plt.legend()
plt.show()
