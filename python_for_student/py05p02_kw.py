#py05p02_kw.py
def introduce(**names, hobby):
   name = names['first_name'] + ' '
   if len(names)>2: name += names['middle_name'] + ' '
   name += names['last_name']
   print(f"{name}의 취미는 {hobby}입니다.")
introduce(last_name='홍', first_name='Gil', middle_name='D.', '낚시')
