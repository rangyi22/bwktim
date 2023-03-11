#age = 34
#ages_as_str = str(age)
#print("You are " + ages_as_str)
#print(f"You are {age}")

#name = "Jose"
#greeting = f"How are you, {name}?"
#print(greeting)

#name = "Bob"
#print(greeting)

'''
name = "Jose"
final_greeting = "How are you, {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)
'''
'''
name = "Jose"
final_greeting = "How are you, {name}?"
jose_greeting = final_greeting.format(name=name)
print(jose_greeting)
bob_greeting = final_greeting.format(name="Bob")
print(bob_greeting)
'''

name = "Jose"
final_greeting = "How are you, {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)