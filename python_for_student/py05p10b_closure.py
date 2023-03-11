#py05p10b_closure.py
def my_closure(func):
   def f(L):
      return func(L) 
   return f 

def mul(L): # 자기 안에서 자기를 호출하는 재귀(recursive) 함수
   if type(L) != list:  return L
   if len(L) < 2:  return L[0]
   else:  return  L[0] * mul(L[1:])
sum_list = my_closure(sum)
mul_list = my_closure(mul)
L = [1, 2, 3, 4]
print(sum_list(L))
print(mul_list(L))
