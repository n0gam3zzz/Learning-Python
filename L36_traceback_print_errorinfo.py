# written by zyf in 2022/7/16 15:59
# 使用traceback模块的print_exc方法打印错误信息
# traceback.print_exc()
import traceback

print(''.center(30, '-'))
try:
    num = 10 / 0
except BaseException:
    traceback.print_exc()
