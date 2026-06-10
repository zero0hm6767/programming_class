keys = input("keyとなる文字列を3つ入力しなさい: ").split()
values = map(float, input("valueとなる実数を3つ入力しなさい: ").split())

dict = dict(zip(keys, values))
print(dict)

# Output
# keyとなる文字列を3つ入力しなさい: health attack speed
# valueとなる実数を3つ入力しなさい: 310.5 18.5 230.2
# {'health': 310.5, 'attack': 18.5, 'speed': 230.2}