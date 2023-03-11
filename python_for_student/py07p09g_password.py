#py07p09g_password.py
import re
L = ['bc$09_', 'AnM1_#23$4', 'A%1!234', 'A@1234', '2S# o%p']
p = "^(?=.{  })(?=.*\d)(?=.*[   ])(?=(.*\W){2})(?!.   ).*$"
for s in L:  # 부록 D의 예제 D.1 참조
   mo = re.match(p, s) # 이 값이 뭐든지 간에 있기만 하면 ok
   if mo: print(s, ' is valid as a password.')
   else: print(s, ' is invalid as a password.')
