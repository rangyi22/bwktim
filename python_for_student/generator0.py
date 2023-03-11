#generator0.py
# readlines() 함수를 사용해서 파일을 한꺼번에 읽는다. 
def reader(file_name):
   f = open(file_name, "r")
   rows = f.readlines()  # readlines()로 파일 전체 내용을 한꺼번에 읽는다. 
   return rows
rows1 = reader("grade.csv") # reader()를 사용해서 파일을 한꺼번에 읽는다.
for n in range(len(rows1)): 
   print(rows1[n], end='')
