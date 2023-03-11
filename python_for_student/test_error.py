#test_error.py (이 code를 저장한 파일이름)
while True:
   x = input("숫자를 입력하세요: ")
   if x.isdigit(): # 10진수로 변환가능한가?
      x = int(x)  # 정수로 변환
      print(f' {x}**2 = {x**2}')
      break
   else:  # ValueError:
      print("에구, 그건 숫자가 아닌데요. 다시 입력하세요!")
      continue
