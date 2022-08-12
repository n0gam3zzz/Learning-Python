# written by zyf in 2022/07/19 19:36
# with 语句（上下文管理器）
# with语句可以自动管理上下文资源
# 无论是正常执行完指令跳出with块，还是出现了错误，都能确保文件正确的关闭
"""
with open(FileName, mode) as NickName:
    (code)
    ...
"""
# open(FileName, mode)为上下文表达式，实现了__enter__()方法和__exit__()方法
# 也将实现了__enter__()方法和__exit__()方法的类中的实例对象称为上下文管理器，属于_io.TextIOWrapper类

with open("txt5.txt", 'r', encoding="UTF-8") as FFF:
    print(FFF.read())

print(type(open("txt5.txt", 'r', encoding="UTF-8")))  # 属于_io.TextIOWrapper类


class A:
    def __enter__(self):
        print("__enter__方法被调用。")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__方法被调用。")

    def fun(self):
        print("fun方法被调用。")


with A() as FFF2:  # 首先调用__enter__()方法，然后执行里面的语句，执行完后调用__exit__()方法
    FFF2.fun()
