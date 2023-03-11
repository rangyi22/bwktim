str = "Programming"

# 자음이 나타날때만 출력
for val in str:
    if val in ['a', 'e', 'i', 'o', 'u']:
        break # 모음인 경우 반복문을 종료
    print(val)

print("The end")