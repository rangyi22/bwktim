# 콘솔을 통해 사용자로터 입력받고 출력해주는 프로그램
# 입력: input()
#data = input("Enter your inputs.: ")
#print(data)

# input >> 모두 문자열 취급
# num1 = input("1.")
# num2 = input("2.")
# print(num1 + num2)

# File Generation
# file = open("./example.txt", "w")

# for i in range(1, 11):
#     data = "It is %d line.\n" % i
#     file.write(data)

# file.close()

# File Read
#file = open("./example.txt", "r")

# while True:
#     line = file.readline()
#     if not line: break
#     print(line)

# lines = file.readlines()

# for line in lines:
#     print(line)

# file.close()

# File Append
file = open("./example.txt", "a")

file.write("Write down a new line.")

file.close()