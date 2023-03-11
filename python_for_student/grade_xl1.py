#grade_xl1.py
#> pip install pandas (in Windows Powershell)
import pandas as pd
Mypath = 'D:/Python/data'
fxl = Mypath+'grade.xlsx'; fxl1 = Mypath+'grade1.xlsx'
df = pd.read_excel(fxl) # Pandas dataframe
# 위에서 만들어진 Pandas dataframe df를 dictionary로 변환
dic1 = df.to_dict() # s = df.to_string()
dic1_keys = list(dic1.keys())
Number_of_data = len(dic1[dic1_keys[0]])
d1 = {0: 0} # 이제 만들 subdictionary를 초기화
for i in range(Number_of_data):
   name = dic1['Name'][i]
   kor = dic1['Kor'][i]; math = dic1['Math'][i]
   physics = dic1['Physics'][i]
   sum = kor + math + physics
   d1[i] = sum
dic1['Sum'] = d1 # 생성된 subdictionary를 dic1에 추가
# 변경된 dictionary를 Pandas dataframe으로 변환
df1 = pd.DataFrame.from_dict(dic1) #, orient='index')
# Pandas dataframe을 Excel 파일로 저장
df1.to_excel(fxl1, index=False)
