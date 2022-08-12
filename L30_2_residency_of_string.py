# written by zyf in 2022/7/12 10:56
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
s1 = ''
s2 = ''
print(s1 is s2)  # True 两者ID相同
s1 = '#'
s2 = '#'
print(s1 is s2)  # True 两者ID相同
s1 = "abc%#"
s2 = "abc%#"
print(s1 is s2)  # False 两者ID不同
s1 = "abc_123"
s2 = "abc_123"
print(s1 is s2)  # True 两者ID相同
s1 = "abc"
s2 = "a" + "bc"
s3 = ''.join(["a", "bc"])
print(s2 is s1)  # True 两者ID相同
print(s3 is s1)  # False 两者ID不同
s1 = -5
s2 = -5
print(s1 is s2)  # True 两者ID相同
s1 = -6
s2 = -6
print(s1 is s2)  # False 两者ID不同
# 2.2 强制使两者指向同一个对象
# 使用库sys中的intern方法使a和b指向同一个对象
# import sys
# a = sys.intern(b)
import sys
b = "abc!@#$%^&*()"
a = "abc!@#$%^&*()"
print(a is b)  # False 两者ID不同
a = sys.intern(b)
print(a is b)  # True 两者ID相同
