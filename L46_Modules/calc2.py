# written by zyf in 2022/07/18 17:18
def add(a, b):
    return a + b


# 在被其余文件导入时仍然执行
print(add(333, 333))
