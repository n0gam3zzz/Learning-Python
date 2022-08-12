# written by zyf in 2022/7/9 16:01
# 列表生成式
# [(关于i的表达式) for i in (可迭代对象)]

# 生成x为1-10的列表，y为x^2的列表
x = list(range(1, 11))
print("x:", x, id(x))
y = [i*i for i in x]
print("y:", y, id(y))

# 生成z为1/(1-e^-x)在[-10, 10]的列表
x = list(range(-10, 11))
print("x:", x)
e = 2.17281728
z = [1/(1+e**(-i)) for i in x]
print("z:", z)

# 生成全为233的列表
lst = [233 for i in range(10)]
print(lst)
