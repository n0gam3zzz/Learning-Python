# written by zyf in 2022/7/7 16:41
# 位运算符
# 对于二进制数而言
a = 12  # 00001100b
b = 10  # 00001010b
# 1 位与 &
print(a & b)  # 与 结果为00001000b，即8d
# 2 位或 |
print(a | b)  # 或 结果为00001110b，即14d
# 3 左移 <<
# x << y # 对x左移y位
# 左移一位相当于*2
x = 0b00000001
print(x)
print(x << 1, x << 2, x << 3, x << 4, x << 5, x << 6, x << 7, x << 8, x << 9)
# 4 右移 >>
# x >> y # 对x右移y位
# 右移一位相当于/2，会截断
y = 0b10000000
print(y)
print(y >> 1, y >> 2, y >> 3, y >> 4, y >> 5, y >> 6, y >> 7, y >> 8, y >> 9)
