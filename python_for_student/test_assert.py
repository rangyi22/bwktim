#test_assert.py
import math
def my_sqrt(x): 
   assert type(x) != str, 'x should not be a string!'
   if x < 0:
     raise Exception('x must be nonnegative!')
     #raise NotImplementedError('x must be nonnegative!') #이렇게 해도
   else: # 아무런 실행오류가 발생하지 않았을 때
     y = math.sqrt(x)
   return y 
