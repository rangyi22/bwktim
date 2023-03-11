import re
# match
#p = re.compile('[a-z]+')
#m = p.match('python')
#m = p.match('3 python')
#print(m)

# search
#p = re.compile('[a-z]+')
#m = p.search('3 python')
#print(m)

# findall
#p = re.compile('[a-z]+')
# findall (일치하는 string을 list로 담아서 return)
#m = p.findall('life is too short')
#print(m)
#p = re.compile('[a-z]+')

# DOTALL, S
#p = re.compile('a.b', re.DOTALL)
#p = re.compile('a.b', re.S)
#m = p.match('a\nb ')
#print(m)

# IGNORECASE, I
#p = re.compile('[a-z]', re.I)
#print(p.match('python'))
#print(p.match('Python'))
#print(p.match('PYTHON'))

# MULTILINE, M --> 각 line의 처음으로 인식시는 option
#p = re.compile('^python\s\w+', re.M)

#data = """python one
#life is too short
#python two
#you need python
#python threee""
#"""
#print(p.findall(data))

# VERBOSE, X
#charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

#charref = re.compile(r"""
#&[#]    # Start of a numeric entity reference
#(
#    0[0-7]+         # Octal form
#  | [0-9]+          # Decimal form
#  | [0-9a-fA-F]+    # Hexadecimal form
#)
#;
#""", re.VERBOSE)

# Meta Character |
#p = re.compile('Crow|Servo')
#m = p.match('CrowHello')
#print(m)

# Meta Character ^
#print(re.search('^Life', 'Life is too short'))
#print(re.search('^Life', 'My Life'))

# Meta Character $
#print(re.search('short$', 'Life is too short'))
#print(re.search('short$', 'Life is too short, you need Python'))

# Meta Character \b
#p = re.compile(r'\bclass\b')
#print(p.search('no class at all'))
#print(p.search('the declassified algorithm'))
#print(p.search('one subclass is'))

# Grouping ()
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group())