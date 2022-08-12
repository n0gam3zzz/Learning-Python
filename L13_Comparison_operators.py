# written by zyf in 2022/7/7 15:50
# 比较运算符
# 1 比较值
a, b, c = 1, 2, 2
print("a = ", a, "b = ", b)
print("a<b?", a < b)
print("a<=b?", a <= b)
print("a=b?", a == b)
print("a>b?", a > b)
print("a>=b?", a >= b)
print("a!=b?", a != b)
# 2 比较标识（ID、地址）
# 2.1
x = 10
y = 10
# 为了节省内存，x和y均指向同一个10
print(x == y)
print(id(x), id(y))
print(x is y)  # 比较ID是否相等
print(x is not y)  # 比较ID是否不相等
# 2.2
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(id(x), id(y))
print(x is y)  # 比较ID是否相等
print(x is not y)  # 比较ID是否不相等
