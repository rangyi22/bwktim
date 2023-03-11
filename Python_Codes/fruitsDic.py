# Creation of fruits dictionary
fruits = {'melon': 300, 'banana': 400, 'orange': 700}
print(fruits.keys())
print(fruits.values())
print('apple' in fruits.keys())
print('banana' in fruits.keys())
print(fruits.items())

# Creation of a new dictionary
new_fruits = {'watermelon': 400, 'peach': 800, 'mango': 600}
# Merge a dictionary with a new dictionary
fruits.update(new_fruits)
print(fruits.items())
del(fruits['peach'])
print(fruits.items())
fruits.clear()
print(fruits.items())