# written by zyf in 2022/7/13 15:57
# 函数
# 1 函数的创建
"""
def function_name ([input1, input2, ...]):
    code1
    code2
    ...
    [return var1 var2 ...]
"""


# input称为形式参数，简称形参
# 函数名需要遵循标识符
# 在函数调用过程中，进行参数的传递
#     如果是不可变对象，在函数体的修改不会影响实参的值
#     如果是可变对象，在函数体的修改会影响到实参的值
# 函数可以没有返回值，那么可以不写return后的参数，甚至可以省略return
# 如果函数有多个返回值，则返回的是tuple
# 函数可以没有输入参数


def calc(a, b):
    c = a + b
    return c


# 2 参数传递
# 2.1 位置实参
# 根据形参对应的位置进行实参传递
print(calc(10, 20))  # 其中，10传递给calc中的a，20传递给calc中的b
# 2.2 关键字实参
# 根据形参的名称进行实参传递
print(calc(b=10, a=20))  # 其中，10传递给calc中的b，20传递给calc中的a


# 3 参数传递的内存分析
def fun(x, y):
    # y必须为list
    print("x:", x)
    print("y:", y)
    x = 100
    y.append(233)
    print("x:", x)
    print("y:", y)


print("---------------------")
n1 = 50
n2 = [6, 7, 8]
print("n1:", n1)
print("n2:", n2)
fun(n1, n2)
print("n1:", n1)
print("n2:", n2)
print("---------------------")


# 在函数体中改变了x的值，使其不再同n1一样指向值50，所以没有改变n1的值
# 在函数体中将y指向的列表后增加了值233，而n2指向同一个列表，所以改变了n2的值


# 3 函数的返回值
# 可以使用多个变量对多个值进行接收，两边一一对应
#     var1, var2, ... = output1, output2, ...
def oe(num_list):
    odd_list = []  # 存储奇数
    even_list = []  # 存储偶数
    for i in num_list:
        if i % 2:  # 为奇数
            odd_list.append(i)
        else:  # 为偶数
            even_list.append(i)
    return odd_list, even_list


n = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(oe(n))
odd, even = oe(n)
print(odd, even)

# 4 默认参数值
"""
def function_name ([input1=default_value1, input2, ...]):
    code
    ...
    [return var1 var2 ...]
"""


# 如果input不符或为空时，将采用默认值default_value
#     如内置函数print中，默认end='\n'


def fun1(a1, a2=20):
    print(a1, a2)


print("---------------------")
fun1(30)
fun1(30, True)
fun1(30, 40)


# 5 个数可变的位置形参
# def function_name ([*input, ...]):
# 使用*定义个数可变的位置形参，只能定义1个
# 定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置参数
# 输入结果为tuple
#     例如内置函数print()中的*args


def fun2(*lst1):
    print(lst1, type(lst1))


print("---------------------")
fun2(10, "and", 3.14)
fun2("Hello", "World")


# 6 个数可变的关键字形参
# def function_name ([**input, ...]):
# 使用**定义个数可变的关键字形参，只能定义1个
# 定义函数时，无法事先确定传递的关键字实参的个数时，使用可变的关键字形参
# 输入结果为dict


def fun3(**ls):
    print(ls, type(ls))


print("---------------------")
fun3(a=10, b="and", c=3.14)
fun3(x="Hello", y="World")


# 6.ex 如果函数的形参中同时含有位置形参和关键字形参
# 要求个数可变的位置形参要在个数可变的关键字形参前面


def fun4(*s1, **s2):
    print(s1)
    print(s2)


print("---------------------")
fun4("Hello", "World", x=233, y=114, z=514)


# 7 调用函数时将列表的每个元素转换为位置实参
# function(*list)
# 如果不使用*，则将list看作一个参数输入函数中


def fun5(s51, s52, s53):
    print(s51, '*', s52, '*', s53, '=', s51 * s52 * s53)


print("---------------------")
fun5(2, 3, 5)
lst = [2, 3, 5]
fun5(*lst)

# 8 调用函数时将字典的每个键值对转换为关键字实参
# function(**dict)
# 如果不使用**，则将dict看作一个参数输入函数中
print("---------------------")
fun5(s51=2, s52=3, s53=5)
dct = {"s52": 3, "s53": 5, "s51": 2}
fun5(**dct)


# 9 混合传参
# function(i1, i2, input3=i3, input4=i4)
# 前两者为位置传参，后两者为关键字传参
def fun6(ss1, ss2, ss3, ss4):
    print(ss1, ss2, ss3, ss4)


print("---------------------")
fun6(123, 234, 345, 456)
fun6(123, 234, ss4=456, ss3=345)
fun6(ss4=456, ss1=123, ss2=234, ss3=345)


# 10 限制为关键字实参传递
# def function_name ([input1, input2, *, input3, ...]):
# *前的不强制要求关键字传参，*后的必须要关键字传参
def fun6(x1, x2, *, x3, x4):
    print(x1, x2, x3, x4)


# fun6(123, 234, 345, 456)  # 后两个输入报错，意外实参TypeError
print("---------------------")
fun6(123, 234, x3=345, x4=456)
fun6(123, 234, x4=456, x3=345)
fun6(x4=456, x2=234, x1=123, x3=345)


def function1(a, b, *, c, d, **e):
    print(a, b, c, d, e)
    pass


def function2(*x, **y):
    print(x, '\t', y)
    pass


def function3(a=1, b=0, *arg1, **arg2):
    print(a, b, arg1, arg2)
    pass
