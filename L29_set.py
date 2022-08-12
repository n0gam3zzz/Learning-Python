# written by zyf in 2022/7/10 20:37
# set 集合
# 集合是只有key没有value的字典
# 集合中的元素是无序的

# 1. 集合的创建
# 创建重复的key最终只有一个，即key不允许重复
# 1.1 使用花括号{}
# set = {(key1), (key2), ...}
# key可以为字符、字符串和数字，如果为字符或字符串则需要加引号
# 1.2 使用set()函数
# set(range/list/tuple/string/set)
# 函数里可以是range()、列表、元组、字符串、{}和空
# 若set函数中为字符串，则将其中的每一个字符作为key
# 1.3 空集合的创建
# set()
# 通过{}定义的为空字典

# 2. 集合元素的判断
# in, not in
st1 = {"A1", "A2", "B1", 90}
print("A1" in st1)
print("A1" not in st1)
print("C1" in st1)
print("C1" not in st1)

# 3. 集合的元素增加操作
# 3.1 使用add方法
# set.add(key)
# 不可以为空
# 一次只能添加一个元素
stt = {"张三", "李四", 123, 233}
print("添加前：", stt)
stt.add("王五")
print("添加后：", stt)
# 3.2 使用update方法
# set.update()
# update方法中可以是range()、列表、元组、字符串、集合和空
# 可以一次添加多个元素
stt.update({"老六", "老八"})
print(stt)

# 4. 集合的元素删除操作
# 4.1 使用remove方法删除指定元素
# set.remove(key)
# 一次只能删除一个指定元素
# 如果元素不存在则报错KeyError
print("删除前：", stt)
stt.remove(233)
print("删除后：", stt)
# 4.2 使用discard方法删除指定元素
# set.discard(key)
# 一次只能删除一个指定元素
# 如果元素不存在不会报错
stt.discard(12312313)  # 并不存在该元素，但不报错
print("删除前：", stt)
stt.remove(123)
print("删除后：", stt)
# 4.3 使用pop方法删除任意元素
# set.pop()
# 一次删除一个任意元素
print("删除前：", stt)
stt.pop()
print("删除后：", stt)
# 4.4 使用clear方法清空集合
# set.clear()
stt.clear()
print(stt)

# 5. 集合的关系
# 5.1 两个集合是否相等
# set1 == set2
# set1 != set2
# 5.2 子集
# 判断set1是否为set2的子集
# set1.issubset(set2)
# 5.3 超集
# 判断set1是否为set2的超集
# set1.issuperset(set2)
# 5.4 交集
# 判断set1和set2是否没有交集
# set1.isdisjoint(set2)

# 6. 集合的数学运算
# 运算对原集合不产生变化，产生新集合
# 6.1 求交集
# set1.intersection(set2)
# set1 & set2
s1 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
s2 = {1, 2, 3, 5, 8, 13, 21}
print(s1.intersection(s2))
print(s1 & s2)
# 6.2 求并集
# set1.union(set2)
# set1 | set2
s1 = {1, 2, 3, 4, 5}
s2 = {6, 7, 8, 9, 10}
print(s1.union(s2))
print(s1 | s2)
# 6.3 求差集
# 求set1对set2的差集，从set1中减去set1和set2共有的元素
# set1.difference(set2)
# set1 - set2
s1 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
s2 = {1, 2, 3, 5, 8, 13, 21}
print(s1.difference(s2))
print(s1 - s2)
# 6.4 求对称差集
# 求set1与set2的对称差集，从set1并set2中减去共有的元素
# set1.symmetric_difference(set2)
# set1 ^ set2
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

# 7 集合生成式
# 同列表生成式，将[]改为{}即可
# {(关于i的表达式) for i in (可迭代对象)}
x = set(range(1, 11))
print("x:", x, id(x))
y = {i*i for i in x}
print("y:", y, id(y))
