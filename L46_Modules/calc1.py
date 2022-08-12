# written by zyf in 2022/07/18 17:18
def add(a, b):
    return a + b


if __name__ == '__main__':  # 该文件以主程序运行时将执行下面的语句，在被其余文件导入时则不会执行
    print(add(333, 333))
