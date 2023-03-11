#test_pickle.py
import pickle 
# 하나의 dict(ionary)형 data를 만든다.
db = {}  # 빈 dictionary로 초기화한다.
db['Charley'] = {'Kor': 85, 'Math': 90, 'Physics': 75} 
db['Jessica'] = {'Kor': 90, 'Math': 75, 'Physics': 85} 
fname = 'grade.pkl'; # 쓸 pickle (binary) 파일의 이름 
f = open(fname,'wb') # 이진 mode로 쓸 파일을 연다.
pickle.dump(db, f)  # 데이터 db를 pickle (binary) 파일로 저장한다.
f.close() # 쓰기를 완료한 pickle 파일을 닫는다.
f = open(fname, 'rb') # 읽을 파일을 binary read mode로 연다.
db1 = pickle.load(f) # binary data 파일을 읽는다.
print(db1) 
f.close() # 읽기를 완료한 pickle 파일을 닫는다.
