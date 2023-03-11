#py05p01c.py
def avg(*t): # 입력인자가 tuple일 거라 기대함
   if type(t) != tuple:  y = t
   else:
     y = sum(t)/len(t)
   return y
