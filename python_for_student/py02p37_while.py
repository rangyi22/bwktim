#py02p37_while.py
user_numbers = [] # Initialize user_numbers as an empty list
while len(user_numbers)<3:
   user_number = input('Input a number:')
   if not user_number.isnumeric():
      
   user_numbers.append(int(user_number))
print(user_numbers)
