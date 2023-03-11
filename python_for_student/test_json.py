#test_json.py
import json as js
str1 = 'Hello, Python!'
with open('str1.json', 'w') as f:
   js.dump(str1, f)  # 문자열 str1을 'str1.json'이라는 JSON 파일에 저장
with open('str1.json') as f:
   str2 = js.load(f) # JSON 파일 'str1.json'을 읽는다.
print(str2)
L1 = [1, '2', 'a']
with open('L1.json', 'w') as f:
   js.dump(L1, f) # list L1을 'L1.json' 파일에 저장
with open('L1.json') as f:
   L2 = js.load(f) # JSON 파일 'L1.json'을 읽는다.
print(L2)
dic1 = {'Name': 'Won', 'Subjects': ['Math','Physics','Chemistry']}
with open('dic1.json', 'w') as f:
   js.dump(dic1, f) # dictionary dic1을 'dic1.json' 파일에 저장
with open('dic1.json') as f:
   dic2 = js.load(f) # JSON 파일 'dic1.json'을 읽는다.
print(dic2)
