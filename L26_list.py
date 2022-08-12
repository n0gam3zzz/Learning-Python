# written by zyf in 2022/7/8 10:32
# list函数或list变量
# 创建列表对象相当于创建了多个对象，而列表指向列表对象，每个列表对象指向创建的每个对象

# 0. 列表的特点
# (1) 列表元素按顺序有序排序
# (2) 索引映射唯一个数据
# (3) 列表可以存储重复数据
# (4) 任意数据类型混存
# (5) 根据需要动态分配和回收内存

# 1. 列表的创建
# [(元素1), (元素2), ...]
# list([(元素1), (元素2), ...])
lst = ["ABC", 'a', 123, 3.14, True]
print(lst)
print(id(lst), type(lst))

# 2. 元素的获取
# 列表对象的第1个元素的序号为0或-n，n为列表的长度
# 索引 0  1    2    3    ... n-2  n-1
# 列表 i1 i2   i3   i4   ... in-1 in
# 索引 -n -n+1 -n+2 -n+3 ... -2   -1

# 3. 查找列表中的元素
# list.index函数
lst = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
# 3.1 list.index((元素))
# 查找所有元素中第一个出现该元素的序号
print(lst.index(8))
# 3.2 list.index((元素), (起始序号))
# 从起始序号开始查找（包括起始序号）第一个出现该元素的序号
print(lst.index(8, 10))
# 3.3 list.index((元素), (起始序号), (终止序号))
# 从起始序号开始查找（包括）到终止序号（不包括）中第一个出现该元素的序号
print(lst.index(16, 1, 10))
# 若不存在则出现ValueError

# 4. 切片
# list[start:end:step]
# 得到从start到end，以step为步长的元素的新列表
# 4.1 只有start和end，默认step为1
# 4.2 只有end和step，在step为正时，默认start为0
# 4.3 只有start和step，在step为正时，默认end为列表末尾n-1
# 4.4 step为负
# step为负时，start默认为末尾n-1，end默认为0

# 5. 判断元素是否存在
# in, not in
lst = ['a', "BCD", 80, 666]
print('a' in lst)
print('a' not in lst)
print('n' in lst)
print('n' not in lst)

# 6. 对列表的增加
# 6.1 往末尾增加单个元素
# list.append(object)
# 6.2 往列表增加多个元素
# list.extend(object/list)
# 6.3 在某处插入单个元素
# list.insert(n, object)
# 在序号处插入元素
# 6.4 将列表某处或多处元素替换为单个或多个元素
# list[start:end] = (object/list)
# start默认为0，end默认为末尾n
# 将list中[start, end - 1]的这些元素进行替换

# 7. 对列表的删除
# 7.1 删除重复的元素
# list.remove(object)
# 删除一次首次出现元素
# 7.2 删除指定序号的元素
# lise.pop(n)
# 没有指定序号则删除末尾的元素
# 7.3 删减列表某处或多处元素
# list[start:end] = []
# 7.4 清空列表
# list.clear()
# 7.5 删除列表
# del list

# 8. 对列表的排序
# 使用方法 list.sort(...) 默认为升序排序，不会产生新的列表对象
# 使用内置函数sorted(list)，会产生新的列表对象
# 8.1 使用方法对列表的升序排序
# list.sort()
# list.sort(reverse=False)
# 8.2 使用方法对列表的降序排序
# list.sort(reverse = True)
# 8.3 使用内置函数sorted()对列表的排序
# 8.3.1 升序排序
# sorted(list)
# 8.3.2 降序排序
# sorted(list, reverse=True)

# 9. 列表生成式
# [(关于i的表达式) for i in (可迭代对象)]
