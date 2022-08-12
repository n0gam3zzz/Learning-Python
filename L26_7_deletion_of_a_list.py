# written by zyf in 2022/7/8 20:06
# 7. 对列表的删除
# 7.1 删除重复的元素
# list.remove(元素)
# 删除一次首次出现元素
# 指定一个不存在的元素会报错
lst = [1, 2, 3, 3, 4, 5]
lst.remove(3)
print(lst)

# 7.2 删除指定序号的元素
# lise.pop(序号)
# 指定一个超出列表长度的序号会报错
lst = ['a', 'b', 'c', "infinite", 'd']
lst.pop(3)
print(lst)
# 不指定序号，则默认删除末尾元素
lst.pop()
print(lst)

# 7.3 删减列表某处或多处元素
# list[start:end] = []
lst = [0, 'a', 'b', 'c', 1, 5, 25, 125]
print("删减前：", lst)
lst[1:4] = []
print("删减后：", lst)

# 7.4 清空列表
# list.clear()
lst = ['a', '1', 2]
print(lst)
lst.clear()
print(lst)

# 7.5 删除列表
# del list
del list
