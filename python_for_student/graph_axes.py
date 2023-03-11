#graph_axes.py
import matplotlib.pyplot as plt
x = [-0.1, 0.1, 0.2, 0.4, 0.5, 0.7, 1] # 주어진 data
y = [2, 1, 0, 0.5, -1, 0, 3] 
fig = plt.figure(tight_layout=True, figsize=(6.4, 4.8))
ax1 = plt.subplot2grid((3,4),(0,0), colspan=4)
ax1.plot(x,y,'r.') # 그림 8.1(a)
ax2 = plt.subplot2grid((3,4),(1,0), rowspan=2, colspan=2)
ax2.plot(x,y,'b:') # 그림 8.1(b)
ax3 = plt.subplot2grid((3,4),(1,2), colspan=2)
ax3.plot(x,y,'k') # 그림 8.1(c)
ax4 = plt.subplot2grid((3,4),(2,2))
ax4.plot(x,y,'m-x') # 그림 8.1(d)
ax5 = plt.subplot2grid((3,4),(2,3))
ax5.plot(x,y,'go-.') # 그림 8.1(e)
ax5.axis('equal') # x-축과 y-축의 scale을 똑같이 해
#ax5.set(xlim=(-1, 1.5), ylim=(-1,3))
#plt.xlim([-1, 1.5]), plt.ylim([-1,3])
# ax가 싫으면 subplot 문의 ax=을 지우고, 다른 ax=은 plt로 대체하되
# 각 축의 범위를 제한하는 문장인 제17행은 제18행과 같이 바꿔준다.
plt.show()
