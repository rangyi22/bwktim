#test_match.py
import re
s_list = ['Pw_12#', 'Ab#12@', 'B23', 'Ccdefg12']
pattern = '[A-Z][a-z0-9_#]{3,5}$'
for s in s_list:
   mobj = re.match(pattern, s) # , re.IGNORECASE)
   print('mobj =', mobj)
