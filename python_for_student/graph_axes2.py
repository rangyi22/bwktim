#graph_axes2.py
import matplotlib.pyplot as plt

# Given data
x = [-0.1, 0.1, 0.2, 0.4, 0.5, 0.7, 1] 
y = [2, 1, 0, 0.5, -1, 0, 3] 

fig = plt.figure(tight_layout=True)
#plt.rc('font', family='NanumGothic')
plt.subplot(2,3,1)
plt.plot(x,y,'r.')
plt.subplot(2,3,2)
plt.plot(x,y,'b:')
plt.subplot(2,3,3)
plt.plot(x,y,'k')
plt.subplot(2,3,4)
plt.plot(x,y,'m-x')
plt.subplot(2,3,5)
plt.plot(x,y,'go-.')
plt.subplot(2,3,6)
plt.plot(x,y,'y^')
plt.show()
