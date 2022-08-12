# written by zyf in 2022/7/12 19:49
# 7 字符串的判断
# 7.1 判断是否为合法的标识符
# string.isidentifier()
# 合法标识符：不能以数字开头；不能包含+-*/=!@#等非法字符；不能为纯数字；不能包含空格。
s = "_M249"
print(s, s.isidentifier())
s = "张三"
print(s, s.isidentifier())
s = "_123"
print(s, s.isidentifier())
s = "123"
print(s, s.isidentifier())
s = "a+b"
print(s, s.isidentifier())
s = "Hello World"
print(s, s.isidentifier())
# 7.2 判断是否全部由空白字符组成
# string.isspace()
# 空白字符包括空格 、回车\r、换行\n、水平制表符'\t'
s = ' '
print(s, s.isspace())
s = "a\tb\tc"
print(s, s.isspace())
s = '\t'
print(s, s.isspace())
# 7.3 判断是否全部由字母组成
# string.isalpha()
# 中文在Python中也被认定为字母
s = "abc"
print(s, s.isalpha())
s = "张三ABC"
print(s, s.isalpha())
s = "list_generation"
print(s, s.isalpha())
s = "string1"
print(s, s.isalpha())
# 7.4 判断是否全部由十进制数组成
# string.isdecimal()
s = "0123456789"
print(s, s.isdecimal())
s = "EFF3AC"
print(s, s.isdecimal())
# 7.5 判断是否全部由数字组成
# string.isnumeric()
# 包括罗马数字、中文的数字（一壹叄仨）、罗马数字（ⅠⅡⅢⅰⅱⅲ）
#     ①②③⑴⑵⑶⒈⒉⒊❶❷❸㈠㈡㈢
s = "123"
print(s, s.isnumeric())
s = "一二三四"
print(s, s.isnumeric())
s = "壹贰叄肆仨"
print(s, s.isnumeric())
s = "壹贰叄肆呃呃"
print(s, s.isnumeric())
s = "FFAC"
print(s, s.isnumeric())
s = "①⑴⒈❶㈠"
print(s, s.isnumeric())
s = "ⅠⅡⅢⅰⅱⅲ"
print(s, s.isnumeric())
# 7.6 判断是否全部由字母和数字组成
# string.isalnum()
s = "ABC123"
print(s, s.isalnum())
s = "ABCabc123ⅠⅡⅢⅰⅱⅲ①⑴⒈❶㈠壹贰叄"
print(s, s.isalnum())
s = "啊1"
print(s, s.isalnum())
s = "Hello Python 呃呃"
print(s, s.isalnum())
