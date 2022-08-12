# written by zyf in 2022/07/17 08:50
# 类的继承
"""
class Classname(Father1, (Father2), ...):  # 可以继承多个父类

    def __init__(self, attr1, attr2, attr3, ...)
        super().__init__(attr1, attr2)  # attr1和attr2为父类Father1拥有的实例属性
        # Father1.__init__(attr1, attr2)  # 如果只有一个父类则可用super()代替，多个则不能
        self.attr3 = attr3
        ...
"""


# 如果一个类没有继承任何一个类，则默认继承object
# Python支持多继承
# 定义子类时，必须在其构造函数中调用父类的构造函数


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info1(self):
        print(f"姓名为{self.name}，年龄为{self.age}。")


class Student(Person):
    def __init__(self, name, age, num, score):
        super().__init__(name, age)  # 继承父类Person的实例属性
        # Person.__init__(name, age)  # 效果同
        self.num = num
        self.score = score

    def info2(self):
        print(f"姓名为{self.name}，年龄为{self.age}，学号为{self.num}，成绩为{self.score}。")


class Teacher(Person):
    def __init__(self, name, age, ty):
        super().__init__(name, age)  # 继承父类Person的实例属性
        # Person.__init__(name, age)  # 效果同
        self.ty = ty

    def info2(self):
        print(f"姓名为{self.name}，年龄为{self.age}，教龄为{self.ty}。")


stu = Student("田所浩二", 24, "114514", 114)
stu.info1()  # 继承父类Person的方法
stu.info2()  # 类Student自身的方法
tc = Teacher("布施明", 66, 514)
tc.info1()  # 继承父类Person的方法
tc.info2()  # 类Teacher自身的方法


# 继承多个父类
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def fun1(self):
        print(self.a, self.b)


class B:
    def __init__(self, c, d):
        self.c = c
        self.d = d

    def fun2(self):
        print(self.c, self.d)


class C(A, B):  # 多继承
    def __init__(self, a, b, c, d, e):
        A.__init__(self, a, b)  # 继承父类A的实例属性a, b
        B.__init__(self, c, d)  # 继承父类B的实例属性c, d
        self.e = e

    def fun_(self):
        print(self.a, self.b, self.c, self.d, self.e)


t = C(1, 2, 3, 4, 5)
t.fun1()
t.fun2()
t.fun_()
