#test_concat_csv.py
import pandas as pd

# 특정 경로에 있는 여러 개의 CSV 파일들을 하나의 DataFrame으로
Mypath = 'D:/Python/data/'
file_nos = [1,2,3]
n = 0
for file_no in file_nos:
   filename = Mypath + f'grade0{file_no}.csv'
   dfn = pd.read_csv(filename) # 부록 J.1 참조
   dfn['Class'] = file_no
   if n == 0:   dfs = dfn
   else:  dfs = pd.concat([dfs, dfn], ignore_index=True)
   n = n+1
print(dfs)
