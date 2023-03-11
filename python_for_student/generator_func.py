#generator_func.py
# generator를 이용해서 한 파일을 한 줄씩 읽어낸다.
def generator1(file_name):  # generator function
   for row in open(file_name, "r"):
      yield row
gen = generator1("grade.csv")  # generator object
while True:
   try:  print(next(gen), end='')
   except: 
      print("Generator gen has been out of stock!")
      break  # 어떤 실행오류라도 발생되면 종료  
