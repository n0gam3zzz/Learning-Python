# written by zyf in 2022/7/8 17:04
# 4. 切片
# list[start:end:step]
# 得到从start到end，以step为步长的元素的新列表
lst = list(range(5, 101, 5))
print(lst)  # lst = [5, 10, 15, ..., 95, 100]
# 4.1 只有start和end，默认step为1
print(lst[0:5])
print(lst[0:5:])
# 4.2 只有end和step，在step为正时，默认start为0
print(lst[:10:1])
print(lst[:10:2])
# 4.3 只有start和step，在step为正时，默认end为列表末尾n-1
print(lst[10::1])
print(lst[10::2])
# 4.4 step为负
# 倒序
print(lst[5:0:-1])
# step为负时，start默认为末尾n-1，end默认为0
