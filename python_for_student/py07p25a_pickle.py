#py07p25a_pickle.py
import pickle 
# 하나의 dictionary 형 data를 만든다.
db = {}  # 빈 dictionary로 초기화한다.
db['Charley'] = {'Kor': 85, 'Math': 90, 'Physics': 75} 
db['Jessica'] = {'Kor': 90, 'Math': 75, 'Physics': 85} 
bts = pickle.dumps(db) # db를 binary data(bytes)로 저장한다.
db1 = pickle.loads(bts) # binary data를 읽는다.
