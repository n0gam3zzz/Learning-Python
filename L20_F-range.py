# written by zyf in 2022/7/7 20:33
# range函数 或 range变量
# 生成一个迭代器
# 使用list函数查看迭代结果，为整数序列

# 1. range(num)
# 生成一个 [0, num) 步长为1的迭代器
l1 = range(10)
print(l1, type(l1))
print(list(l1))

# 2. range(min, max)
# 生成一个 [min, max) 步长为1的迭代器
l2 = range(10, 15)
print(l2, type(l2))
print(list(l2))

# 3. range(min, max, step)
# 生成一个 [min, max) 步长为step的迭代器
l3 = range(0, 101, 10)
print(l3, type(l3))
print(list(l3))
l4 = range(100, -101, -10)
print(l4, type(l4))
print(list(l4))
