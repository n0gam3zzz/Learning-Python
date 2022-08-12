# written by zyf in 2022/7/13 21:04
# 局部变量与全局变量
# 在函数体内的变量均为局部变量
# 在函数体外的变量均为全局变量
def fun1():
    a = 20
    b = 30
    print(a, b)
    return


fun1()
# print(a, b)  # 无法输出，a和b为在fun1函数体内的局部变量


# 1 将局部变量转换为全局变量
# 在函数体内使用 global var
# 将局部变量var转换为全局变量
def fun2(a):
    global ret
    ret = a**a
    print(a, ret)
    return


fun2(5)
print(ret)
