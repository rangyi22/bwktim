str = "Programming"

# 모음이 나타나면 출력을 건너뛴다.
for val in str:
    if val in ['a', 'e', 'i', 'o']:
        continue
    print(val)

print("The end")