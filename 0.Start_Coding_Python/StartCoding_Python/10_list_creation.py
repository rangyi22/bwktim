# List Creation
animals = ["Lion", "Tiger", "Cat", "Dog"]

# Data Access
name = animals[3]

# Adding the data
animals.append("Hippo")
animals.append(1)

# Delete the data
del animals[-1] # delete the last data

# List slicing
slicing = animals[1:3]

# List length
length = len(animals)

# List sorting
animals.sort(reverse=True) # print the list with the descending order

print(animals)