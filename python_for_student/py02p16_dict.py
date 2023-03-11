#py02p16_dict.py
dic = {'홍길동': {'나이': 36, 'Corona': '치료중'},
       '장비': {'나이': 33, 'Corona': '치료중'},
       '관우': {'나이': 35, 'Corona': '음성'},
       '조자룡': {'나이': 32, 'Corona': '완치'}}
dic[     ] = {'나이':   , '      ': '음성'}
print(dic)
dicitems = dic.copy().items()
for key, val in dicitems:
   if val['Corona'] == '음성': # value가 '음성'이면
     dic.pop(key)  # key-value 쌍 삭제
print(dic)
dickeys =     (dic.    ());  print(dickeys)
print(   ['조자룡'])
dic['  ']['      '] = '  ';  print(dic)
for key,    in dic.    ():
   print(f'{   } = {val}')
