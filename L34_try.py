# written by zyf in 2022/7/16 12:25
# 异常处理
# try except else finally
"""
try:
    (code0)  # 可能出现异常的代码
    ...
except (ErrorType1):
    (code1)  # 出现ErrorType1时执行的代码
    ...
except (ErrorType2) as string:  # 将错误信息以str类型送给string
    (code2)  # 出现ErrorType2时执行的代码
    ...
else:
    (code3)  # 无异常时执行的代码
    ...
finally:
    (code4)  # 无论如何最终都会执行的代码，可用于释放try中申请的资源
    ...
"""
# BaseException 包含所有错误

# 计算两个数相除的结果
# 当除数为0
try:
    n1 = float(input("请输入被除数:"))
    n2 = float(input("请输入除数:"))
    result = n1 / n2
except ValueError as s:
    print(s)
    print("请输入纯数字！")
except ZeroDivisionError:
    print("除数不允许为0！")
except BaseException as s:
    print(s)
else:
    print("结果为:", result)
finally:
    print("END".center(30, '-'))
