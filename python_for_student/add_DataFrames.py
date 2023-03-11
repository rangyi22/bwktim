#add_DataFrames.py
import pandas as pd

Mypath = 'D:/Python/data/'
fxl_name1='Hana.xlsx'; fxl_name2='KEB.xlsx'; # 두 입력파일명
fxl_name='HanaKEB.xlsx' # 출력 파일명
df1e = pd.read_excel(Mypath+fxl_name1) # Pandas dataframe
df2e = pd.read_excel(Mypath+fxl_name2) # Pandas dataframe
print('DataFrames from the two Excel files:')
print('df1e =\n', df1e);  print('df2e =\n', df2e)
# dfe1/dfe2의 제0열에 있는 ID를 index로 해서 새로운 df1/df2를 만든다.
col1=df1e.columns[1:]; ind1=df1e.values[0:,0]
col2=df2e.columns[1:]; ind2=df2e.values[0:,0]

df1=pd.DataFrame(df1e.values[0:,1:],columns=col1,index=ind1)
df2=pd.DataFrame(df2e.values[0:,1:],columns=col2,index=ind2)
nc = 1  # 수치 data가 시작되는 column 번호
columns1 = list(col1[nc:]); columns2 = list(col2[nc:])

# 숫자는 확실히 실수형으로 type을 지정한다.
df1[columns1] = df1[columns1].astype(float)
df2[columns2] = df2[columns2].astype(float)

# df2에는 있는데 df1에는 없는 예금계좌의 잔액을 0으로 설정한다.
for x in list(set(columns2)-set(columns1)):   df1[x] = 0.

# df1에는 있는데 df2에는 없는 예금계좌의 잔액을 0으로 설정한다.
for x in list(set(columns1)-set(columns2)):   df2[x] = 0.
print('\n 통합될 준비가 된 DataFrame들:')
print('df1 =\n', df1);  print('df2 =\n', df2)

# 덧셈작업대상인 두 df의 숫자부분을 취해서
df1_2 = pd.DataFrame(df1[df1.columns[nc:]])
df2_2 = pd.DataFrame(df2[df2.columns[nc:]])
# 더하되, data가 없는 공란은 0으로 채운다.
df = df2_2.add(df1_2, fill_value=0)
print('\n 통합된 (숫자만 포함한) DataFrame df:\n', df)

# 통합된 df의 index에 있는 ID들에 대한 이름값들을 두 개의 df에서 찾아 
#  names라는 이름의 list를 만들어서
names = [] #  names라는 이름의 list를 일단 빈 list로 초기화한다.
for ID in df.index:
   if ID in df1.index: names.append(df1.loc[ID]['이름'])
   else: names.append(df2.loc[ID]['이름'])
# 통합된 df에 '이름' column으로 추가한다.
df['이름'] = names 
# 마지막 '이름' column label을 제1 column의 label로 앞세운다.
L = list(df.columns); columns12 = L[-1:]+L[:-1]
# 새로 만들어진 column label에 맞춰 열들을 재정렬한다.(10.3.1(9) 참조)
df = pd.DataFrame(df, columns=columns12)
# df array의 좌상귀에 'Item'과 'ID'를 추가한다.
df.index.name = 'ID'; df.columns.name = 'Item'
print('\n 통합된 DataFrame df =\n', df)

# Save the modified Pandas dataframe as an Excel 파일
df.to_excel(Mypath+fxl_name, index=True)
