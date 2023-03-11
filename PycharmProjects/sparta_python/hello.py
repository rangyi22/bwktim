#print('hello sparta')

#a = (3 == 2)
#print(a)

#first_name = 'WK'
#last_name = 'BAE'
#print(first_name+last_name)

#a = '2'
#b = str(2)
#print(a+b)

#text = 'abcdefghijk'
#result = text[3:8]
#result = text[:] # Copy
#print(result)

'''
myemail = 'wk.bae2020@gmail.com'
result = myemail.split('@')[1].split('.')[0]
print(result)
'''

'''
text = 'sparta'
result = text[:3]
print(result)
'''

'''
phone = '031-4257-8070'
result = phone.split('-')[0]
print(result)
'''

#a_list = [2, 'peach', False, ['apple', 'peach']]
#a_list = [1,5,6,3,2]
#a_list.append(99)
#a_list.append(100)
'''
a_list = [1,5,6,3,2]
result = len(a_list)
print(result)
'''

#a_list = [1,5,6,3,2]
#a_list.sort()
#a_list.sort(reverse=True)
#print(a_list)

'''
a_list = [1,5,6,3,2]
result = (99 in a_list)
print(result)
'''

'''
a_dict = {'name': 'Bob', 'age': 27, 'friend': ['Joey', 'Tony']}
#result = a_dict['name']
#result = a_dict['age']
#result = a_dict['friend'][1]
#a_dict['height'] = 180
result = 'height' in a_dict
print(result)
'''
'''
people = [
    {'name': 'Bob', 'age': 27},
    {'name': 'John', 'age': 30}
]
print(people[1]['age'])
'''

'''
people = [
    {'name': 'Bob', 'age': 20, 'score': {'Math': 90, 'Science': 70}},
    {'name': 'Carry', 'age': 38, 'score': {'Math': 40, 'Science': 72}},
    {'name': 'Smith', 'age': 28, 'score': {'Math': 80, 'Science': 90}},
    {'name': 'John', 'age': 34, 'score': {'Math': 75, 'Science': 100}}
]
result = people[2]['score']['Science']
print(result)
'''

'''
money = 1000

if money > 3800:
    print('Take a taxi!')
elif money > 1200:
    print('Take a bus!')
else:
    print('Let\'s walk!')
'''
'''
fruits = ['apple', 'peach', 'banana', 'water melon', 'strawberry']
for fruit in fruits:
    print(fruit)
'''

'''
people = [
    {'name': 'Bob', 'age': 20},
    {'name': 'Carry', 'age': 38},
    {'name': 'John', 'age': 7},
    {'name': 'Smith', 'age': 17},
    {'name': 'Ben', 'age': 27},
    {'name': 'Bobby', 'age': 57},
    {'name': 'Red', 'age': 32},
    {'name': 'Queen', 'age': 25},
]
'''

#print(people[0])
'''
for person in people:
#print(person)
    name = person['name']
    age = person['age']
    #print(name, age)
    if age > 20:
        print(name, age)
'''
# For statement with enumerate
'''
people = [
    {'name': 'Bob', 'age': 20},
    {'name': 'Carry', 'age': 38},
    {'name': 'John', 'age': 7},
    {'name': 'Smith', 'age': 17},
    {'name': 'Ben', 'age': 27},
    {'name': 'Bobby', 'age': 57},
    {'name': 'Red', 'age': 32},
    {'name': 'Queen', 'age': 25},
]
'''

'''
for i, person in enumerate(people):
    name = person['name']
    age = person['age']
    print(i, name, age)
    if i > 2:
        break
'''
'''
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
count = 0
for num in num_list:
    if num % 2 == 0:
        count += 1
print(count)
'''
'''
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
sum = 0
for num in num_list:
    sum += num
print(sum)
'''

'''
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 80, 2, 4]
max = 0
for num in num_list:
    if num > max:
        max = num
print(max)
'''

'''
def hello():
    print('Hello!')
    print('Nice weather!')

hello()
hello()
'''

'''
def sum(a,b):
    print('You\'ve added two numbers!')
    return a+b

result = sum(1,2)
print(result)
'''

'''
def bus_rate(age):
    if age > 65:
        #print('It is free.')
        return 0
    elif age > 20:
        #print('You are adult.')
        return 1200
    else:
        #print('You are adolescence.')
        return 750

my_rate = bus_rate(15)
print(my_rate)
'''

'''
def check_gender(pin):
    #gender_pin = pin.split('-')[1][0]
    num = pin.split('-')[1][:1] # num is a string
    #print(num)
    if int(num) % 2 == 0:
        print('You are a female!')
    else:
        print('You are a male!')

check_gender('150101-1012345')
check_gender('150101-2012345')
check_gender('150101-4012345')
'''

'''
a = ('Apple', 'Peach', 'Grape')
a[1] = 'Water Melon'
print(a[1])
'''

#people = [{'name': 'Bob', 'age': 27}, {'name': 'John', 'age': 30}]
#people = [('Bob', 27), ('John', 30)]

#a= [1,2,3,4,3,2,3,4,5,8,7,1]
#a_set = set(a)
#print(a_set)
'''
a = ['Apple', 'Peach', 'Grape', 'Water Melon', 'Strawberry']
b = ['Grape', 'Apple', 'Banana', 'Orange', 'Lemon']

a_set = set(a)
b_set = set(b)

print(a_set & b_set)
print(a_set | b_set)
'''

'''
student_a = ['물리2', '국어', '수학1', '음악', '화학1', '화학2', '체육']
student_b = ['물리1', '수학1', '미술', '화학2', '체육']

a_set = set(student_a)
b_set = set(student_b)
print(a_set - b_set)
'''

'''
scores = [
    {'name': '영수', 'score': 70},
    {'name': '영희', 'score': 65},
    {'name': '기찬', 'score': 75},
    {'name': '희수', 'score': 23},
    {'name': '서경', 'score': 99},
    {'name': '미주', 'score': 100},
    {'name': '병태', 'score': 32}
]

for s in scores:
    name = s['name']
    score = str(s['score'])
    #print(name, score)
    #print(name + '의 점수는 ' + score + '점입니다.')
    print(f'{name}의 점수는 {score}점입니다.')
'''

'''
people = [
    {'name': 'Bob', 'age': 20},
    {'name': 'Carry', 'age': 38},
    {'name': 'John', 'age': 7},
    {'name': 'Smith', 'age': 17},
    {'name': 'Ben', 'age': 27},
    {'name': 'Bobby'},
    {'name': 'Red', 'age': 32},
    {'name': 'Queen', 'age': 25},
]

for person in people:
    try:
        if person['age'] > 20:
            print(person['name'])
    except:
        print(person['name'], 'Error occurs')
'''

'''
num = 3
#if num % 2 == 0:
#    result = 'even number'
#else:
#    result = 'odd number'

result = ('even number' if num % 2 == 0 else 'odd number')
print(f'{num} is an {result}.')
'''

'''
a_list = [1,3,2,5,1,2]

#b_list = []
#for a in a_list:
#    b_list.append(a*2)

b_list = [x*2 for x in a_list]

print(b_list)
'''

'''
people = [
    {'name': 'Bob', 'age': 20},
    {'name': 'Carry', 'age': 38},
    {'name': 'John', 'age': 7},
    {'name': 'Smith', 'age': 17},
    {'name': 'Ben', 'age': 27},
    {'name': 'Bobby', 'age': 57},
    {'name': 'Red', 'age': 32},
    {'name': 'Queen', 'age': 25},
]
def check_adult(person):
    if person['age'] > 20:
        return 'Adult'
    else:
        return 'Adolescent'

result = list(map(check_adult, people))
print(result)
'''
'''
def check_adult(person):
    return 'Adult' if person['age'] > 20 else 'Adolescent'
result = map(check_adult, people)
#result = map(lambda x:x, people)
result = map(lambda person: ('성인' if person['age'] > 20 else '청소년'), people)
print(list(result))
'''

'''
#result = filter(lambda person: person['age'] > 20, people)
result = filter(lambda x: x['age'] > 20, people)
print(list(result))
'''

'''
def cal(a,b):
    return a+2*b

result = cal(b=2,a=1)
print(result)
'''

'''
def cal(a,b=2):
    return a+2*b

#result = cal(1)
result = cal(1,3)
print(result)
'''

'''
def cal(*args): # *args (arguments)를 통해서 인자들을 무제한으로 받을 수 있다.
    for name in args:
        print(f'{name} 밥먹어라!')

cal('Jane', 'Tom', 'Jerry')
'''

'''
def cal(**kwargs): # dictionary 형태의 keyword arguments를 함수로 사용
    print(kwargs)

cal(name='Bob', age=30, height=180)
'''

# Class Example
class Monster():
    hp = 100
    alive = True

    def damage(self, attack):
        self.hp = self.hp - attack
        if self.hp < 0:
            self.alive = False

    def status_check(self):
        if self.alive:
            print('It is alive.')
        else:
            print('It is dead.')

m1 = Monster() # m1 is an instance
m1.damage(150)
m1.status_check()

m2 = Monster()
m2.damage(90)
m2.status_check()
