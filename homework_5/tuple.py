a = ()
b1 = (1, 2)
b2 = (1)
b3 = (1, )

print(type(a), type(b1), type(b2), type(b3))

# Output:
# <class 'tuple'> <class 'tuple'> <class 'int'> <class 'tuple'>

c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

print('>>>>>>>>>>>>')
print('d - ', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[-1])
print('e -', e[-1][1])
print('e -', list(e[-1][1]))

# Output:
# >>>>>>>>>>>>>>
# d -  1000
# d - 2100
# d - Captain
# e - Base
# e - ['B', 'a', 's', 'e']

t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])

(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# Output:
# ('foo', 'bar', 'baz', 'qux')
# foo
# qux
# <class 'str'> <class 'str'> <class 'str'> <class 'str'>
# foo bar baz qux

t2 = 1, 2, 3
t3 = 4, 
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2, t3)
print(x1, x2, x3)
print(x4, x5, x6)

# Output:
# (1, 2, 3) (4,)
# 1 2 3
# 4 5 6