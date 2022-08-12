# written by zyf in 2022/07/18 16:22
import copy


# 0 变量的赋值方式
class A:
    pass


class B:
    pass


class C:
    def __init__(self, a, b):
        self.a = a
        self.b = b


c1 = C(114, 514)
c2 = c1
print(c1, id(c1), '\n', c2, id(c2))

# 1 类的浅拷贝
# copy.copy(x)
# Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝
# 因此，源对象与拷贝对象会引用同一个子对象
#     类比于快捷方式
aa = A()
bb = B()
c1 = C(aa, bb)  # 创建一个C类对象
c2 = copy.copy(c1)  # 浅拷贝c1为c2
print(c1, c1.a, c1.b)
print(c2, c2.a, c2.b)
# c1和c2的id不同，但是子对象没有拷贝，均指向相同的id


# 2 类的深拷贝
# copy.deepcopy()
# 使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
#    类比于备份
c3 = copy.deepcopy(c1)
print(c3, c3.a, c3.b)
