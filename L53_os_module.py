# written by zyf in 2022/07/19 20:16
# 模块 os
#     os模块是Python内置的与操作系统功能和文件系统相关的模块
#     该模块中的语句的执行结果通常与操作系统有关，在不同的操作系统上运行，得到的结果可能不一样。
#     os模块与os.path模块用于对目录或文件进行操作
import os

# 1 cmd
# os.system("txt")
os.system("calc.exe")  # 打开计算器
# 与cmd中输入calc效果相同

# 2 获取当前工作目录
# os.getcwd()
# 返回值为str
# get current work directory
print(os.getcwd())

# 3 返回指定路径下的文件和目录信息
# os.listdir(path)
# 返回值为list
#     "../" 返回上一级目录
print(os.listdir("../test"))

# 4 创建目录
# os.mkdir(path[, mode])
# 已存在该目录则报错FileExistsError
os.mkdir("testdir")

# 5 创建多级目录
# os.makedirs("path1/path2/..."[, mode])
# 已存在该目录则报错FileExistsError
os.makedirs("testdir2/A/B/C")

# 6 删除目录
# os.rmdir(path)
# 不存在该目录则报错FileNotFoundError
os.rmdir("testdir")

# 7 删除多级目录
# os.removedirs("path1/path2/...")
# 不存在该目录则报错FileNotFoundError
os.removedirs("testdir2/A/B/C")

# 8 设置工作目录
# os.chdir(path)
# change directory
os.chdir("../")
print(os.getcwd())
os.chdir("Learn")
print(os.getcwd())
os.chdir(os.path.dirname(__file__))  # 将本文件所在目录作为工作目录