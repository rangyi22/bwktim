#grade_txt.py
Mypath = 'D:/Python/data/'
fr = open(Mypath+"grade.txt", 'r') # 읽을 파일
fw = open(Mypath+"grade1.txt", 'w') # 쓸 파일
i=0 # 읽어들일 줄 번호를 0으로 초기화
while 1:
   line = fr.readline()  # 파일을 한 줄 한 줄 읽어 
   if not line: break  # 더 이상 읽을 줄이 없으면 while loop 탈출
   i = i + 1  # 줄 번호(line number)를 1만큼 증가시켜
   (name,kor,mat,phy) = line.split() # name, kor, mat, phy값을 읽어
   # 여기서 민약 data들이 comma로 분리되어 있었다면 split(',')와 같이 해야
   if i==1: # column name을 포함한 첫 번째 row에 대해
     data = f'{name:10} {kor:5} {mat:5} {phy:5} {"Sum":7}\n' 
   else: # data를 포함한 두 번째 row부터
     kor = float(kor); mat = float(mat);  phy = float(phy)
     sum = kor + mat + phy
     data= f'{name:8}: {kor:5.1f} {mat:5.1f} {phy:5.1f} {sum:7.1f}\n'
   fw.write(data)
fr.close()
fw.close()
