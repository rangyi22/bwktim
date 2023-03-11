#grade_csv2.py
import pandas as pd
Mypath = 'D:/Python/data/'
fcsv_name= Mypath+'grade.csv'; fcsv_name2= Mypath+'grade2.csv'
df = pd.read_csv(fcsv_name) # Pandas dataframe
df[       ] = df['Kor'] + df[      ] + df['Physics']
# 변경된 Pandas dataframe을 CSV 파일로 저장
df.to_csv(fcsv_name2, sep=',', index=None, header=True)
