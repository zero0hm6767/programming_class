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

print(dir(d))
for i in d.keys():
    print(i)

for i in d.values():
    print(i)

# tuple型で返す
for i in d.items():
    print(i)

print('a - ', a)
print('a - ', 'birth' in a)
print(' a- ', 'birth2' in a)

a['test'] = 'hello test'
print('a - ', a)

a['birth'] = 900123
print('a - ', a)

# split()は文字列を指定した区切りで分割してリストで返す

# a, b = input('文字列を2つ入力してください: ').split()
# print(a)
# print(b)

# a, b = input('文字列を2つ入力してください: ').split(',')
# print(a)
# print(b)

# a, b = map(int, input('数字を2つ入力してください: ').split(','))
# print(a + b)

scores = [60, 70, 80]
#lambdaは無名関数を作るためのキーワード。引数と式を指定することで、簡単に関数を定義できる。
#mapはリストの各要素に対して、指定した関数を適用するための関数。第一引数に関数、第二引数にリストを指定する。
new_scores = list(map(lambda x: x + 10, scores)) 
print(new_scores)

words = ['python', 'java', 'c']
# str.upperは文字列を大文字に変換するためのメソッド。mapを使って、wordsの各要素を大文字に変換する。
# listにint型があると、mapはint型に対してstr.upperを適用しようとするため、エラーが発生する。
upper_words = list(map(str.upper, words))
print(upper_words)

#zipは複数のリストを同じ位置の要素同士を組み合わせるための関数。第一引数に複数のリストを指定する。
d2 = dict(zip(['name', 'age'], ['niceman', 20]))
print(d2)

name = ['taro', 'hanako', 'mike']
age = [10, 20, 30]

for n, a in zip(name, age):
    print(n, a)