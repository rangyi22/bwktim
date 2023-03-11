sum = 0

n = int(input("Enter the number for sum: "))

# for i in range(n):
#     sum = sum + (i+1)
for i in range(n+1):
    sum += i

print('The total sum from 1 to {} is {}'.format(n, sum))