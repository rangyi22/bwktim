#py04p07_json.py
import json as js
dic1 = {}
dic1['홍길동'] = {'나이': 25, '코로나': '확진'}
dic1['한석봉'] = {'나이': 33, '코로나': '완치'}
with open('py04p07.json', 'w') as f:
    js.    (dic1, f)
with open('py04p07.json') as f:
    dic2 = js.    (f)
print(dic2)
