# written by zyf in 2022/7/15 18:33
# 递归函数
#     如果在一个函数的函数体内调用了该函数本身，这个函数就称为递归函数
# 递归的组成部分：递归调用 + 递归终止条件
# 递归的调用过程
#     每递归调用一次函数，都会在栈内存分配一个栈帧
#     每执行完一次函数，都会释放相应的空间
# 递归的优缺点
#     缺点：占用内存多，效率低下
#     优点：思路和代码简单


# 阶乘（递归函数实现）
def fac(x):
    # x: int
    # x >= 0
    if x > 1:
        result = x * fac(x - 1)
    elif (x == 1) or (x == 0):
        result = 1
    else:
        result = "ValueError"
    return result


print(fac(10))  # 10! = 3628800


# 阶乘（循环实现）
def fac_(x):
    # x: int
    # x >= 0
    result = 1
    if x > 1:
        for i in range(x, 0, -1):
            result *= i
    elif x == 1:
        pass
    else:
        result = "ValueError"
    return result


print(fac_(10))  # 10! = 3628800


# 斐波那契数列（递归实现）
# 输出为第n位上的数
def fib(n):
    # n: int
    # n >= 1
    if (n == 1) | (n == 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))


# 斐波那契数列（循环实现）
# 输出可选
def fib_(n, islist=1):
    # n: int
    # n >= 1
    lst = list(range(n))  # 初始化
    if n == 1:
        lst[0] = 1
    elif n == 2:
        lst[0] = lst[1] = 1
    else:
        lst[0] = lst[1] = 1
        for i in range(2, n):
            lst[i] = lst[i - 1] + lst[i - 2]
    if islist:
        return lst
    else:
        return lst[n - 1]


print(fib_(10))
print(fib_(10, 0))
