#grade_xl2.py
import pandas as pd
Mypath = 'D:/Python/data'
fxl = Mypath+'grade.xlsx'; fxl1 = Mypath+'grade1.xlsx' 
fcsv = Mypath+'grade2.csv'
df = pd.read_excel(fxl) # Pandas dataframe
df['Sum'] = df['Kor'] + df['Math'] + df['Physics']
# 변경된 Pandas dataframe을 Excel 파일로 저장
df.to_excel(fxl1, index=False)
# 변경된 Pandas dataframe을 CSV 파일로 저장
df.to_csv(fcsv, sep=',', index=None, header=True,\
          encoding='utf-8-sig') # CSV 파일에 한글이 제대로 쓰여지도록
