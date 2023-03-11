#py07p01.py
import os
path = os.getcwd()  # 현재 경로
directory = os.listdir(path) # 현재 경로의 파일, folder 목록
files = list(filter(os.path.isfile, directory)) # 파일 목록
dirs = list(filter(os.path.isdir, directory))   # folder 목록
print("\n dirs =", dirs)   # folder 목록
newpath = "myfolder"  # 파일을 저장할 하위 경로
if newpath not in dirs:  # 현재 경로에 없다면 
  os.mkdir(newpath)      # 만들어
fname = 'py07p01.txt'    # 파일명
f = open(path + '/' + newpath + '/' + fname, 'w')
s = """나는 대한민국이 번영하기 위해서는 어떻게든 북한과 협력하여
서울-유럽간 철도를 개통하고 한국-러시아간 가스관을 설치하는 한편,
인구절벽문제에도 대비해야 한다고 생각합니다."""
f.write(s)
f.close()
