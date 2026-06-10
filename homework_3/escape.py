print("I'm a boy")
print('I\'m a boy')
print('I\\m a boy')

print('a \t b')
print('a \n b')
print('a \"\" b')

# Output:
# I'm a boy
# I'm a boy
# I\m a boy
# a        b
# a 
#  b
# a "" b

escape_str1 = "Do you have a \"retro games\"?"
escape_str2 = "What\'s on TV?"
print(escape_str1)
print(escape_str2)

t_s1 = "Click \tStart!"
t_s2 = "New Line\n Check!"
print(t_s1)
print(t_s2)

# Output:
# Do you have a "retro games"?
# What's on TV?
# Click   Start!
# New Line
#  Check!

raw_s1 = r'D:\Python\python3' # rをつけると、\をエスケープ文字として認識しない。つまり、\tはタブではなく、\とtの2文字として認識される。
raw_s2 = r'D:\tPython\python3'

print(raw_s1)
print(raw_s2)

# Output:
# D:\Python\python3
# D:\tPython\python3

print("C:\\Users\\Student")
print(r"C:\Users\Student")

# Output:
# C:\Users\Student
# C:\Users\Student

multi_str = ''' 
String
Multiline
Test
'''
print(multi_str)

# Output:
#  
# String
# Multiline
# Test
# 

multi_str2 = \
'''
String Multiline
バックラッシュ(\)\
テスト
'''
print(multi_str2)

# Output:
# 
# String Multiline
# バックラッシュ(\)テスト
# 

multi_str3 = \
'abc' \
'def' \
'ghi'\

print(multi_str3)
# Output:
# abcdefghi

str_o1 = 'Python'
str_o2 = "Apple"
str_o3 = "Show are you doing?"
str_o4 = 'Tokyo Kyoto Osaka Okinawa'

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('z' in str_o1)
print('P' not in str_o2)

# Output:
# PythonPythonPython
# PythonApple
# True
# True
# False
# True

print(str(77))
print(type(str(77)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))
print(str(complex(12)), type(str(complex(12))))

# Output:
# 77
# <class 'str'>
# 10.1 <class 'str'>
# True <class 'str'>
# (12+0j) <class 'str'>

str_o1 = 'python'
str_o2 = "Apple"
str_o3 = "Show are you doing?"
str_o4 = 'Tokyo Kyoto Osaka Okinawa'

print('Capitalize: ', str_o1.capitalize())
print('endswith: ', str_o2.endswith('s'))
print("replace1: ", str_o1.replace('thon', ' Good'))
print('sorted: ', sorted(str_o1)) 
print("split: ", str_o4.split(' '))

# Output:
# Capitalize:  Python
# endswith:  False
# replace1:  py Good
# sorted:  ['h', 'n', 'o', 'p', 't', 'y']
# split:  ['Tokyo', 'Kyoto', 'Osaka', 'Okinawa']

im_str = "Good Boy!"
print(dir(im_str)) 

# Output:

# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', 
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__',
#  '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
#  '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
#  '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode',
#  'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
#  'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
#  'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
#  'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
#  'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
#  'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

for i in im_str:
    print(i)

# Output:
# G
# o
# o
# d
 
# B
# o
# y
# !

str_slice = "Nice Python"
print(len(str_slice))

print(str_slice[0:3])
print(str_slice[5:11])
print(str_slice[5:])
print(str_slice[:])
print(str_slice[:len(str_slice)])
print(str_slice[:len(str_slice) - 1])
print(str_slice[1:4:2])
print(str_slice[-5:])
print(str_slice[1:-2])
print(str_slice[::2])
print(str_slice[::-1])

# Output:
# 11
# Nic
# Python
# Python
# Nice Python
# Nice Python
# Nice Pytho
# ie
# ython
# ice Pyth
# Nc yhn
# nohtyP eciN

code = 'a'
print(ord(code))
print(chr(97))

# Output:
# 97
# a

print("Hello, world")
print('Hello, world')

# Output:
# Hello, world
# Hello, world


str = '''
Hello
Python
'''
print(str)

str = """
Hello
Python
"""
print(str)

# Output:

# Hello
# Python


# Hello
# Python

print("Hello, \'Python\'")
print("Hello, 'Python'")
print(""""Hello", Python""")

# Output:
# Hello, 'Python'
# Hello, 'Python'
# "Hello", Python

s = """Python is a programming language that lets you work quickly
and
integrate systems more effectively."""
print(s)

# Output:
# Python is a programming language that lets you work quickly
# and
# integrate systems more effectively

s = r"""'Python' is a "programming language" that lets you work quickly
and
integrate systems more effectively."""
print(s)

# Output:
# 'Python' is a "programming language" that lets you work quickly
# and
# integrate systems more effectively.