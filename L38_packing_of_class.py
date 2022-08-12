# written by zyf in 2022/07/17 08:30
# 分装

# 面向对象的三大特征
#     封装：提高程序的安全性
#         将数据（属性）和行为(方法）包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。这样无需关心方法
#         内部的具体实现细节，从而隔离了复杂度。
#         在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个“_”。
#     继承：提高代码的复用性
#     多态：提高程序的可扩展性和可维护性

# 类的实例属性私有
#     定义实例属性时 self.__attr = attr
#     不希望被外部使用
#     但是仍然可以通过obj._Classname__attr访问
#     Python的私有为伪私有，前一条的访问方法最好不要使用
"""
class Classname:

    def __init__(self, attr1, ...):  # 定义实例属性attr1
        self.__attr1 = attr1  # 将实例属性attr1私有
        ...
"""


class Student:
    place = "广州"  # 定义类属性place

    def __init__(self, name, age):  # 定义实例属性name, age
        self.name = name
        self.__age = age  # self.__age定义实例属性age私有

    def info(self):  # 实例方法
        print("姓名为", self.name, "，年龄为", self.__age, '。')


stu = Student("田所浩二", 24)
print(dir(stu))  # 得到stu所属的属性与方法
print(stu.name)
# print(stu.__age) # 无法执行
print(stu._Student__age)  # 能够进行访问，但是不推荐使用
stu.info()
