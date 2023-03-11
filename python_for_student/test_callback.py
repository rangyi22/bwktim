#test_callback.py
def cal(callback_ftn, L_in):
   L_out = []
   for i in L_in: 
      L_out.append(callback_ftn(i))
   return L_out
def add2(num):
   return num + 2
def mul2(num):
   return num * 2
