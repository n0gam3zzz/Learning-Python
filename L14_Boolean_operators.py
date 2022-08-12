# written by zyf in 2022/7/7 16:25
# 布尔运算符（逻辑运算符）
a, b = 2, 3
# 1 and 与
print("1. and")
print(True and True)
print(a == 2 and b == 3)
print(a == 1 and b == 3)
print(a == 1 and b == 2)
# 2 or 或
print("2. or")
print(True or False)
print(a == 2 or b == 3)
print(a == 1 or b == 3)
print(a == 1 or b == 2)
# 3 not 非
print("3. not")
print(not 1)
print(not 0)
# 4 in, not in 是否在其中
print("4. in, not in")
s = "ABC"
print('A' in s)
print('D' in s)
print('A' not in s)
print('D' not in s)
n = [1, 2]
print(1 in n)
print(3 in n)
