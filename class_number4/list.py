# 変数を100こ管理するためにリスト型を使う

mi = ['a', 'b', 'c']

print(mi[1],
mi[-1],
mi[-2])

# append() は、リストの末尾に要素を追加するメソッドです。
# extend() は、リストに複数の要素を追加するメソッドです。
# insert() は、リストの指定した位置に要素を挿入するメソッドです。
# remove() は、リストから指定した要素を削除するメソッドです。
# del は、リストから指定した位置の要素を削除するキーワードです。
color1 = ['red', 'green', 'blue']
color2 = ['orange', 'black', 'white']

color1.append('yellow')
color1.extend(["black", "purple"])
color1.insert(1, 'pink')
print(color1)

color1.remove('green')
print(color1)

del color1[0]
print(color1)
# pythonのリストは様々なデータ型を格納できるため、リストの中にリストを入れることもできます。    
