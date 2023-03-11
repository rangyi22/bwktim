#py07p09f_password.py
import re
s_list = ['bc09_', 'Anm1_234', 'a_@', '2sop']
pattern = '^[a-z][a-z0-9_]{2,7}$' # ^: 시작, $: 끝
for s in s_list:
   mobj = re.match(pattern, s)
   if mobj: print('Ok')
   else: print('Wrong format!')
