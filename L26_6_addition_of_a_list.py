# written by zyf in 2022/7/8 17:18
# 6. 对列表的增加
lst = [1, 3, 10, 20]

# 6.1 往末尾增加单个元素
# list.append(object)
# 列表的ID不变
print("增加前：", lst, "\tID:", id(lst))
lst.append(50)
print("增加后：", lst, "ID:", id(lst))

# 6.2 往列表增加多个元素
# list.extend(object/list)
lst2 = [100, 200]
str1 = "abc"
lst.extend(lst2)
print(lst)
# extend字符串会将字符串的每个字符分别作为一个元素添加
lst.extend(str1)
print(lst)

# 6.3 在某处插入单个元素
# list.insert(n, object)
# 在序号处插入元素
print("插入前：", lst)
lst.insert(2, 5)
print("插入后：", lst)

# 6.4 将列表某处或多处元素替换为单个或多个元素
# list[start:end] = (object/list)
# start默认为0，end默认为末尾n
# 将list中[start, end - 1]的这些元素进行替换
lst[8:] = [300, 500]
print(lst)
lst[1:3] = [2, 3]
print(lst)
lst[:3] = [0, 5]
print(lst)
