# written by zyf in 2022/07/17 15:38
# 特殊属性

class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fun():
        print("呃呃。")


class D(A):
    pass


# 1 __dict__
# ex.__dict__
# obj.__dict__
# 查看实例绑定的属性或类绑定的属性和方法，以dict形式输出

print("__dict__".center(50, '*'))
x = C("dev1ce", 114)
print(x.__dict__)
print(C.__dict__)
print(D.__dict__)

# 2 __class__
# ex.__class__
# 输出实例所属的类，为type
print("__class__".center(50, '*'))
print(x.__class__)  # <class '__main__.C'>

# 3 __bases__
# obj.__bases__
# 输出类的所有父类，为tuple
print("__bases__".center(50, '*'))
print(C.__bases__)
print(D.__bases__)
# 3.1 __base__
# obj.__base__
# 输出类的第一个父类，为type
print("__base__".center(50, '*'))
print(C.__base__)
print(D.__base__)

# 4 __mro__
# obj.__mro__
# 输出类的层次结构（家谱），为tuple
print("__mro__".center(50, '*'))
print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
print(D.__mro__)
print(object.__mro__)

# 5 __subclasses__
# obj.__subclasses__
# 输出类的子类，为list
print("__subclasses__".center(50, '*'))
# print(object.__subclasses__())
print(A.__subclasses__())
print(B.__subclasses__())
print(C.__subclasses__())
print(D.__subclasses__())
