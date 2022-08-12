# written by zyf in 2022/07/18 17:20
# 请将本文件夹定义为源代码根目录
import calc1
import calc2
print(''.center(50, '*'))
print(calc1.add(0, 1))  # 定义了main，模块calc1中的语句将不会执行。没有输出666
print(''.center(50, '*'))
print(calc2.add(1, 1))  # 由于没有定义main导致模块calc2中的语句执行。输出了666
print(''.center(50, '*'))
