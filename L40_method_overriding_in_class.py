# written by zyf in 2022/07/17 09:35
# 方法重写（类的继承中）
# 子类中有与父类名字相同的方法，在实际调用该子类的方法时不会使用父类的方法
# 子类重写时可以通过super().method()调用父类的方法

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"姓名为{self.name}，年龄为{self.age}。")


class Student(Person):
    def __init__(self, name, age, num, score):
        super().__init__(name, age)  # 继承父类Person的实例属性
        self.num = num
        self.score = score

    def info(self):  # 重写父类Person的方法
        super().info()  # 调用父类Person的方法
        Person.info(self)  # 效果同，但需要传入参数
        print(f"姓名为{self.name}，年龄为{self.age}，学号为{self.num}，成绩为{self.score}。")


class Teacher(Person):
    def __init__(self, name, age, ty):
        super().__init__(name, age)  # 继承父类Person的实例属性
        self.ty = ty

    def info(self):  # 重写父类Person的方法
        print(f"姓名为{self.name}，年龄为{self.age}，教龄为{self.ty}。")


stu = Student("田所浩二", 24, "114514", 114)
stu.info()
tc = Teacher("布施明", 66, 514)
tc.info()
