def swap_offset(offset_x, offset_y):
    temp = a[offset_x]
    a[offset_x] = a[offset_y]
    a[offset_y] = temp

a = [1, 2, 3, 4, 5]
print(a)
swap_offset(1, 2)
print(a)

# Output:
# [1, 2, 3, 4, 5]
# [1, 3, 2, 4, 5]

def swap_reference(list_ex, offset_x, offset_y):
    temp = list_ex[offset_x]
    list_ex[offset_x] = list_ex[offset_y]
    list_ex[offset_y] = temp

a = [1, 2, 3, 4, 5]
print(a)
swap_reference(a, 1, 2)
print(a)

# Output:
# [1, 2, 3, 4, 5]
# [1, 3, 2, 4, 5]

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(int(input("整数を入力してください:"))))

# Output:
# 整数を入力してください:3
# 6

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)
print(x, y, z)

# Output:
# 100 200 300


def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)
print(type(q), q, list(q))

# Output:
# <class 'tuple'> (200, 400, 600) [200, 400, 600]


def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mul2(30)
print(type(p), p, set(p))
# Output:
# <class 'list'> [300, 600, 900] {600, 900, 300}

def args_func(*args):
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')

args_func('Yamaguchi')
args_func('Yamaguchi', 'Iguchi')
args_func('Yamaguchi', 'Iguchi', 'Iwamura')

# Output:
# Result : 0 Yamaguchi
# -----
# Result : 0 Yamaguchi
# Result : 1 Iguchi
# -----
# Result : 0 Yamaguchi
# Result : 1 Iguchi
# Result : 2 Iwamura
# -----

def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-----')

kwargs_func(name1 = 'Yamaguchi')
kwargs_func(name1 = 'Yamaguchi', name2 = 'Iguchi')
kwargs_func(name1 = 'Yamaguchi', name2 = 'Iguchi', name3 = 'Iwamura')

# Output:
# name1 Yamaguchi
# -----
# name1 Yamaguchi
# name2 Iguchi
# -----
# name1 Yamaguchi
# name2 Iguchi
# name3 Iwamura
# -----

def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Yamaguchi', 'Iguchi', age1=20, age2=30, age3=50)

# Output:
# 10 20 ('Yamaguchi', 'Iguchi') {'age1': 20, 'age2': 30, 'age3': 50}

def mul_func(x, y):
    return x * y
q = mul_func(10, 50)
print(q)

# Output:
# 500

mul_func_var = mul_func
print(mul_func_var(10, 50))

# Output:
# 500

lambda_mul_func = lambda x, y: x * y
print(lambda_mul_func(50, 50))

# Output:
# 2500

def func_final(x, y, func):
    print('>>>', x * y * func(100, 100))

func_final(10, 20, lambda x, y : x * y)
func_final(10, 20, lambda_mul_func)
func_final(10, 20, mul_func_var)

# Output:
# >>> 2000000
# >>> 2000000
# >>> 2000000