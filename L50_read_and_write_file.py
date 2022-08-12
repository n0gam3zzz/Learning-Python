# written by zyf in 2022/07/19 12:55
# 文件的打开与读写

# file = open(filename, (mode, encoding=""))
#     mode="?"
#         'r' 只读（默认）
#         'w' 只写 如果不存在该文件则创建，如果存在则覆盖文件的内容
#         'a' 追加 如果不存在该文件则创建，如果存在则在该文件末尾追加内容
#         'b' 以二进制方式 需要配合使用
#             "rb" 以二进制方式读取
#             "wb" 以二进制方式写入
#         '+' 以读写方式 需要配合使用
#             "a+" 可读写追加
#     encoding="?"
#         "GBK" 以GBK编码（默认）
#         "UTF-8" 以UTF-8编码
#         "UTF-16" 以UTF-16编码


file = open("txt2.txt", 'r', encoding="UTF-8")  # 以UTF-8编码只读该文件
print(file.readlines())  # 将每一行的内容进行输出，为列表
file.close()

file = open("txt2.txt", 'w', encoding="UTF-8")  # 以UTF-8编码只写该文件
file.write("牛牛牛\n666")  # 此时文件内容变为 "牛牛牛\n666..." ...为没有覆盖的内容
file.close()

file = open("txt2.txt", 'a', encoding="UTF-8")  # 以UTF-8编码追加写入该文件
file.write("Hello\n你好呀")  # 此时文件内容变为 "Hello\n你好呀"
file.write("Hello\n你好呀")  # 此时文件内容变为 "Hello\n你好呀Hello\n你好呀"
file.close()

# 复制图片
pic = open("pic1.png", "rb")
pic2 = open("pic1_copy.png", "wb")
pic2.write(pic.read())
pic.close()
pic2.close()
