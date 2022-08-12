# written by zyf in 2022/7/11 21:35
# 字符串
# 1. 字符串的创建
# '(txt)'
# "(txt)"
# '''(txt)'''
a = 'string'
b = "string"
c = '''string'''
print(a, id(a), type(a))
print(b, id(b), type(b))
print(c, id(c), type(c))

# 2. 字符串的驻留机制
# 2.1 驻留机制演示
# 驻留机制的几种情况
#     字符串的长度为0或1时
#     符合标识符(字母、数字和下划线)的字符串
#     字符串只在编译时进行驻留，而非运行时
#         Python是一种解释性的语言
#     [-5, 256]之间的整数数字（这里适用的是int）
# 需要进行字符串拼接的时候，使用join方法，效率比+更高
# 注：PyCharm进行了优化，不能体现出，请在cmd-Python进行验证
# 以下两者或三者在value上相等。
# 2.2 强制使两者指向同一个对象
# 使用库sys中的intern方法使a和b指向同一个对象
# import sys
# a = sys.intern(b)

# 3. 字符串的查询
# 相当于列表中的元素查询
# 3.1 利用index方法查找子串第一次出现的位置
# string.index(substr)
# 如果不存在则报错ValueError
s = "ABcaABC1"
print("3.1", s.index('A'), s.index("AB"))
# 3.2 利用rindex方法查找子串最后一次出现的位置
# string.rindex(substr)
# 如果不存在则报错ValueError
print("3.2", s.rindex('A'), s.rindex("AB"))
# 3.3 利用find方法查找子串第一次出现的位置
# string.find(substr)
# 如果不存在则返回-1
print("3.3", s.find('A'), s.find("ABC"), s.find("ABCD"))
# 3.4 利用rfind方法查找子串最后一次一次出现的位置
# string.rfind(substr)
# 如果不存在则返回-1
print("3.4", s.rfind('A'), s.rfind("ABC"), s.rfind("ABCD"))

# 4. 字符串的大小写转换
# 产生新的字符串
# 4.1 把所有字符都转换为大写
# string.upper()
s = "ABCdEfghIJklMnOpq StRinG caPiTaL"
print("4.1", s, s.upper())
# 4.2 把所有字符否转换为小写
# string.lower()
print("4.2", s.lower())
# 4.3 大写变为小写，小写变为大写
# string.swapcase()
print("4.3", s.swapcase())
# 4.4 第一个字符大写而其余小写
# string.capitalize()
print("4.4", s.capitalize())
# 4.5 每个单词首字母大写而其余小写
# string.title()
print("4.5", s.title())

# 5. 字符串对齐
# 5.1 居中对齐
# string.center(width, (char))
# width指定宽度；char指定填充符，可选，默认是空格
# 如果设置宽度小于实际宽度则则返回原字符串
s = "Python"
print("5.1", s.center(11, '-'))
print("5.1", s.center(11))
# 5.2 左对齐
# string.ljust(width, (char))
# width指定宽度；char指定填充符，可选，默认是空格
# 如果设置宽度小于实际宽度则则返回原字符串
print("5.2", s.ljust(11, '-'))
print("5.2", s.ljust(11))
# 5.3 右对齐
# string.rjust(width, (char))
# width指定宽度；char指定填充符，可选，默认是空格
# 如果设置宽度小于实际宽度则则返回原字符串
print("5.3", s.rjust(11, '-'))
print("5.3", s.rjust(11))
# 5.4 右对齐且前面用0填充
# string.zfill(width)
# 左边用0填充，width用于指定字符串的宽度
# 如果设置宽度小于实际宽度则则返回原字符串
# 如果string开头为-或+，则会将0填充到其之后
print("5.4", s.zfill(11))
n = "-203"
print("5.4", n.zfill(10))
n = "+aaa"
print("5.4", n.zfill(10))

# 6 劈分
# 6.1 从左边开始劈分
# string.split()
# string.split(sep=''), string.split('')
# string.split(sep='', maxsplit=n)
# 返回的值为list，list中的元素均为str
# 通过参数sep指定劈分字符，默认的劈分字符是空格字符
# 通过参数maxsplit指定劈分字符串时的最大劈分次数n，在经过最大次劈分之后，剩余的子串会单独做为一部分
s = "1 2 3 4 5 6 7 8 9 10"
print("6.1", s.split())
s = "1-2-4-8-16-32"
print("6.1", s.split())
print("6.1", s.split('-'))
print("6.1", s.split(sep='-'))
print("6.1", s.split(sep='-', maxsplit=3))
# 6.2 从右边开始劈分
# string.rsplit()
# string.rsplit(sep=''), string.rsplit('')
# string.rsplit(sep='', maxsplit=n)
s = "1 2 3 4 5 6 7 8 9 10"
print("6.2", s.rsplit())
s = "1-2-4-8-16-32"
print("6.2", s.rsplit())
print("6.2", s.rsplit('-'))
print("6.2", s.rsplit(sep='-'))
print("6.2", s.rsplit(sep='-', maxsplit=3))

# 7 字符串的判断
# 7.1 判断是否为合法的标识符
# string.isidentifier()
# 合法标识符：不能以数字开头；不能包含+-*/=!@#等非法字符；不能为纯数字；不能包含空格。
# 7.2 判断是否全部由空白字符组成
# string.isspace()
# 空白字符包括空格 、回车\r、换行\n、水平制表符'\t'
# 7.3 判断是否全部由字母组成
# string.isalpha()
# 中文在Python中也被认定为字母
# 7.4 判断是否全部由十进制数组成
# string.isdecimal()
# 7.5 判断是否全部由数字组成
# string.isnumeric()
# 包括罗马数字、中文的数字（一壹叄仨）、罗马数字（ⅠⅡⅢⅰⅱⅲ）
#     ①②③⑴⑵⑶⒈⒉⒊❶❷❸㈠㈡㈢
# 7.6 判断是否全部由字母和数字组成
# string.isalnum()

# 8 字符串的替换与合并
# 8.1 字符串的替换
# string.replace(str1, str2, (n))
# 将str1替换为str2，替换n次，默认全部替换
s = "Hello, Python, Python, Python"
print("8.1", s)
print("8.1", s.replace("Python", "C++"))
print("8.1", s.replace("Python", "C++", 2))
# 8.2 字符串的合并
# string.join(list/tuple/string)
# 将列表或元组中的字符串合并成一个字符串
# 其中两者间的字符为string
print("8.2", ", ".join(["Hello", "Python", "C", "Java"]))
print("8.2", ''.join(("Hello", "Python", "C", "Java")))
print("8.2", "Hello, ".join(["Python"]))
print("8.2", '-'.join("Python"))

# 9 字符串的比较
# > >= < <= == !=
# 不同于is，is比较的是ID
# 比较规则：
#     首先比较第一个字符，若相同则比较下一个，直到不同，或一者为空
#     比较的是Unicode，可通过ord(char)获取其Unicode值
print("9", "apple" > "app")
print("9", "apple" > "banana", ord('a'), ord('b'))
print("9", "张三" < "李四", ord('张'), ord('李'))

# 10 字符串的切片
# 切片将生成一个新的字符串
# string[(start):(end):(step)]
# 同列表
s = "Hello, World"
print("10", s[:5] + '!' + s[7:] + '!')
print("10", s[3:9])
print("10", s[::2])
print("10", s[::-1])
print("10", s[-5::1])

# 11 格式化字符串
# 11.1 使用%占位
# 占位符：
#     文本中为 %s %d %f，string % (str0, str1, ...)
#         %s为str形式，%d为int形式，%f为float形式
#         用str0, str1, ...依次替换文本中的%?
name = "田所浩二"
age = 24
weight = 74
height = 170
occupation = "学生"
txt1 = "大家好，我叫%s，%d岁，是%s。身高是%d厘米，体重是%d公斤。" % (name, age, occupation, height, weight)
print("11.1", txt1)
# 11.2 使用{}占位
# 占位符：
#     文本中为 {n}，string.format(str0, str1, ...)
#         n为后面format方法中字符串的序号
#         只有一个可以留空则默认为0
txt2 = "大家好，我叫{0}，{1}岁，是{4}。身高是{3}厘米，体重是{2}公斤。".format(name, age, weight, height, occupation)
print("11.2", txt2)
print("11.2", "{0}, {1}, {2}, {3}, {4}".format(name, age, weight, height, occupation))
# 11.3 f-string
# string = f"txt"
# 文本中使用{变量名}占位
txt3 = f"大家好，我叫{name}，{age}岁，是{occupation}。身高是{height}厘米，体重是{weight}公斤。"
print("11.3", txt3)

# 12 占位符的格式控制
# 12.1 %占位符指定宽度
# %(n)d, %(n)s, %(n)f
#     指定宽度为n，右对齐
# 12.2 %占位符指定浮点型的小数位数
# %.(m)f
#     指定保留m位小数，不足则补零
# 12.3 %占位符指定整型的宽度，不足则补零
# %.(m)d
#     指定宽度为m，不足在前面补零
# 12.4 {}占位符指定宽度
# {num/var:n}
#     指定宽度为n，字符串左对齐，数字右对齐，超过则保留原字符串
# {num/var:.n}
#     指定宽度为n，超过则截取
# 12.5 {}占位符指定浮点型的小数位数
# {num/var:.mf}
#     指定小数位数为m，不足则补零
# 12.6 {}占位符同时指定宽度和小数位数
# {num/var:n.mf}
#     指定宽度为n，小数位数为m

# 13 字符串的编码与解码
# string→(编码)→bytes→(解码)→string
# 13.1 编码
# string.encode(encoding="(encoding_format)")
#     编码格式有"GBK", "UTF-8", "UTF-16"
s = "张三劳改过了同性恋真是人类的毒瘤abc123+-/*编码解码"
b1 = s.encode(encoding="GBK")
b2 = s.encode(encoding="UTF-8")
b3 = s.encode(encoding="UTF-16")
print("13.1", b1, type(b1))
print("13.1", b2, type(b2))
print("13.1", b3, type(b3))
# 13.2 解码
# bytes.decode(encoding="(encoding_format)")
print("13.2 √", b1.decode(encoding="GBK"))
# print("13.2 ×", b1.decode(encoding="UTF-8"))
# print("13.2 ×", b1.decode(encoding="UTF-16"))
# print("13.2 ×", b2.decode(encoding="GBK"))
print("13.2 √", b2.decode(encoding="UTF-8"))
# print("13.2 ×", b2.decode(encoding="UTF-16"))
# print("13.2 ×", b3.decode(encoding="GBK"))
# print("13.2 ×", b3.decode(encoding="UTF-8"))
print("13.2 √", b3.decode(encoding="UTF-16"))
