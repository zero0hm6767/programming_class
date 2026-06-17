
cor = int(input("掛け算九九のどの段を計算しましょうか？"))
print("掛け算九九", cor, "段を計算します。")
for i in range(1, 10):
    # print(f"{cor} × {i} = {cor * i : 2d}")
    print(cor, "×", i, "=", cor * i)
