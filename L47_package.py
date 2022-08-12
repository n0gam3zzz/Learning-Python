# written by zyf in 2022/07/18 19:57
# 包
# 与目录Directory的区别是，多了__init__.py的目录就是包
# 包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下
# 包的作用:
#   ·代码规范
#   ·避免模块名称冲突

# 1 导入包
import L47_Package
print(L47_Package)

# 2 导入包中的模块
# import PackageName.ModuleName (as NickName)
import L47_Package.module1 as M1  # M1为模块L47_Package.module1的别名
print(M1)

# 3 import与from ... import的区别
# import只能导入包或模块
# from ... import可以导入模块和模块中的内容
import L47_Package
print(L47_Package)
import L47_Package.module1
print(L47_Package.module1)
from L47_Package import module1
print(module1)
from L47_Package.module1 import FFF
print(FFF)

