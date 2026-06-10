a = "abcde"
print(a[0], a[4]) # a e
print(a[-1], a[-5]) # e a

a = "TOKYO KOSEN"
print(a[0:4]) # 0~3文字目まで
print(a[0:5]) # 0~4文字目まで
print(a[-5:]) # 後ろから5文字目から最後まで
print(a[:]) # すべての文字
print(a[-50:50]) # 後ろから50文字目から前から50文字目まで
print(a[::2]) # 0~最後まで、2文字おきに
print(a[::-1]) # 0~最後まで、-1文字おきに（逆順）
print(a[::1]) # 0~最後まで、1文字おきに（すべての文字）
print(a[2::2]) # 2~最後まで、2文字おきに
print(a[::-2]) # 0~最後まで、-2文字おきに（逆順で2文字おき）

a = "hello"
b = "world"

print(a+b)
print(a+" "+b)
print(a*2 + " " + b*2)

print("e" in a)
print("x" in a)
print(len(a))

a = "ABC\tDEF" # \tはtabを入れる
print(a)
a = "ABC\t\tDEF"
print(a)

a = "abc\'DEF"
print(a)
a = "abc\'\'DEF"
print(a)

a = "abc\"DEf"
print(a)
a = "ABC\"\"DEf"
print(a)

a = 'ABC\bDEF' # \bはバックスペースを入れる。つまり、Cが消える。
print(a)
a = 'ABC\b\bDEF'# \bを2回入れると、Bも消える。
print(a)

a = "ABC\nDEF" # \nは改行を入れる
print(a)
a = 'ABC\n\nDEF' # \nを2回入れると、改行も2回入る。
print(a)