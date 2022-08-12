# written by zyf in 2022/7/6 10:25
# print函数

# 1. 输出数字
print(110)
print(3.14159265)

# 2. 输出字符串
# 字符串需要加引号" ' "或" " "
print('Hello World!')
print("Hello World!")

# 3. 输出含有运算符的表达式
# 3.1 计算表达式中的数值
print(3 + 1)
# 3.2 字符串相接
print("number is " + '114514')

# 4. 数据输出
# 没有该文件会自动创建，每次运行会追加print的内容
filepath = open('D:/学习/Python/Learn/txt1.txt', 'a+')
print('TEST', file=filepath)
filepath.close()

# 5. 在一行内输出多个字符
# 使用逗号隔开即可
print('WASD', 103)
print(123, 456, 789, 222+444, '222+444')

# 6. 转义字符
# 6.1 \n 换行符
print('123\n456')
# 6.2 \t 水平制表符
print('1\t123\t12\t123\t1234\t12345\n123\t123\t1234\t12\t123\t1')
# 6.3 \b 退格符
print('il\b loa\bvar\b\be user\b\b\b!')
# 6.4 \r 回车符
print('Are you ok?\rOK!')
# 6.5 \\ \' \" 输出\ ' "
print("\\ \' \"")

# 7. 原字符
# 输出内容中的转义字符失效，在输出内容的引号前添加"R"或"r"
print(r'Hello.\nI\'m fine.')
# 最后一个字符不能为反斜杠
# print(r'Hello\')

# 8. 控制最后一个字符
# print函数默认最后输出 \n
print("---------------------")
print()  # 换行
print("aaaa", end='')  # 不换行
print("bbbb", end='')
print("cccc")
