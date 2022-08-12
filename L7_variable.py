# written by zyf in 2022/7/6 14:58
# 变量
# 1. 赋值，查看变量信息（包括ID、类型与值）
name = '测试'
print('ID:', id(name))
print('TYPE:', type(name))
print('VALUE:', name)
num = 12345
print('ID:', id(num))
print('TYPE:', type(num))
print('VALUE:', num)

# 2. 变量类型
# 2.1 int 整型 integer
num = 123
print('TYPE:', type(num), ', VALUE:', num)
# 2.2 float 浮点型
num = 3.1415
print('TYPE:', type(num), ', VALUE:', num)
# 2.3 bool 布尔型 boolean
# True 和 False，转换为整型则为1和0
flag = True
print('TYPE:', type(flag), ', VALUE:', flag)
print('flag = ', int(flag))
# 2.4 str 字符型
name = '测试'
print('TYPE:', type(name), ', VALUE:', name)

# 3. 删除变量
# del (变量)
del num
