
# StackはLIFO最後に格納されたデータが最初に取り出される
# push データを入れる
# pop データを取り出す

# Queue
# FIFO最初に格納したデータが最初に取り出される
# append()
# pop(0)

a = []
a.append(3)
print(a)
a.append(12)
print(a)
a.append(16)
print(a)
a.pop() 
print(a)
a.pop()
print(a)

# Output:
# [3]
# [3, 12]
# [3, 12, 16]
# [3, 12]
# [3]

a = []
a.append(3)
print(a)
a.append(12)
print(a)
a.append(16)
print(a)
a.pop(0) 
print(a)
a.pop(0)
print(a)

# Output:
# [3]
# [3, 12]
# [3, 12, 16]
# [12, 16]
# [16]