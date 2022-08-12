# written by zyf in 2022/7/10 21:02
# 1. 集合的创建
# 创建重复的key最终只有一个，即key不允许重复
# 1.1 使用花括号{}
# set = {(key1), (key2), ...}
# key可以为字符、字符串和数字，如果为字符或字符串则需要加引号
st1 = {"A1", "A2", "B1", 90}
print(st1, type(st1))
# 1.2 使用set()函数
# set()
# 函数里可以是range()、列表、元组、字符串、{}和空
# 若set函数中为字符串，则将其中的每一个字符作为key
st2 = set(range(1, 11))
print(st2)
lst = [123, 234, 345]
st3 = set(lst)
print(st3)
tp = (114, 514)
st4 = set(tp)
print(st4)
st5 = set("Python")
print(st5)
# 1.3 空集合的创建
# set()
# 通过{}定义的为空字典
st_b = set({})
print(st_b, type(st_b))
st_b1 = set()
print(st_b1, type(st_b1))
