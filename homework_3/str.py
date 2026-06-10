str1 = "I am Python."
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

# Output:
# <class 'str'>
# <class 'str'>
# <class 'str'>
# <class 'str'>
# 12
# 6
# 12
# 10

str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# Output:
# <class 'str'> 0
# <class 'str'> 0