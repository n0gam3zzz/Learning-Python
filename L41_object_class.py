# written by zyf in 2022/07/17 12:23
# Object 类
#   ·object类是所有类的父类，因此所有类都有object类的属性和方法。
#   ·内置函数dir()可以查看指定对象所有属性
#   ·Object有一个__str__()方法，用于返回一个对于“对象的描述”，对应于内置函数str()经常用于print()方法，
#     帮我们查看对象的信息，所以我们经常会对__str__()进行重写

# 1 重写__str__()
# 默认输出类或实例的内存地址 如<__main__.Student object at 0x000001F76241AE60>
# 重写可以输出不同的信息文本，通常用于返回描述信息
# print(obj) 会默认调用obj.__str__()

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # 重写了Object类的方法
        return f"我叫{self.name}，今年{self.age}岁。"

    def info(self):
        print(f"姓名为{self.name}，年龄为{self.age}。")


class Student(Person):
    def __init__(self, name, age, num, score):
        super().__init__(name, age)  # 继承父类Person的实例属性
        self.num = num
        self.score = score

    def __str__(self):  # 重写了Person类的方法
        return f"我叫{self.name}，今年{self.age}岁，学号为{self.num}，成绩为{self.score}。"

    def info(self):  # 重写父类Person的方法
        super().info()  # 调用父类Person的方法
        print(f"姓名为{self.name}，年龄为{self.age}，学号为{self.num}，成绩为{self.score}。")


stu = Student("田所浩二", 24, 114514, 114)
print(dir(Student))
print(dir(stu))
print(stu)  # 改写__str__(self)后输出的结果
