str1 = "I am Python."
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4), sep="\n")
print(len(str1), len(str2), len(str3), len(str4), sep="\n")

# 空文字列
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

print("I'm a boy")
print('I\'m a boy')
print('I\\m a boy')

print('a \t b')
print('a \n b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
escape_str2 = "What\'s on TV?"
print(escape_str1)
print(escape_str2)

t_s1 = "Click \tStart!"
t_s2 = "New Line\n Check!"
print(t_s1)
print(t_s2)

raw_s1 = r'D:\Python\python3' # rをつけると、\をエスケープ文字として認識しない。つまり、\tはタブではなく、\とtの2文字として認識される。
raw_s2 = r'D:\tPython\python3'

print(raw_s1)
print(raw_s2)

print("C:\\Users\\Student") #\をエスケープ文字として認識させるために、\\とする必要がある。つまり、\\は\という1文字として認識される。
print(r"C:\Users\Student") # rをつけると、\をエスケープ文字として認識しない。つまり、\UはUnicodeエスケープシーケンスの開始ではなく、\とUの2文字として認識される。

# '''←これを一つ下の行にするとエラーが出る \にすると改行無視になるので、'''を一つ下の行にしてもエラーは出ない。
multi_str = ''' 
String
Multiline
Test
'''
print(multi_str)

multi_str = \
'''
String
Multiline
Test
'''
print(multi_str)

str_o1 = 'Python'
str_o2 = "Apple"
str_o3 = "Show are you doing?"
str_o4 = 'Tokyo Kyoto Osaka Okinawa'

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('z' in str_o1)
print('P' not in str_o2)

print(str(77))
print(type(str(77)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))
print(str(complex(12)), type(str(complex(12))))

str_o1 = 'python'

print('capitalize: ', str_o1.capitalize())
print('endswith: ', str_o2.endswith('s'))
print("replace1: ", str_o1.replace('thon', ' Good'))
print('sorted: ', sorted(str_o1)) # 文字列をアルファベット順に並べたリストを返す。
print("split: ", str_o4.split(' ')) # 文字列をスペースで分割してリストを返す。

im_str = "Good Boy!"
print(dir(im_str)) #__iter__というイテレータを返すメソッドがあることがわかる。つまり、文字列は繰り返し処理ができるオブジェクトであることがわかる。

for i in im_str:
    print(i)

str_slice = "Nice Python"
print(len(str_slice))

print(str_slice[0:3])
print(str_slice[5:11])
print(str_slice[5:])
print(str_slice[:])
print(str_slice[:len(str_slice)])
# print(str_slice[])

code = 'a'
print(ord(code))
print(chr(97))

s = "Python is a programming language that lets you work quickly\nand\nintegrate systems more effectively."
print(s)

s = '\'Python\' is a programming language that lets you work quickly\nand\nintegrate systems more effectively.'
print(s)