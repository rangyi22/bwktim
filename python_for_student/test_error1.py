#test_error1.py
while True:
   try: # 이 부분은 iteration마다 수행되며, 실행오류를 만날 수 있다.
        x = int(input("숫자를 입력하세요: "))
        print(f' {x}**2 = {x**2}')
        break
   except: # ValueError 같은 오류가 발생하면
        print("에구, 그건 숫자가 아닙니다. 다시 입력하세요!")
        continue 
