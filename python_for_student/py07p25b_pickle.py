#py07p25b_pickle.py
import pickle 
# 하나의 함수 add()를 만든다.
def add(a, b):
   return a+b
# add() 함수를 저장할 파일을 write-binary mode로 연다.
fw = open('ftn_add.pkl', 'wb')
# add() 함수를 fw 파일에 저장한다. 
pickle.dump(add, fw)# pickling
fw.close() # closing file
# add() 함수를 저장한 파일을 read-binary mode로 연다.
frb = open('ftn_add.pkl', 'rb')
# add() 함수를 되살려내서 add_my라는 이름으로 저장한다.
add_my = pickle.load(frb) # unpickling
frb.close() # closing file
# add_my() 함수를 호출하여 사용해본다.
a, b = 2, 3
print(f"{a}+{b} = {add_my(a,b)}")
