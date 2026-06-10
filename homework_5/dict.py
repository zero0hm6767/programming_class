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

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)   
print('e - ', type(e), e)
print('f - ', type(f), f)

print('a - ', a['name'])
print('a - ', a.get('name')) #getを使うとキーがない場合にNoneを返す

a['address'] = 'Tokyo'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# a = input("1番目の数字")
# b = input("2番目の数字")
# print(a + b)

a = tuple([1, 2, 3, 4])
print(type(a))