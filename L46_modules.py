# written by zyf in 2022/07/18 16:57
# 模块
# 1 创建模块
# 一个*.py文件就是模块，包含函数、类和语句
# 尽量不要与Python自带的模块重名
# 模块名尽量见文知意
# 使用模块的好处
#     方便其它程序和脚本的导入并使用避免函数名和变量名冲突
#     提高代码的可维护性
#     提高代码的可重用性
class A:
    def __init__(self, aa, bb):
        self.aa = aa
        self.bb = bb

    @staticmethod
    def fun1():
        pass

    @classmethod
    def fun2(cls):
        pass

    def fun3(self):
        pass


def fun_1():
    pass


a = 114
b = 514
print(a, '+', b, '=', a + b)

# 2 导入模块
# import ModuleName [as AnotherName]
# 导入模块中的函数/变量/类
# from ModuleName import fun/var/class
# 可以导入整个模块，也可以导入其中的函数/变量/类
# 在import中指定别名AnotherName可以简化导入内容的名称
import math

print(math, id(math), type(math))
print(math.pi, math.e)
print(''.center(50, '*'))
print(dir(math))
print(''.center(50, '*'))

from math import pi

print(pi)

# 3 导入自定义模块
# PyCharm中，右键该文件夹 - 将目录标记为 - 源代码根目录
import L35_ErrorType

print(L35_ErrorType)

# 4 以主程序方式运行
# 当该文件以主程序运行时，将运行main下的代码
"""
if __name__ == '__main__':
    (code)
    ...
"""
