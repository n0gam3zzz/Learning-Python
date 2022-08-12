# written by zyf in 2022/7/16 16:09
# 类与对象
#     数据类型即类
#     类下的实例称为对象

# 1 创建类
# 类包括类属性、实例方法、静态方法、类方法
# 创建类的同时，也为创建了类名这个为type类型的对象
"""
class Classname：  # 类名为Classname，可由多个单词组成，但要求每个首字母均大写，其余小写
    cls_attr1 = value1  # 直接写在类里的变量，称为类属性，为所有实例共有
    ...
    def __init__(self, (attr1), ...)  # 初始化方法，必须包含self，使所有该类的实例都具有这些属性
        self.attr1 = attr1 # self.attr1为实例属性，这里将局部变量attr1赋值给了实例属性
        ...
    # 实例方法既可以获取构造函数定义的变量，也可以获取类的属性值
    def fun1(self, (input1), ...):  # 定义类的实例方法，必须包含self
        (code1)
        ...
    # 类方法不能获取构造函数定义的变量，可以获取类的属性
    @classmethod  # 使用该句修饰，以定义类方法
    def fun2(cls):  # 类方法中必须包含cls
        (code2)
        ...
    # 静态方法不能获取构造函数定义的变量，也不可以获取类的属性
    @staticmethod  # 使用该句修饰，以定义静态方法
    def fun3((var)):  # 静态方法中不包含self，可以有其余输入
        (code3)
        ...
"""


# 创建类的同时，也为创建了类名这个为type类型的对象
class Example:
    pass


print(Example, type(Example), id(Example))


# 以创建Student属性为例
class Student:
    place = "广州"  # 定义类属性place

    def __init__(self, name, age, num):  # 定义实例属性name, age, num
        self.name = name
        self.age = age
        self.num = num

    def info(self):  # 实例方法
        print("姓名为", self.name, "，年龄为", self.age, "学号为", self.num, '。')

    def eat(self, is_canteen=1):  # 实例方法
        if is_canteen:
            print(self.name, "在食堂吃饭。")
        else:
            print(self.name, "在吃饭。")

    @staticmethod
    def sm():  # 静态方法
        print("静态方法，@staticmethod")

    @classmethod
    def cm(cls):  # 类方法
        print("类方法，@classmethod")


print(Student, type(Student), id(Student))

# 2 创建类对象（实例）
# obj = Classname(var1, var2, ...)
# 其中var1, var2, ...与Classname中的__init__一一对应
stu_1 = Student("张三", 24, 114514)
stu_2 = Student("李四", 30, 1919810)
# 2.1 获取实例的属性
# obj.var
# var为Classname中的__init__定义的实例属性
print(stu_1.name, stu_1.age, stu_1.num)
print(stu_2.name, stu_2.age, stu_2.num)
# 2.2 对实例应用实例方法
# obj.fun(...)
# Classname.fun(obj, ...)
#     fun为obj这个Class_name中的实例方法
#     ...为fun中额外的输入参数
stu_1.info()
Student.info(stu_1)
stu_1.eat()
Student.eat(stu_1)
stu_1.eat(False)
Student.eat(stu_1, False)

# 3 获取类属性
# Classname.cls_attr
# obj.cls_attr
#    obj的类为Class_name
print(stu_1.place)
print(Student.place)

# 4 调用静态方法
# Classname.fun()
# obj.fun()
Student.sm()
stu_1.sm()

# 5 调用类方法
# Classname.fun()
# obj.fun()
Student.cm()
stu_1.cm()

# 6 动态绑定属性
# obj.attr = value
#     直接进行赋值
#     obj所属的类中不包含该属性attr时也可操作
#         操作之后，其余的obj并不包含该属性attr
stu_1.gender = '女'
print(stu_1.name, stu_1.age, stu_1.num, stu_1.gender)


# 7 动态绑定方法
# obj.fun = fun_
#     fun_为在类外定义的函数
#     fun为将fun_定义在obj中的方法名称
#     操作之后，其余的obj并不包含该方法fun
def show():
    print("定义在类之外的函数。")


stu_2.show = show
stu_2.show
