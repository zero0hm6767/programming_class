print("Quiz(1) : 3.11 python 200を1行に出力する正しい方法は?")

print("回答 : ➃", end = "\n")
print(3.11, 'Python', 200)

print(" ")
print("Quiz(2) : 15:8を出力する正しい方法は?")

print("回答 : ➂", end = "\n")
print(15, 8, sep=':')

print(" ")
print("Quiz(3) : HelloとPythonを2行で出力する正しい方法をすべて選べ")

print("回答 : ➁, ➃, ➄", end = "\n")
print("➁")
print("hello\npython")
print("➃")
print("hello", "python", sep="\n")
print("➄")
print("hello", "\n","python", sep="")

print(" ")
print("Quiz(4) : 2026/4/23 11:40:30を出力する正しい方法は?")

year = 2026
month = 4
day = 23
hour = 11
minute = 40
second = 30

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')