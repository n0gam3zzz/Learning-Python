# written by zyf in 2022/07/19 13:37
# 文件对象的使用
# 在读取之后指针会停留，不会返回0


def reopenfile(filename, mode='r', encod="UTF-8"):
    global f
    f.close()
    f = open(filename, mode, encoding=encod)


f = open("txt3.txt", 'r', encoding="UTF-8")
# 1 读取文件
# file.read((size))
#     size
#         读取size个字节
#         留空，则读取所有字节
print("读取文件".center(30, 'ㄨ'))
print(f.read(2), '\n', f.read())

# 2 读取一行内容
# file.readline()
print("读取文件的一行内容".center(30, 'ㄨ'))
reopenfile("txt3.txt")
print(f.readline())

# 3 将每一行内容作为一个字符串对象，形成列表
# file.readlines()
print("将每一行内容作为一个字符串对象，形成列表".center(30, 'ㄨ'))
reopenfile("txt3.txt")
print(f.readlines())

# 4 将str内容写入文件
# file.write(str)
reopenfile("txt4.txt", 'w')
f.write("好好好")

# 5 将字符串列表写入文件
# file.writelines(strlist)
reopenfile("txt4.txt", 'w')
f.writelines(['牛牛牛\n', '好好好\n', '呃呃呃'])

reopenfile("txt5.txt")
# 6 把文件指针移动到新的位置
# file.seek(offset(, whence)))
# 把文件指针移动到新的位置
#     offset 表示相对于whence的位置
#         为正往结束方向移动
#         为负往开始方向移动
#     whence
#         0 从文件头开始计算（默认值）
#         1 从当前位置开始计算
#         2 从文件尾开始计算
print("把文件指针移动到新的位置".center(30, 'ㄨ'))
f.seek(6)  # 指针移到第6B
# 注：UTF-8编码中，一个汉字占3B
print(f.read())
# "一二三四五六七八九十123+" 中，指针在第6字节，则跳过了"一二"，从"三"开始

# 7 返回文件指针的当前位置
# file.tell()
print(f.tell())
# 指针读取完所有文本，到"一二三四五六七八九十123+"的结尾，即为3*10+4=34

# 8 把缓冲区的内容写入文件，但不关闭文件
# file.flush()
# 相当于保存操作
f.flush()

# 9 把缓冲区的内容写入文件，同时关闭文件
# file.close()
# 相当于保存并关闭的操作
f.close()
