keys = input("keyとなる文字列を3つ入力しなさい: ").split()
values = map(float, input("valueとなる実数を3つ入力しなさい: ").split())

dict = dict(zip(keys, values))
print(dict)