# written by zyf in 2022/7/7 23:59
# for in 循环

# for (变量) in (可迭代对象):
#    (code1)

# 每次循环将可迭代对象中的下一个赋值给变量
# 可迭代对象包括 string, range, list

# 1. 需要用到变量
for i in "ABCDE":
    print(i)
print('\n')

for i in range(11):
    print(i)
print('\n')

for i in [1, 4, 9, 16, 25]:
    print(i)
print('\n')

# 2. 不需要用到变量，循环n次
# 变量写为下划线_
for _ in range(5):
    print("输出五次。")
print('\n')
