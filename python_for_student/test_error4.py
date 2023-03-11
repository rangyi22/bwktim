#test_error4.py
def divide(x, y):
   try:   result = x/y
   except Exception as e:
          print(f'{type(e)}: {e}')
   else: # 아무런 실행오류가 발생하지 않았을 때  
        print(f'{x}/{y} = {result}')
divide(3,2) # 정상적인 나눗셈(normal division)
divide(2,0) # 0으로 나누기(Division by zero)!
divide('3',2) # TypeError
