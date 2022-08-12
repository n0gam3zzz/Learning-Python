# written by zyf in 2022/7/7 09:11
# 添加库Decimal
import decimal
# 使用2进制存储的浮点数在计算中可能存在误差
a = 1.1
b = 2.2
print(a + b)
# 使用decimal库进行计算则不存在误差
print(decimal.Decimal('1.1') + decimal.Decimal('2.2'))
# 创建只有整数部分的浮点型
c = 3.0
print(c, type(c))
