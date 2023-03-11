#test_error3.py
def divide(x, y): # x, y라는 두 입력인자를 가진 divide() 함수의 정의 
   try:
       result = x/y
   except ZeroDivisionError:
       print('Division by zero!')
   except TypeError: 
       print('TypeError')
   else: # 아무런 실행오류가 발생하지 않았을 때
       print(f'{x}/{y} = {result}')
divide(3,2) # Normal division performed
divide(2,0) # Division by zero!
divide('3',2) # TypeError
