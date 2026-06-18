n = 5

while n > 0:
    print(n)
    n = n - 1

# Output:
# 5
# 4
# 3
# 2
# 1

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)

print('Loop Ended.')

# Output:
# 4
# 3
# Loop Ended.

n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print("else out.")

# Output:
# 9
# 8
# 7
# 6
# 5

a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'

i = 0

while i < len(a):
    if a[i] == s:
        print(s, "found in list")
        break
    i += 1
else:
    print(s, "not found in list")

# Output:
# qux found in list

a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop())

# Output:
# baz
# bar
# foo