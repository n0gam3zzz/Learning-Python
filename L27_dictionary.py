# written by zyf in 2022/7/9 16:20
# dictionary 字典
# 字典由key-value对组成
# 字典中的key不能重复，若重复，则保留最新的key，但是value可以重复
# key必须是不可变的值，如不能将list作为key
# value所在的空间是key对应的哈希函数得到的值，所以说字典的元素是无序的
# 字典的查询速度快（通过哈希函数），但是会占用很大的空间

# 1. 字典的创建
# 1.1 使用花括号{}
# {(key1): (value1), (key2): (value2), ...}
# 这里的key可以为字符、字符串和数字，如果为字符或字符串则需要加引号
dictionary1 = {"老一": 100, "老二": 96, "老三": 81, "老四": 75, "老五": 30, "老六": 56, "老七": 90, "老八": 54, "总": "呃呃"}
print(dictionary1)
# 1.2 使用dict()函数
# dict((key1) = (value1), (key1) = (value1), ...)
# 这里的key如果是字符或字符串，不需要加引号
# value1的存储地址为key1的哈希(hash)函数得到的值
dictionary2 = dict(A=1, B=2, C=4, ALL="three")
print(dictionary2)
# 1.3 创建空字典
# {}
# dict()
dictionary_b = {}
print(dictionary_b)

# 2. 获取字典中的元素
# 无所谓单双引号
# 2.1 使用方括号[]
# dict[key]
# 如果不存在指定的key则会报错KeyError
print(dictionary1["老八"])
# 2.2 使用get方法
# dict.get(key)
# 如果不存在指定的key则返回None
print(dictionary1.get("老八"))
# 2.3 查找不存在的key时设定的返回值
# dict.get(key, (value))
# 如果查找的key不存在则返回value
print(dictionary1.get("老二三三", "对象不存在！"))

# 3. key的判断
# in, not in
print("老二" in dictionary1)
print("老二" in dictionary2)
print("老二" not in dictionary2)

# 4. 元素的增减
# 4.1 元素的删除
# del dict[key]
dictionary3 = {'A': 123, 'B': 234, 'C': 345, "CC": 456}
print(dictionary3)
del dictionary3["CC"]
print(dictionary3)
# 4.2 元素的增加或修改
# dict[key] = value
dictionary3['D'] = 456
print(dictionary3)
dictionary3['A'] = 321
print(dictionary3)
# 4.3 字典的清空
# dict.clear()
dictionary4 = {"password", 666}
print(dictionary4)
dictionary4.clear()
print(dictionary4)

# 5. 获取字典视图
# 5.1 获取所有key
# dict.keys()
# 可以通过list()转换为list
key1 = dictionary1.keys()
print(key1, type(key1))
key1 = list(key1)
print(key1, type(key1))
# 5.2 获取所有value
# dict.values()
# 可以通过list()转换为list
value1 = dictionary1.values()
print(value1, type(value1))
value1 = list(value1)
print(value1, type(value1))
# 5.2 获取所有(key, value)对/元组
# dict.items()
# 可以通过list()转换为list
items1 = dictionary1.items()
print(items1, type(items1))
items1 = list(items1)
print(items1, type(items1))

# 6. 字典元素的遍历
# 是对字典中的key进行遍历
for i in dictionary1:
    print(i, dictionary1.get(i))

# 7. 字典生成式
# zip([(key1), (key2), ...], [(value1), (value2), ...])
# dict = {a: b for a, b in zip([keys], [values])}
# 7.1 使用zip函数打包成元组列表
# [((key1), (value1)), ((key2), (value2)), ...] = list(zip([(key1), (key2), ...], [(value1), (value2), ...])）
# 打包以较短的为准
key_ = ["A1", "A2", "A3"]
value_ = ['a', 'b', 'c']
pack = zip(key_, value_)
print(pack)
dict_ = list(pack)
print(dict_)
# 7.2 将元组列表通过for-in转换为词典
# dict = {a: b for a, b in zip([keys], [values])}
# a为zip中的前一个即key，a可以任意替换，前后对应即可
# b为zip中的后一个即value，b可以任意替换，前后对应即可
dict_ = {a: b for a, b in zip(key_, value_)}
print(dict_)
# a.upper() 可以全部转换为大写
dict_ = {a: b.upper() for a, b in zip(key_, value_)}
print(dict_)
