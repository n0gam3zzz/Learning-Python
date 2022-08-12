# written by zyf in 2022/7/8 09:24
# break
# 用于跳出循环

# 输入密码，但只有三次试错机会
# 使用for-in循环实现
n = 3
for i in range(1, n + 1):
    password = input("请输入密码：")
    if password == "1234":
        print("密码正确！")
        break
    else:
        if i != n:
            print("密码错误！你还有", 3 - i, "次机会。")
        else:
            print("密码错误！你没有机会了！")
# 使用while循环实现
n = 3
i = 1
while i <= 3:
    password = input("请输入密码：")
    if password == "1234":
        print("密码正确！")
        break
    else:
        if i != n:
            print("密码错误！你还有", 3 - i, "次机会。")
        else:
            print("密码错误！你没有机会了！")
    i += 1
