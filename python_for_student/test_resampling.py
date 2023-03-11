#test_resampling.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.3f}'.format
dr = pd.date_range('2020-03-01', periods=31, freq='D')
df = pd.DataFrame(np.sqrt(np.arange(len(dr))), index=dr,
                  columns=['A'])
df_ = df
df_['index'] = df.index
df1 = df.resample('W-FRI').mean()
df_['resample:W-FRI_mean'] = df1
df4 = df1.resample('D').bfill() # upsampled daily
df_['upsample:bfill'] = df4
df5 = df1.resample('D').interpolate(method='linear')
df_['interp:linear'] = df5
df6 = df1.resample('D').interpolate(method='polynomial', order=2)
df_['interp:poly'] = df6
print("\n df_ =\n", df_)  
fig, axes = plt.subplots(1,3, tight_layout=True)
df_[['A','upsample:bfill']].plot(ax=axes[0], fontsize=5) #그림10.4a
df_.plot.scatter(x='index', y='resample:W-FRI_mean', ax=axes[0])
df_[['A','interp:linear']].plot(ax=axes[1], fontsize=5) #그림10.4b
df_.plot.scatter(x='index', y='resample:W-FRI_mean', ax=axes[1])
df_[['A','interp:poly']].plot(ax=axes[2], fontsize=5) #그림10.4c
# nan을 포함한 df1을 scatter 아닌 plot()을 사용해서도 점형으로 그릴 수 있다.
df_.plot(x='index', y='resample:W-FRI_mean', kind='scatter', ax=axes[2])
plt.show()
