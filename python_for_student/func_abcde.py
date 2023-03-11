#func_abcde.py
def func_a(): 
   print(f'a = {a} inside func_a().')
def func_b(): 
   b = 20
   print(f'b = {b} inside func_b().')
def func_c(): 
   func_b()
   print(f'b = {b} inside func_c().')
def func_d(): 
   global a
   a = 30
def func_e(): 
   c = c + 1  
