# written by zyf in 2022/07/19 20:41
# 模块 os.path
import os

# 1 获取文件或目录的绝对路径
# abspath(path)
# 返回值为str
print(os.path.abspath("testp.py"))

# 2 判断文件或目录是否存在
# exists(path)
# 存在则返回True，否则返回False
print(os.path.exists("txt233.txt"))
print(os.path.exists("L34_try.py"))

# 3 将目录与目录或文件全名拼接起来
# join(path, name)
# 返回值为str
# 如果path末尾没有反斜杠会自动添加
print(os.path.join("D:\\学习\\Python\\Learn", "txt1.txt"))

# 4 分离目录名为路径名和文件全名
# split(path)
# 返回值为tuple
# "A\\B\\C\\s1.s2" 其中'.'为文件全名的最后一个点 → ('A\\B\\C', 's1.s2')
print(os.path.split("D:\\学习\\Python\\Learn\\txt1.txt"))

# 5 分离文件全名为文件名和扩展名
# splitext(FileName)
# 返回值为tuple
# "s1.s2" 其中'.'为最后一个 → ('s1', '.s2')
print(os.path.splitext("pic1.png"))

# 6 从一个目录中提取文件全名
# basename(path)
# 返回值为str
# "A\\B\\C\\s1.s2"  → 's1.s2'
print(os.path.basename("D:\\学习\\Python\\Learn\\txt1.txt"))

# 7 从一个路径中提取文件路径，不包括文件全名
# dirname(path)
# 返回值为str
# "A\\B\\C\\s1.s2" → 'A\\B\\C'
print(os.path.dirname("D:\\学习\\Python\\Learn\\txt1.txt"))

# 8 判断是否为路径
# isdir(path)
print(os.path.isdir("D:\\学习\\Python\\Learn\\"))
print(os.path.isdir("D:\\学习\\Python\\Learn\\txt1.txt"))
print(os.path.isdir("txt1.txt"))

# 9 遍历路径内所有的目录与文件
# walk(path)
# 返回值为tuple
# 包括目录路径(str)、该目录路径下的文件夹(str_list)、该目录路径下的文件(str_list)
list_files = os.walk("D:\\学习\\Python\\Learn")
for current_path, dir_name, file_name in list_files:
    print(''.center(50, '*'))
    print(current_path)
    print(dir_name)
    print(file_name)
    print(''.center(50, '*'))

# 输出本目录下的所有*.py文件
print(''.center(50, '*'))
path = os.getcwd()
lstpath = os.listdir(path)
for i in lstpath:
    if i.endswith(".py"):
        print(i, end=' ')
