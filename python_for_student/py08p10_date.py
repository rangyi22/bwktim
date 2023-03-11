#py08p10_date.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
import 한글_font # 한글을 그래프에 넣기 위한 module 가져오기

fname= 'D:/Python/corona_Korea.csv' # 코로나 확진자수파일 (문제 7.32)
df = pd.read_csv(fname, header=None) # A Pandas dataframe
#index_col=None, usecols=None)
t = df.iloc[:][0] # 제 0(첫 번째) 열: 날짜 (datetime object들)
y = df.iloc[:][1] # 제 1(두 번째) 열: 일일 확진자수
locator = mdates.DayLocator(bymonthday=[1, 15])
formatter = mdates.DateFormatter('%Y %m %d') # ('%Y %b %d')
fig = plt.figure(tight_layout=True)
ax = plt.subplot(2,2,1)  # 그림 P8.10.1(a)
ax.xaxis.set_major_locator(locator) # 날짜눈금 위치
ax.xaxis.set_major_formatter(formatter) # 날짜눈금 형식
ax.bar(t, y)
ax.tick_params(axis='x', rotation=70) # x-축 눈금을 70도 기울여
dt=0.01; ts = np.arange(0, 1, dt)
ys = np.cumsum(ts**2)*dt  # xs의 누적합(cumulative sum)
ax = plt.subplot(2,2,2)  # 그림 P8.10.1(b)
ax.plot(ts, ys, ts, ts**3/3,'r:') # t^2의 적분 t^3/3도 빨간 점선으로
ax.set_xlabel('시간 t[s] \n based on a long experiment')
ax.set_ylabel(r'$\int_0^t t^2 dt = \frac{1}{3}t^2$') #LaTex format

dt=0.01; ts = np.arange(0, 2.1, dt)
pi = np.pi; ys = np.sin(pi*ts)
ax1 = plt.subplot(2,2,3)  # 그림 P8.10.2(a)
ax1.plot(ts, ys)
ax1.set_xlabel('t')
ax1.set_ylabel('sin($\pi t$)')
ts1 = ts*pi
ys1 = np.sin(ts1)
ax2 = plt.subplot(2,2,4)  # 그림 P8.10.2(b)
ax2.plot(ts1, ys1)
ticks = np.arange(0, 2.1, 0.5) # 눈금값 수열
ticks1 = ticks*pi
ax2.xaxis.set_ticks(ticks1) # 눈금의 좌표 지정
#눈금값 수열 ticks로부터 눈금 label 모음을 구성하는 list comprehension
tickla = [f'{tick:1.1f}$\pi$' for tick in ticks]
ax2.xaxis.set_ticklabels(tickla) # 눈금에 표시할 문자(열)
ax2.set_xlim([ts1[0],ts1[-1]+0.1]) # x-축의 범위 지정
ax2.set_xlabel('t')
ax2.set_ylabel('sin(t)') 

plt.show()
