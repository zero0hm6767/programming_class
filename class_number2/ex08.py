# 宣言の英語って何？　→　Declaration

# 宣言
def declaration():
    n = 700
    print(n)
    print(type(n)) # nのデータ型を表示します。intは整数を表すデータ型です。

# 同時宣言
def same_timing_declaration():
    x = y = z = 700
    print(x, y, z)

# 再宣言
def re_declaration():
    var = 75
    var = "change value"
    print(var)
    print(type(var)) # varのデータ型を表示します。intは整数を表すデータ型です。


# object references
def object_references():
    print(300)
    print(int(300.1234)) # int()は、引数を整数に変換する関数です。

# 総合
def re_declaration2():
     n = 777 
     print(n,type(n))
     print()

     m = n

     print(m, n)
     print(type(m), type(n))

     m = 400

     print(m, n)
     print(type(m), type(n))

def main():
    declaration()
    same_timing_declaration()
    re_declaration()
    object_references()
    re_declaration2()

if __name__ == "__main__":
    main()