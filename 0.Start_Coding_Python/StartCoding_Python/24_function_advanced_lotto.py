import random

lotto_num = [] # empty Lotto number list creation

def getRandomNumber():
    number = random.randint(1, 45)
    return number

count = 0 # variable to count the number of times

while True:
    if count > 5:
        break
    random_number = getRandomNumber() # Extract one Lotto number
    if random_number not in lotto_num: # If extracted one Lotto number is not included the lotto_num list,
        lotto_num.append(random_number) # Add the extracted one into the lotto_num list
        count = count + 1

print(lotto_num)