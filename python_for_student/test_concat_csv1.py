#test_concat_csv1.py
import pandas as pd

Mypath = 'D:/Python/data/' # 이 경로는 알맞게 정한다.
file_nos = [1,2,3]
dfns = []
for file_no in file_nos:
   filename = Mypath + f'grade0{file_no}.csv'
   dfn = pd.read_csv(filename) # 부록 J.1 참조
   dfn['Class'] = file_no
   dfns.append(dfn)
dfs = pd.concat(dfns, ignore_index=True)
print(dfs)
