# (a * x^2) + (b * x) + c = 0
# where a != 0 
def print_root(a, b, c):
    r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    print('해는', r1, '또는', r2)

print_root(1, 2, -8)

n1 = 2
n2 = -6
n3 = -8

# 함수 호출 시 인자를 변수 값으로 사용함
print_root(n1, n2, n3)