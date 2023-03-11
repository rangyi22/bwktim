#py10p04_merge.py
import pandas as pd

Mypath = 'D:/Python/data/'
foname = 'corona_out.csv' # 출력파일 이름
file_nos = [1, 2] # 각 CSV 파일 이름의 어미들을 모아놓은 list
for n, file_no in enumerate(file_nos):
   filename = Mypath + 'corona%d.csv' % file_no
   dfn = pd.read_csv(filename) #, header=None
   if n==0:  
     dfs = dfn  # 첫 번째 파일은 그것만으로 하나의 df로 저장하고
   else:  
     dfs = pd.merge(dfs, dfn, on='Date', how='outer')
df = dfs.fillna(0)  # NaN을 0으로 대체
df = df.sort_values(by='Date') # Date 열을 기준으로 정렬
print('dfs =\n', dfs)
print('df =\n', df)
# Save the modified Pandas DataFrame as an Excel file
df.to_csv(Mypath+foname, sep=',', na_rep='NaN', index=False)
