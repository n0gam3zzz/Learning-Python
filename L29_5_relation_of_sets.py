# written by zyf in 2022/7/11 16:29
# 5. 集合的关系
# 5.1 两个集合是否相等
# set1 == set2
# set1 != set2
s1 = {"张三", "李四", "王五", 233, 114}
s2 = {233, "张三", "王五", 233, "李四"}
print("s1是否等于s2：", s1 == s2)
print("s1是否不等于s2：", s1 != s2)
# 5.2 子集
# 判断set1是否为set2的子集
# set1.issubset(set2)
s1 = {1, 2, 4, 8, 16}
s2 = {1, 2, 4, 8, 16, 32, 64}
s3 = {1, 2, 4, 8, 10}
print("s1是否为s2的子集：", s1.issubset(s2))
print("s3是否为s2的子集：", s3.issubset(s2))
# 5.3 超集
# 判断set1是否为set2的超集
# set1.issuperset(set2)
print("s2是否为s1的超集：", s2.issuperset(s1))
print("s2是否为s3的超集：", s2.issuperset(s3))
# 5.4 交集
# 判断set1和set2是否没有交集
# set1.isdisjoint(set2)
s4 = {0, 3, 9, 27, 54}
print("s1是否与s2没有交集：", s1.isdisjoint(s2))
print("s3是否与s2没有交集：", s3.isdisjoint(s2))
print("s4是否与s2没有交集：", s4.isdisjoint(s2))
