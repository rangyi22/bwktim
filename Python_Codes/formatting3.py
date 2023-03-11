print('{} and {}'.format('King', 'Queen'))
print('{0} and {1}'.format('King', 'Queen'))
# {1}: second argument, {0}: first argument
print('{1} and {0}'.format('King', 'Queen'))

# 인수의 이름을 통해 접근
print('Coordinates: {latitude}, {longitude}'.format(
    latitude = '37.24N', longitude = '-115.81W'))

print('{:<30}'.format('Left Sorting')) # 30 is the width of the field
print('{:>30}'.format('Right Sorting'))

print('{:+f}, {:+f}'.format(3.14, -3.14)) # Insert +, - signals
print('{: f}, {: f}'.format(3.14, -3.14)) # Insert - signal only

print("int: {0:d}; hex: {0:x}; oct: {0:o}, bin: {0:b}".format(30))
print('{:,}'.format(1234567890)) # 1,000 단위 쉼표 출력

# 소수점 아래 출력 (percentage)
print('1/3은 {:.2%}'.format(1/3))

# 연, 월, 일, 시 출력
import datetime
d = datetime.datetime(2022, 5, 24, 23, 57, 28)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))