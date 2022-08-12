# written by zyf in 2022/07/18 20:29
# 常用模块
import sys
import time
import urllib.request
import math

# 1 模块 sys
# 与Python解释器及其环境操作相关的标准库
# 1.1 sys.getsizeof(obj) 查看对象占用的内存
a, b, c, d, = 114, 1, 3.1415926535, True
print(sys.getsizeof(a), sys.getsizeof(b), sys.getsizeof(c), sys.getsizeof(d))
# 1.2 sys.version Python版本信息
print(sys.version)
# 1.3 sys.path 文件路径信息
print(sys.path)

print(''.center(50, '-'))
# 2 模块 time
# 提供与时间相关的各种函数的标准库
# 2.1 time.time() 当前时间，单位为s
print(time.time())
# 2.2 time.localtime(time.time()) 当前时间信息
# tm_isdst 是否为夏令时
print(time.localtime(time.time()))

print(''.center(50, '-'))
# 3 模块 os
# 提供了访问操作系统服务功能的标准库

# 4 模块 calendar
# 提供与日期相关的各种函数的标准库

# 5 模块 urllib
# 用于读取来自网上（服务器）的数据标准库
# 5.1 urllib.request.urlopen(url).read() 读取网页内容
# print(urllib.request.urlopen("http://www.baidu.com/").read())

# 6 模块 json
# 用于使用JSON序列化和反序列化对象

# 7 模块 re
# 用于在字符串中执行正则表达式匹配和替换

# 8 模块 math
# 提供标准算术运算函数的标准库
# 8.1 math.pi 常数π
print(math.pi)
# 8.2 math.e 常数e
print(math.e)
# 8.3 math.sqrt 开根号
print(math.sqrt(81))
# 8.4 math.sin sin

# 9 模块 decimal
# 用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算

# 10 模块 logging
# 提供了灵活地记录事件、错误、警告和调试信息等日志信息的功能


