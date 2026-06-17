a = 75
b = 40
c = 10

print('and : ', a > b and b > c)
print('or : ', a > b or b > c)
print('not : ', not (a > b))    
print('not : ', not (b > c))
print(not True)
print(not False)

# Output
# and :  True
# or :  True
# not :  False
# not :  False
# False
# True

print('e1 : ', 3 + 12 > 7 + 3)
print('e2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10)

# Output
# e1 :  True
# e2 :  False
# e3 :  True
# e4 :  False

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("Pass.")
else:
    print("Fail.")

# Output
# Pass.

id1 = "vip"
id2 = "admin"
grade = 'platinum'

if id1 == "vip" or id2 == "admin" :
    print("管理者認証")

if id2 == "admin" and grade == "platinum":
    print("最上位の管理者")

# Output
# 管理者認証
# 最上位の管理者

num = 75

if num >= 80:
    print("Grade : A")
elif num >= 70:
    print("Grade : B")
elif num >= 60:
    print("Grade : C")
else:
    print("不合格")

# Output
# Grade : B

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

# Output
# 奨学金 100%

q = [10, 20, 30]
w = {70, 80, 90, 90}
e = {"name": 'Lee', "city": "tokyo", "grade" : 'A'}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print('name' in e)
print("tokyo" in e.values())

# Output
# False
# True
# False
# True
# True

# for num in range(100):
#     print(num)

for i in range(5):
    print(i)
else:
    print("終了")

for i in range(5):
    print(i)
    if i == 3:
        break;
else:
    print("終了")

for v1 in range(10):
    print("V1 is :", v1)

sum1 = 0

for v in range(1, 1001):
    sum1 += v

print("1 ~ 1000 sum : ", sum1)
# Output
# 1 ~ 1000 sum :  500500

print("1 ~ 1000 sum : ", sum(range(1, 1001)))
# Output
# 1 ~ 1000 sum :  500500

# f-string : 文字列の中に変数を埋め込むことができる機能

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j : 2d}", end = ' ')
    print()

name = 'America'
print('reverse : ', reversed(name))
