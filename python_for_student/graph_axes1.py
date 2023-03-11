#graph_axes1.py
import matplotlib.pyplot as plt

# Given data
x = [-0.1, 0.1, 0.2, 0.4, 0.5, 0.7, 1] 
y = [2, 1, 0, 0.5, -1, 0, 3] 

fig = plt.figure(tight_layout=True)
#plt.rc('font', family='NanumGothic')
plt.subplot2grid((3,4),(0,0), colspan=4)
plt.plot(x,y,'r.')
plt.subplot2grid((3,4),(1,0), rowspan=2, colspan=2)
plt.plot(x,y,'b:')
plt.subplot2grid((3,4),(1,2), colspan=2)
plt.plot(x,y,'k')
plt.subplot2grid((3,4),(2,2))
plt.plot(x,y,'m-x')
plt.subplot2grid((3,4),(2,3))
plt.plot(x,y,'go-.')
#ax6 = plt.subplot2grid((3,3),(2,2))
#ax6.plot(x,y,'^-.')
plt.show()
