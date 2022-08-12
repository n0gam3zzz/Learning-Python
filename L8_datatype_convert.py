# written by zyf in 2022/7/7 09:35
# 1 转换为str类型
a1 = 10  # int
a2 = 3.1415  # int
a3 = True  # bool
print(str(a1), str(a2), str(a3))
# 2 转换为int类型
b1 = '10'  # str
b2 = 3.1415  # float
b3 = True  # bool
# b4 = '3.1415'  # str 字符串为小数，不能直接转换为整型。可以先转换为浮点型然后转换为整型
# b5 = 'H'  # str 字符串中包含数字之外的字符，不能转换为整型
# b6 = "hello"  # str 字符串中包含数字之外的字符，不能转换为整型
print(int(b1), int(b2), int(b3))
# 3 转换为float类型
c1 = '3.1415'  # str
c2 = '3'  # str
c3 = 4  # int
c4 = True  # bool
# c5 = 'H'  # str 字符串中包含数字之外的字符，不能转换为浮点型
# c6 = "hello"  # str 字符串中包含数字之外的字符，不能转换为浮点型
print(float(c1), float(c2), float(c3), float(c4))
# 4 转换为bool类型
# 只要为非0数，转化为布尔型均为True；否则为False
d1 = 66
d2 = 3.14
d3 = -1.1
d4 = 0
# d5 = '1'  # str 字符串不能转换为布尔型
# d6 = '0'  # str 字符串不能转换为布尔型
# d7 = 'H'  # str 字符串不能转换为布尔型
# d8 = "hello"  # str 字符串不能转换为布尔型
print(bool(d1), bool(d2), bool(d3), bool(d4))

