#test_error2.py
while True:
   try: # 이 부분은 어떤 경우든 실행되며, 여기서 실행오류가 발생하면 except로 
        x = int(input("숫자를 입력하세요: "))
        if x=='':  break
        x = int(x)
   except: # ValueError같은 예외가 발생하면
        print("에구, 그건 숫자가 아닙니다. 다시 입력하세요!")
        continue
   else: # try 문에서 아무런 예외가 발생하지 않으면
        print(f' {x}**2 = {x**2}')
   finally: # 어떤 경우든지 이 loop를 벗어나기 직전에 꼭 수행되는 부분
        print(' End of this block')        
