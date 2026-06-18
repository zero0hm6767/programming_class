def f():
    global t
    t = "I love Kyoto!"
    print(t)

t = "I love Tokyo!"
f()
print(t)

def calculate(x, y):
    total = x + y
    print("In Function")
    print("a: ", str(a), "b:", str(b),
          "a+b:", str(a+b), "Total:", str(total))
    return total

a = 5
b = 7

total = 0

print("In Program")
print("a:", str(a), "b:", str(b), "a+b:", str(a+b))
sum = calculate(a, b)
print("After calculation")
print("Total:", str(total), "Sum:", str(sum))