a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'ace', 'base', 'captain']
e = [1000, 10000, ['ace', 'base', 'captain']]

print('>>>>>>>>')
print('d -', type(d), d)
print('d -', d[1])
print(d[0] + d[1] + d[1])
print(d[-1])
print(e[-1][1])
print(type(e[-1][1]))
print(list(e[-1][1]))

print(d[0:3])
print(d[2:])
print(e[2][1:3])

print(c+d)
print(c*3)
print('test' + str(c[0]))
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

temp = c
print(temp, c)
print(id(c))
print(id(temp))
print(c == temp)

c[1] = 200
print(c)
print(temp)
print(id(c))
print(id(temp))

c = [70, 75, 80, 85]
c[0] = 4
print(c)
c[1:2] = ['a', 'b', 'c'] # c[1:2]は、cの1番目から1番目までを意味します。つまり、c[1]を意味します。
print(c)
c[1:2] = [['a', 'b', 'c']]
print(c)

c[1:3] = []
print(c)
del c[2]
print(c)

a = [5, 2, 3, 1, 4, 10]
a.sort()
print(a)
a.reverse()
print(a)

a = [10, 4, 7, 1, 3, 2, 5]

del a[6]
print(a)

a.remove(1) # a.remove(1)は、aの中から1を削除することを意味します。
print(a)

# pop() は、リストの末尾の要素を削除して、その値を返すメソッドです。
print(a.pop())
print(a)

print(a.count(7))  # a.count(7)は、aの中に7がいくつあるかを数えることを意味します。
ex = [8, 9]
a.extend(ex)
print(a)

while a:
    data = a.pop()
    print(data)