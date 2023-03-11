#test_filter1.py
alphabets = ['a','b','d','e','i','j','o']
vowels = ['a','e','i','o','u']
f = lambda x: x in vowels  # True if x in vowels
alphabets_vowel = list(filter(f, alphabets))
print(alphabets_vowel)
