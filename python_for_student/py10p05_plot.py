#py10p05_plot.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

N=100 # 생성할 데이터의 개수
dates = pd.date_range('2021-01-01', periods=N, freq='D')
npa01 = np.random.rand(N,2)
npa2 = npa01[:,0]*2 + 0.2*np.random.randn(1,N)
npa = np.concatenate((npa01, npa2.T), axis=1)
# NumPy ndarray to Pandas DataFrame
df = pd.DataFrame(npa, columns=['x','y','z'], index=dates)
#각 행들에 대해 'A','B','C' 중 하나를 (새로운) 'Class' 열의 값으로 ..
classes = ['A','B','C']
class_list = [random.sample(classes,1) for x in df['x']]
df['Class'] = np.array(class_list)
print(df.head()) # 생성된 데이터를 확인해보기 위해
