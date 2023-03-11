#py05p01d.py
def div(**d): #입력인자가 {'a':a,'b':b}같은 dictionary일 거라 기대
if type(d) != dict:  
   y = None
  else: 
     a = d['a'];  b = d['b'] 
     y = a/b 
  return y
