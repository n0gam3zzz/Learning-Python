# written by zyf in 2022/07/17 16:05
# 特殊方法
#     这些特殊方法在创建新类时需要手动编写 (predefined)
#     实现了这些特殊方法即可实现该类实例的+, -或&等等运算
"""
def __??__(self, (input), ...)
    ...
    (return ...)
"""


# + __add__
# - __sub__
# * __mul__
# % __mod__
# & __and__
# len() __len__


# 手动编写特殊方法
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __add__(self, other):  # +
        return self.name + ' ' + str(self.score) + ', ' + other.name + ' ' + str(other.score)

    def __len__(self):  # len()
        return len(self.name)


# 1 __add__
"""
def __add__(self, other):  # self和other为__add__固定的输入参数
    ...
    return ...
"""
# ex1 + ex2 所实现的底层方法
#     在float类、int类和string类等类默认存在的特殊方法
a = 10
b = 20
c = a + b
# 上一条代码运作的原理是下一条代码，即使用了int类的__add__方法
d = a.__add__(b)
print(c, d)
stu1 = Student("哼哼啊啊啊", 114)
stu2 = Student("你是一个一个", 514)
print(stu1 + stu2)  # 定义了__add__方法后即可实现 + 运算
print(stu1.__add__(stu2))  # 同上

# 2 __len__
"""
def __len__(self):  # self为__len__固定的输入参数
    ...
    return ...
"""
# len(ex) 所实现的底层方法
#     在list类、tuple类和set类等类默认存在的特殊方法
print(len([1, 2, 3]))
# 上一条代码运作的原理是下一条代码，即使用了list类的__len__方法
print([1, 2, 3].__len__())
print(len(stu1))  # 定义了__len__方法后即可实现 len() 运算
print(stu1.__len__())  # 同上


# 3 __new__与__init__创建对象的流程
# 以下流程中：
#     __new__产生的obj, __init__传入的self和实例exp三者id相同
#     __new__传入的cls, 类AAA两者id相同
class AAA(object):
    def __new__(cls, *args, **kwargs):
        print(f"__new__方法被调用了，cls的id为{id(cls)}。")
        obj = super().__new__(cls)  # 调用object类的创建对象
        print(f"对象已创建，obj的id为{id(obj)}。")
        return obj

    def __init__(self, a, b):
        print(f"__init__方法被调用，self的id为{id(self)}。")
        self.a = a
        self.b = b


print(''.center(50, '*'))
print(f"Object类的id为{id(object)}。")
print(f"AAA类的id为{id(AAA)}。")

exp = AAA(114, 514)
print(f"obj_AAA这个AAA类的实例的id为{id(exp)}。")
