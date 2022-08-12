# written by zyf in 2022/7/10 19:50
# tuple 元组
# 元组不可变，即不能进行增删改的操作
# 除了空元组，元组中一定包含逗号','
# 元组中存储的是对象的引用
#     如果元组中对象本身不可对象，则不能再引用其它对象
#     如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以改变
# 不可变对象可以避免更改，在程序中尽量使用不可变对象

# 1. 元组的创建
# 1.1 () 使用圆括号与逗号
# tuple = ((value1), (value2), ...)
# 多个元素的元组创建，可以省略圆括号
# tuple = (value1), (value2), ...
t1 = (1, "bye", '3', True, 114514)
print(t1, type(t1), id(t1))
t1 = 1, "bye", '3', True, 114514
print(t1, type(t1), id(t1))
# 1.2 使用内置函数tuple tuple(())
t2 = tuple((1, "bye", '5', False, 114514))
print(t2, type(t2), id(t2))
# 1.3 只创建含一个元素的元组
# tuple = (value, )
# 需要配合一个逗号
t3 = (666)  # 提示冗余圆括号，此时t3的数据类型并不是元组，而是整型
print(t3, type(t3))
t3 = (666, )
print(t3, type(t3))
t3 = 777,
print(t3, type(t3))
# 1.4 空元组的创建
# ()
# tuple()
t4 = ()
print(t4, type(t4))
t4 = tuple()
print(t4, type(t4))

# 2. 元组中元素的提取
# tuple[n]
# 同列表的序号一样，第一个元素为0，最后一个元素为n-1
# 或第一个元素为-n，最后一个元素为-1
# 超过元组长度会报错IndexError
t5 = ([1, '*'], 'A', True, 114, 3.14)
print(t5[0])
print(t5[-5])
print(t5[4])
print(t5[-1])

# 3. 元组的指向
# 元组的指向的ID不可变
# 元组指向的不可变对象不可变，但指向的可变对象（如列表和词典）可变
# 3.ex 改变元组指向的列表的内容
lst = [1, 3, 5, 10]
tt1 = (lst, 'A', True, 114, 3.14)
print(tt1)
print(type(tt1[0]), type(tt1[1]), type(tt1[2]), type(tt1[3]), type(tt1[4]))
# 对元组中的列表进行增删改操作
tt1[0].append(15)
print(lst, '\n', tt1)
tt1[0].pop()
tt1[0].pop()
print(lst, '\n', tt1)
tt1[0][0] = 0
print(lst, '\n', tt1)

# 4. 元组的遍历
# 同列表一样，使用for-in进行遍历
for item in t5:
    print(item, end=" ")
