#test_concat_csv2.py
import pandas as pd

Mypath = 'D:/Python/data/'
file_nos = [1,2,3]
dfns = []
for file_no in file_nos:
   filename = Mypath + f'grade0{file_no}.csv'
   dfn=pd.read_csv(filename, index_col=['Name']) # 부록 J.1 참조
   dfn['Class'] = file_no
   dfns.append(dfn)
dfs2 = pd.concat(dfns, ignore_index=False)
print(dfs2)
foname = 'grade_out.csv' # 출력파일명
dfs2.to_csv(Mypath+foname, sep=',', index=True)
