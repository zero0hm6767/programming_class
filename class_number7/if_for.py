print(type(True))
print(type(False))
print(bool([]))

# Output
# <class 'bool'>
# <class 'bool'>
# False

if True:
    print("Good")

if False:
    print("Bad")

if '':
    print("Bad")

if 'a':
    print("Good")

# Output
# Good
# Good

if False:
    print("Bad")
else:
    print("Good")

if True:
    print("Bad")
else:
    print("Good")

# Output
# Good
# Bad

x = 15
y = 10

print(x == y)
print (x != y)
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)

# Output
# False
# True
# True
# True
# False
# False

city =""
if city:
    print("You are in:", city)
else:
    print("Please enter your city")

city = "Tokyo"
if city:
    print("You are in:", city)
else:
    print("Please enter your city")

# Output
# Please enter your city
# You are in: Tokyo

a = 75
b = 40
c = 10

print('and : ', a > b and b > c)
print('or : ', a > b or b > c)
print('not : ', not (a > b))    
print('not : ', not (b > c))
print(not True)
print(not False)

# # Output
# # and :  True
# # or :  True
# # not :  False
# # not :  False
# # False
# # True

print('e1 : ', 3 + 12 > 7 + 3)
print('e2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10)

# # Output
# # e1 :  True
# # e2 :  False
# # e3 :  True
# # e4 :  False

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("Pass.")
else:
    print("Fail.")

# # Output
# # Pass.

id1 = "vip"
id2 = "admin"
grade = 'platinum'

if id1 == "vip" or id2 == "admin" :
    print("管理者認証")

if id2 == "admin" and grade == "platinum":
    print("最上位の管理者")

# # Output
# # 管理者認証
# # 最上位の管理者

num = 75

if num >= 80:
    print("Grade : A")
elif num >= 70:
    print("Grade : B")
elif num >= 60:
    print("Grade : C")
else:
    print("不合格")

# # Output
# # Grade : B

grade = 'S'
total = 95

if grade == "S":
    if total >= 90:
        print("奨学金 100%")
    elif total >= 80:
        print("奨学金 80%")
    else:
        print("奨学金 70%")
else:
    print("奨学金 50%")

# # Output
# # 奨学金 100%

q = [10, 20, 30]
w = {70, 80, 90, 90}
e = {"name": 'Lee', "city": "tokyo", "grade" : 'A'}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print('name' in e)
print("tokyo" in e.values())

# # Output
# # False
# # True
# # False
# # True
# # True

for v1 in range(10):
    print("V1 is :", v1)

# Output
# V1 is : 0
# V1 is : 1
# V1 is : 2
# V1 is : 3
# V1 is : 4
# V1 is : 5
# V1 is : 6
# V1 is : 7
# V1 is : 8
# V1 is : 9

for v2 in range(1, 11):
    print("V2 is :", v2)

#  Output
# V2 is : 1
# V2 is : 2
# V2 is : 3
# V2 is : 4
# V2 is : 5
# V2 is : 6
# V2 is : 7
# V2 is : 8
# V2 is : 9
# V2 is : 10

for v3 in range(1, 11, 2):
    print("V3 is :", v3)

# Ouptut
# V3 is : 1
# V3 is : 3
# V3 is : 5
# V3 is : 7
# V3 is : 9

for v3 in range(1, 11, 3):
    print("V3 is :", v3)

# Output
# V3 is : 1
# V3 is : 4
# V3 is : 7
# V3 is : 10

# # for num in range(100):
# #     print(num)

# for i in range(5):
#     print(i)
# else:
#     print("終了")

# for i in range(5):
#     print(i)
#     if i == 3:
#         break;
# else:
#     print("終了")

# for v1 in range(10):
#     print("V1 is :", v1)

sum1 = 0

for v in range(1, 1001):
    sum1 += v

print("1 ~ 1000 sum : ", sum1)
# Output
# 1 ~ 1000 sum :  500500

print("1 ~ 1000 sum : ", sum(range(1, 1001)))
# # Output
# # 1 ~ 1000 sum :  500500

print('1 ~ 1000 4の倍数の合計: ', sum(range(4, 1001, 4)))

sum1 = 0
for v in range(4, 1001, 4):
    print(v)
    sum1 += v

# Output
# 4
# 8
# 12
# 16
# ...
# 1000

names = ["Sato", "Suzuki", "Takahashi", "Tanaka", "Watanabe"]
for n in names:
    print("You are :", n)

# Output
# You are : Sato
# You are : Suzuki
# You are : Takahashi
# You are : Tanaka
# You are : Watanabe

lotto_numbers = [11, 19, 21, 28, 36, 37]

for number in lotto_numbers:
    print("Current number : ", number)

# Output
# Current number :  11
# Current number :  19
# Current number :  21
# Current number :  28
# Current number :  36
# Current number :  37

word = 'Beautiful'
for n in word:
    print("word : ", n)

# Output
# word :  B
# word :  e
# word :  a
# word :  u
# word :  t
# word :  i
# word :  f
# word :  u
# word :  l

my_info = {
    "Name": "Yamaguchi",
    "Age": 20,
    "City": "Tokyo"
}

for key in my_info:
    print("key :", key)

# Output
# key : Name
# key : Age
# key : City

for key in my_info:
    print(key, ":", my_info[key])

# Output
# Name : Yamaguchi
# Age : 20
# City : Tokyo

for key in my_info:
    print(key, ":", my_info.get(key))

# Output
# Name : Yamaguchi
# Age : 20
# City : Tokyo

for key, value in my_info.items():
    print(key, ":", value)

# Output
# Name : Yamaguchi
# Age : 20
# City : Tokyo

for v in my_info.values():
    print("value : ", v)

# Output
# value :  Yamaguchi
# value :  20
# value :  Tokyo

for k in my_info.keys():
    print("key : ", k)

# Output
# key :  Name
# key :  Age
# key :  City

name = "FineApplE"

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# Output
# F
# I
# N
# E
# A
# P
# P
# L
# E

for n in name:
    if n.islower():
        print(n)
    else:
        print(n.lower())

# Output
# f
# i
# n
# e
# a
# p
# p
# l
# e

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 17:
        print("Found : 17!")
        break
    else:
        print("Not found :", num)

# Output
# Not found : 14
# Not found : 3
# Not found : 4
# Not found : 7
# Not found : 10
# Not found : 24
# Found : 17!

con = ["1", 2, 5, True, 4.3, complex(4)]

for v in con:
    if type(v) is bool:
        continue
    print("Current type : ", v , type(v))

# Output
# Current type :  1 <class 'str'>
# Current type :  2 <class 'int'>
# Current type :  5 <class 'int'>
# Current type :  4.3 <class 'float'>
# Current type :  (4+0j) <class 'complex'>

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 45:
        print("Found : 45!")
        break
else:
        print("Not Found 45...")

# Output
# Not Found 45...

for num in numbers:
    if num == 34:
        print("Found : 34!")
        break
else:
        print("Not Found 34...")

# Output
# Not Found 34...
# Found : 34!

# # f-string : 文字列の中に変数を埋め込むことができる機能

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j : 2d}", end = ' ')
    print()

# Output
# 3 * 1 =  3 3 * 2 =  6 3 * 3 =  9 3 * 4 =  12 3 * 5 =  15 3 * 6 =  18 3 * 7 =  21 3 * 8 =  24 3 * 9 =  27 
# 4 * 1 =  4 4 * 2 =  8 4 * 3 =  12 4 * 4 =  16 4 * 5 =  20 4 * 6 =  24 4 * 7 =  28 4 * 8 =  32 4 * 9 =  36 
# 5 * 1 =  5 5 * 2 =  10 5 * 3 =  15 5 * 4 =  20 5 * 5 =  25 5 * 6 =  30 5 * 7 =  35 5 * 8 =  40 5 * 9 =  45 
# 6 * 1 =  6 6 * 2 =  12 6 * 3 =  18 6 * 4 =  24 6 * 5 =  30 6 * 6 =  36 6 * 7 =  42 6 * 8 =  48 6 * 9 =  54 
# 7 * 1 =  7 7 * 2 =  14 7 * 3 =  21 7 * 4 =  28 7 * 5 =  35 7 * 6 =  42 7 * 7 =  49 7 * 8 =  56 7 * 9 =  63 
# 8 * 1 =  8 8 * 2 =  16 8 * 3 =  24 8 * 4 =  32 8 * 5 =  40 8 * 6 =  48 8 * 7 =  56 8 * 8 =  64 8 * 9 =  72 
# 9 * 1 =  9 9 * 2 =  18 9 * 3 =  27 9 * 4 =  36 9 * 5 =  45 9 * 6 =  54 9 * 7 =  63 9 * 8 =  72 9 * 9 =  81 

name = 'Aceman'

print('reverse : ', reversed(name))
print("List : ", list(reversed(name)))
print("Tuple : ", tuple(reversed(name)))
print("Set : ", set(reversed(name)))

# Ouptut
# reverse :  <reversed object at 0x0000015D9E4C0FA0>
# List :  ['n', 'a', 'm', 'e', 'c', 'A']
# Tuple :  ('n', 'a', 'm', 'e', 'c', 'A')
# Set :  {'e', 'n', 'm', 'c', 'A', 'a'}