# 集合型set

s = set([1, 2, 3, 4, 5])
s.add(6)
print(s)

s.remove(1)
print(s)

# updateは複数の要素を追加することができる
s.update([7])
print(s)

# 定義された要素より大きい値を追加することもできる
# ただし、重複する値は追加されない
s.update([2, 3, 4, 10, 11, 12])
print(s)

s.discard(2)
print(s)
s.clear()
print(s)

s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])
print(s1.union(s2)) #和集合
print(s1 | s2) #和集合

print(s1.intersection(s2)) #積集合
print(s1 & s2) #積集合

