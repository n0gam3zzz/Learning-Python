# written by zyf in 2022/7/7 14:45
# 赋值运算符
# 执行顺序为从右往左
a = 5 + 6 * 2  # 先计算等号右边数值，后赋值给a
print(a)
# 1 链式赋值
# 这些对象指向同一个ID（内存地址）
x = y = z = 0xABC
print(x, y, z)
print(id(x), id(y), id(z))
# 2 参数赋值
a = 2
n1 = n2 = n3 = n4 = n5 = n6 = 5
n1 += a  # 同 n1 = n1 + a
n2 -= a  # 同 n2 = n2 - a
n3 *= a  # 同 n3 = n3 * a
n4 /= a  # 同 n4 = n4 / a
n5 //= a  # 同 n5 = n5 // a
n6 %= a  # 同 n6 = n6 % a
print(n1, n2, n3, n4, n5, n6)
# 3 系列赋值
# 对应赋值
# 等号左侧变量个数与右边值的个数相同
a, b, c = 1, 2, 3
print(a, b, c)
# 3.p1 交换变量的值
i = 6
j = 9
print(i, j)
i, j = j, i
print(i, j)
