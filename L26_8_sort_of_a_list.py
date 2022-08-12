# written by zyf in 2022/7/9 14:24
# 8. 对列表的排序
# 使用方法 list.sort(...) 默认为升序排序，不会产生新的列表对象
# 使用内置函数sorted(list)，会产生新的列表对象

# 8.1 使用方法对列表的升序排序
# list.sort()
# list.sort(reverse=False)
lst = [123, 564, 1000, 95]
print("排序前：", lst, id(lst))
lst.sort()
print("排序后：", lst, id(lst))
lst = [123, 564, 1000, 95]
print("排序前：", lst, id(lst))
lst.sort(reverse=False)
print("排序后：", lst, id(lst))

# 8.2 使用方法对列表的降序排序
# list.sort(reverse = True)
lst = [123, 564, 1000, 95]
print("排序前：", lst, id(lst))
lst.sort(reverse=True)
print("排序后：", lst, id(lst))

# 8.3 使用内置函数sorted()对列表的排序
# 8.3.1 升序排序
# sorted(list)
lst = [123, 564, 1000, 95]
lst2 = sorted(lst)
print(lst)
print(lst2)
# 8.3.2 降序排序
# sorted(list, reverse=True)
lst = [123, 564, 1000, 95]
lst2 = sorted(lst, reverse=True)
print(lst)
print(lst2)
