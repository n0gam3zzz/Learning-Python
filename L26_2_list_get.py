# written by zyf in 2022/7/8 17:03
# 2. 元素的获取
# 列表对象的第1个元素的序号为0或-n，n为列表的长度
# 索引 0  1    2    3    ... n-2  n-1
# 列表 i1 i2   i3   i4   ... in-1 in
# 索引 -n -n+1 -n+2 -n+3 ... -2   -1
lst = ["ABC", 'a', 123, 3.14, True]
print("-----------------------")
print(lst[0])
print(id(lst[0]), type(lst[0]))
print(lst[1])
print(id(lst[1]), type(lst[1]))
print(lst[2])
print(id(lst[2]), type(lst[2]))
print(lst[3])
print(id(lst[3]), type(lst[3]))
print(lst[4])
print(id(lst[4]), type(lst[4]))
print("-----------------------")
print(lst[-5])
print(id(lst[-5]), type(lst[-5]))
print(lst[-4])
print(id(lst[-4]), type(lst[-4]))
print(lst[-3])
print(id(lst[-3]), type(lst[-3]))
print(lst[-2])
print(id(lst[-2]), type(lst[-2]))
print(lst[-1])
print(id(lst[-1]), type(lst[-1]))
