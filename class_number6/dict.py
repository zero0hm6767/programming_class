a = {'name': 'Yamaguchi', 'phone' : '080122345678', 'birth' : '900124'}
b = {0: 'Hello python!'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name' : 'Niceman',
    'City' : 'Tokyo',
    'Age' : 20,
    'Grade' : 'A',
    'Status' : True
}

print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))
print('d - ', list(d.keys()))

#Output 
# a -  dict_keys(['name', 'phone', 'birth'])
# b -  dict_keys([0])
# c -  dict_keys(['arr'])
# d -  dict_keys(['Name', 'City', 'Age', 'Grade', 'Status'])
# a -  ['name', 'phone', 'birth']
# b -  [0]
# c -  ['arr']
# d -  ['Name', 'City', 'Age', 'Grade', 'Status']

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())   
print('d - ', d.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))
print('d - ', list(d.values()))

# Output

# a -  dict_values(['Yamaguchi', '080122345678', '900124'])
# b -  dict_values(['Hello python!'])
# c -  dict_values([[1, 2, 3, 4]])
# d -  dict_values(['Niceman', 'Tokyo', 20, 'A', True])
# a -  ['Yamaguchi', '080122345678', '900124']
# b -  ['Hello python!']
# c -  [[1, 2, 3, 4]]
# d -  ['Niceman', 'Tokyo', 20, 'A', True]

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))
print('c - ', list(c.items()))
print('d - ', list(d.items()))

# Output
# a -  dict_items([('name', 'Yamaguchi'), ('phone', '080122345678'), ('birth', '900124')])
# b -  dict_items([(0, 'Hello python!')])
# c -  dict_items([('arr', [1, 2, 3, 4])])
# d -  dict_items([('Name', 'Niceman'), ('City', 'Tokyo'), ('Age', 20), ('Grade', 'A'), ('Status', True)])
# a -  [('name', 'Yamaguchi'), ('phone', '080122345678'), ('birth', '900124')]
# b -  [(0, 'Hello python!')]
# c -  [('arr', [1, 2, 3, 4])]
# d -  [('Name', 'Niceman'), ('City', 'Tokyo'), ('Age', 20), ('Grade', 'A'), ('Status', True)]


print(dir(d))
for i in d.keys():
    print(i)

for i in d.values():
    print(i)

# tuple型で返す
for i in d.items():
    print(i)

# Output
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__',  '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
# '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# Name
# City
# Age
# Grade
# Status
# Niceman
# Tokyo
# 20
# A
# True
# ('Name', 'Niceman')
# ('City', 'Tokyo')
# ('Age', 20)
# ('Grade', 'A')
# ('Status', True)

print('a -', a)
print('a - ', a.pop('name'))
print('a - ', a)

print('b - ', b)
print('b - ', b.pop(0))
print('b - ', b)

# Output
# a - {'name': 'Yamaguchi', 'phone': '080122345678', 'birth': '900124'}
# a -  Yamaguchi
# a -  {'phone': '080122345678', 'birth': '900124'}
# b -  {0: 'Hello python!'}
# b -  Hello python!
# b -  {}

print('c - ', c)
print('c - ', c.pop('arr'))
print('c - ', c)

print('d - ', d)
print('d - ', d.pop('Name'))
print('d - ', d)

# Output
# c -  {'arr': [1, 2, 3, 4]}
# c -  [1, 2, 3, 4]
# c -  {}
# d -  {'Name': 'Niceman', 'City': 'Tokyo', 'Age': 20, 'Grade': 'A', 'Status': True}
# d -  Niceman
# d -  {'City': 'Tokyo', 'Age': 20, 'Grade': 'A', 'Status': True}


e = dict([
    ('Name', 'Niceman'),
    ('City', 'Tokyo'),
    ('Age', 20),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name = 'Niceman',
    City = 'Tokyo',
    Age = 20,
    Grade = 'A',
    Status = True
)

print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)

# Output
# f -  {'Name': 'Niceman', 'City': 'Tokyo', 'Age': 20, 'Grade': 'A', 'Status': True}
# f -  ('Status', True)
# f -  {'Name': 'Niceman', 'City': 'Tokyo', 'Age': 20, 'Grade': 'A'}

a = dict(
    phone = "08012345678", 
    birth = "900124",
    address = 'Tokyo',
    rank = [1, 2, 3]
)

print('a - ', a)
print('a - ', 'birth' in a)
print('a - ', 'birth2' in a)

print('a - ', 'name' in a)
print('a - ', 'addr' in a)

# Output
# a -  True
# a -  False
# a -  False
# a -  False

a = {'phone' : '080122345678', 'birth' : '900124'}

print('a - ', a)

a['test'] = 'hello test'
print('a - ', a)

a['birth'] = 900123
print('a - ', a)

# Output
# a -  {'phone': '080122345678', 'birth': '900124'}
# a -  {'phone': '080122345678', 'birth': '900124', 'test': 'hello test'}
# a -  {'phone': '080122345678', 'birth': 900123, 'test': 'hello test'}

a.update(birth = '910123')
print('a - ', a)

temp = {'address' : "Kyoto"}
a.update(temp)
print('a - ', a)

# Output
# a -  {'phone': '080122345678', 'birth': '910123', 'test': 'hello test'}
# a -  {'phone': '080122345678', 'birth': '910123', 'test': 'hello test', 'address': 'Kyoto'}

# # split()は文字列を指定した区切りで分割してリストで返す

# a, b = input('文字列を2つ入力してください: ').split()
# print(a)
# print(b)

# a, b = input('文字列を2つ入力してください: ').split(',')
# print(a)
# print(b)

# Output
# 文字列を2つ入力してください: Hello Python
# Hello
# Python
# 文字列を2つ入力してください: Hello,Python
# Hello
# Python

# a = input('文字列を2つ入力してください: ').split(',')
# print(a)

# Output
# 文字列を2つ入力してください: Hello,Python
# ['Hello', 'Python']

# a, b = map(int, input('数字を2つ入力してください: ').split(','))
# print(a + b)

# Output
# 数字を2つ入力してください: 3,4
# 7

#lambdaは無名関数を作るためのキーワード。引数と式を指定することで、簡単に関数を定義できる。
#mapはリストの各要素に対して、指定した関数を適用するための関数。第一引数に関数、第二引数にリストを指定する。
# str.upperは文字列を大文字に変換するためのメソッド。mapを使って、wordsの各要素を大文字に変換する。
# listにint型があると、mapはint型に対してstr.upperを適用しようとするため、エラーが発生する。

scores = [60, 70, 80]
new_scores = list(map(lambda x: x + 10, scores)) 
print(new_scores)

words = ['python', 'java', 'c']
upper_words = list(map(str.upper, words))
print(upper_words)

# Output
# [70, 80, 90]
# ['PYTHON', 'JAVA', 'C']

# #zipは複数のリストを同じ位置の要素同士を組み合わせるための関数。第一引数に複数のリストを指定する。

d2 = dict(zip(['Name', 'Age'], ['Niceman', 20]))
print(d2)

# Output
# {'Name': 'Niceman', 'Age': 20}

# name = ['taro', 'hanako', 'mike']
# age = [10, 20, 30]

# for n, a in zip(name, age):
#     print(n, a)