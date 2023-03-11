# (a * x^2) + (b * x) + c = 0
# where a != 0 
def get_root(a, b, c):
    r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1, r2

# 함수 호출 시 인자를 상수값을 사용함
result1, result2 = get_root(1, 2, -8)
print('해는', result1, '또는', result2)