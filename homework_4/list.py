a = []
print(type(a))

b = list()
c = [70, 75, 80, 85]
print(len(c))

# Output:
# <class 'list'>
# 4

a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, 'bark', False,  3.14159]

print('>>>>>>>>')
print('d -', type(d), d)
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[-1])
print('e -', e[-1][1])
print('e -', type(e[-1][1]))
print('e -', list(e[-1][1]))

print('d -', d[0:3])
print('d -', d[2:])
print('e -', e[2][1:3])

# Output:
# >>>>>>>>>>
# d - <class 'list'> [1000, 10000, 'Ace', 'Base', 'Captain']
# d - 10000
# d - 21000
# d - Captain
# e - Base
# e - <class 'str'>
# e - ['B', 'a', 's', 'e']
# d - [1000, 10000, 'Ace']
# d - ['Ace', 'Base', 'Captain']
# e - ['Base', 'Captain']

print(">>>>>>>>")
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# Output:
# >>>>>>>>>>
# d -  [1000, 10000, 'Ace']
# d -  ['Ace', 'Base', 'Captain']
# e -  ['Base', 'Captain']

print(">>>>>>>>")
print('c + d =', c+d)
print('c * 3 =', c*3)
print("'Test' + c[0] - " + "Test" + str(c[0]))

# Output:
# >>>>>>>>>>
# c + d = [70, 75, 80, 85, 1000, 10000, 'Ace', 'Base', 'Captain']
# c * 3 = [70, 75, 80, 85, 70, 75, 80, 85, 70, 75, 80, 85]
# 'Test' + c[0] - Test70

print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# Output:
# True
# [70, 75, 80, 85]
# [70, 75, 80, 85]

temp = c
print(temp, c)
print(id(c))
print(id(temp))
print(c == temp)

#Output:
# [70, 75, 80, 85] [70, 75, 80, 85]
# 1865213196864
# 1865213196864
# True

print(c)
print(temp)
print(id(c))
print(id(temp))

#Output:
# [70, 75, 80, 85]
# [70, 75, 80, 85]
# 1865213196864
# 1865213196864

print(">>>>>>>>")
c[0] = 4
print('c-', c)

c[1:2] = ['a', 'b', 'c'] 
print(c)

c[1:2] = [['a', 'b', 'c']]
print(c)

# Output:
# >>>>>>>>
# c- [4, 75, 80, 85]
# [4, 'a', 'b', 'c', 80, 85]
# [4, ['a', 'b', 'c'], 'b', 'c', 80, 85]

c[1:3] = []
print(c)
del c[2]
print(c)

# Output:
# [4, 'c', 80, 85]
# [4, 'c', 85]

a = [5, 2, 3, 1, 4]
print('a - ', a)
a.append(10)
print('a - ', a)

# Output:
# a -  [5, 2, 3, 1, 4]
# a -  [5, 2, 3, 1, 4, 10]

a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)

a1 = [3, 5, 2]
a1.reverse()
print('a1 - ', a1)


# Output:
# a -  [1, 2, 3, 4, 5, 10]
# a -  [10, 5, 4, 3, 2, 1]
# a1 -  [2, 5, 3]

a = [10, 4, 1, 3, 2, 5]
print('a - ', a.index(1))
print('a - ', a[5])
a.insert(2, 7)
print('a - ', a)

# Output:
# a -  5
# a -  5
# a -  [10, 4, 7, 1, 3, 2, 5]

del a[6]
print(a)

a.remove(1) 
print(a)

print(' a - ', a.pop())
print(' a - ', a)

# Output:
# [10, 4, 7, 1, 3, 2]
# [10, 4, 7, 3, 2]
#  a -  2
#  a -  [10, 4, 7, 3]

print('a - ', a.count(7))
ex = [8, 9]
a.extend(ex)
print('a - ', a)

# Output:
# a -  1
# a -  [10, 4, 7, 3, 8, 9]

while a:
    data = a.pop()
    print(data)

# Output:
# 9
# 8
# 3
# 7
# 4
# 10