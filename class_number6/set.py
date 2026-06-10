# 集合型set

# s = set([1, 2, 3, 4, 5])
# s.add(6)
# print(s)

# s.remove(1)
# print(s)

# # updateは複数の要素を追加することができる
# s.update([7])
# print(s)

# # 定義された要素より大きい値を追加することもできる
# # ただし、重複する値は追加されない
# s.update([2, 3, 4, 10, 11, 12])
# print(s)

# s.discard(2)
# print(s)
# s.clear()
# print(s)

a = set()
print(a)
print(type(a))

# Output
# set()
# <class 'set'>

b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', "plate"])
e = {'foo', 'bar', 'baz', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# Output
# a -  <class 'set'> set()
# b -  <class 'set'> {1, 2, 3, 4}
# c -  <class 'set'> {1, 4, 5, 6}
# d -  <class 'set'> {1, 2, 'Cap', 'Pen', 'plate'}
# e -  <class 'set'> {'bar', 'foo', 'baz', 'qux'}
# f -  <class 'set'> {3.14159, 'foo', 42, (1, 2, 3)}

b = set([1, 2, 3, 4, 4, 4])
print('b - ', type(b), b)

print(2 in a)
print(2 in b)

# Ouptut
# b -  <class 'set'> {1, 2, 3, 4}
# False
# True

t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# Output
# t -  <class 'tuple'> (1, 2, 3, 4)
# t -  1 (2, 3)

l = list(c)
l2 = list(e)
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])
print('l2 - ', type(l2), l2)

# Output
# l -  1 [4, 5]
# l2 -  <class 'list'> ['foo', 'baz', 'bar', 'qux']

print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
# Output
# 0
# 4
# 4
# 5
# 4
# 4

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('intersection - ', s1 & s2) #積集合
print('intersection - ', s1.intersection(s2)) #積集合

# Output
# intersection -  {4, 5, 6}
# intersection -  {4, 5, 6}

print('union - ', s1 | s2) #和集合
print('union - ', s1.union(s2)) #和集合

# Output
# union -  {1, 2, 3, 4, 5, 6, 7, 8, 9}
# union -  {1, 2, 3, 4, 5, 6, 7, 8, 9}

print('difference - ', s1 - s2) #差集合
print('difference - ', s1.difference(s2)) #差集合

# Output
# difference -  {1, 2, 3}
# difference -  {1, 2, 3}

print('s1 s2', s1.isdisjoint(s2)) #s1とs2は共通の要素がないか

# Output
# s1 s2 False

#s1はs2の部分集合か

print('s1 <= s2 -', s1.issubset(s2)) 
print('s1 <= s2 -', s1 <= s2)

print('s1 >= s2 -', s1.issuperset(s2)) #s1はs2の上位集合か
print('s1 >= s2 -', s1 >= s2)

# Output
# s1 <= s2 - False
# s1 <= s2 - False
# s1 >= s2 - False
# s1 >= s2 - False

s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)

s1.discard(3)
print('s1 - ', s1)

s1.clear()
print(s1)

# Output
# s1 -  {1, 2, 3, 4, 5}
# s1 -  {1, 3, 4, 5}
# s1 -  {1, 4, 5}
# set()