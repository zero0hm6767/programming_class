a = int(3.5)
b = float(3.5)
c = str(3.5)
print(a, b, c, sep="\n")

print(type(a), type(b), type(c), sep="\n")

"""
シーケンスとは 複数の値をまとめて扱うことができるデータ型のこと。
int : 整数
float : 浮動小数点数
complex : 複素数
bool : 真偽値
str : 文字列(シーケンス)
list : リスト(シーケンス)
tuple : タプル(シーケンス)
set : 集合
dict : 辞書
"""

str1 = "Python"
bool_v = True
str2 = "Anaconda"
float_v = 10.0
int_v = 7
list_v = [str1, str2]
print(list_v)

z = 2+3j
print(z, type(z))
print(z.real, z.imag)