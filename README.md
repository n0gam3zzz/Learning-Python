# 目录

## L1 _Hello, World_

## L2 模板中的注释

## L3 模板

## L4 print函数 输出函数

```py
print("txt")
print("txt", end='')  # 指定默认的结尾字符
```

## L5 字符

## L6 关键字

## L7 变量与变量类型

### 整型 `int`; 浮点型 `float`; 字符串 `string`; 布尔型 `bool`

### 删除变量

```py
del (变量)
```

## L8 变量类型的转换

```py
int(); float(); string(); bool()
```

## L9 注释

\# <内容>

'''
<内容>
'''

## L10 input函数 输入函数

```py
input(<prompt>)
```

## L11 算术运算符

### 加 `+` 减 `-` 乘 `*` 除 `/`

### 整除 `//` 取余 `%` 幂 `**`

## L12 赋值运算符

### `=`

## L13 比较运算符

### 大于 `>` 小于 `<` 等于 `==` 不等于 `!=` 小于或等于 `<=` 大于或等于 `>=`

### 是 `is` 不是 `is not`

## L14 布尔运算符

### 与 `and` 或 `or` 非 `not`

### 在里面 `in` 不在里面 `not in`

## L15 位运算符

### 与 `&` 或 `|`

### 左移 `<<` 右移 `>>`

## L16 运算符的运算顺序

## L17 变量的布尔值

## L18 条件表达式

```py
<为真时的表达式> if <判断式> else <为假时的表达式>
```

## L19 pass 用于判断中的无用函数

## L20 range函数 生成迭代器

```py
range(num1, (num2), (num3))
```

## L21 while 循环

```py
while (flag):
    (code1)
```

## L22 for in 循环

```py
for (变量) in (可迭代对象):
    (code1)
```

## L23 `break`

### 用于跳出循环

## L24 `continue`

### 用于跳过本次循环，进行下一次循环

## L25 `else, elif`

```py
if (check1):
    (code1)
elif (check2):
    (code2)
...
else:
    (coden)
```

## L26 list 列表

### 1 列表的创建

```py
[...]
list([...])
```

### 2 元素的查找

```py
list.index(...)
```

### 3 元素的提取

```py
list[n]
```

### 4 切片

```py
list[start:end:step]
```

### 5 判断元素是否存在列表中

```py
(元素) in (列表)
(元素) not in (列表)
```

### 6 在末尾增加一个元素

```py
list.append(object)
```

### 7 在末尾增加多个元素

```py
list.extend(object/list)
```

### 8 在某处插入单个元素

```py
list.insert(n, object)
```

### 9 将列表某处或多处元素替换为单个或多个元素

```py
list[start:end] = (object/list)
```

### 10 删减列表某处或多处元素

```py
list[start:end] = []
```

### 11 对列表升序排序

```py
list.sort()
list.sort(reverse=False)
sorted(list)
```

### 12  对列表降序排序

```py
lisr.sort(reverse=True)
sorted(list, reverse=True)
```

### 13 列表生成式

```py
[(关于i的表达式) for i in (可迭代对象)]
[(表达式) for _ in (可迭代对象)]
```

## L27 dict 字典

### 1 字典的创建

```py
{(key1): (value1), (key2): (value2), ...}
{}
```

### 2 字典的创建

```py
dict((key1) = (value1), (key1) = (value1), ...)
dict()
```

### 3 获取字典中的元素

```py
dict[key]
dict.get(key, (value))
```

### 4 key的判断

```py
key in dict
key not in dict
```

### 5 元素的删减

```py
del dict[key]
```

### 6 元素的增加或修改值

```py
dict[key] = value
```

### 7 词典的清空

```py
dict.clear()
```

### 8 获取所有的key

```py
dict.keys()
```

### 9 获取所有的value

```py
dict.values()
```

### 10 获取所有(key, value)对/元组

```py
dict.items()
```

### 11 字典元素的遍历（对key的遍历）

```py
for i in dict:
    (code)
```

### 12 字典生成式

#### 12.1 打包

```py
zip([(key1), (key2), ...], [(value1), (value2), ...])
```

#### 12.2 生成

```py
dict = {a: b for a, b in zip([keys], [values])}
```

## L28 tuple 元组

### 1 元组的创建

```py
((value1), (value2), ...)
()
(value1), (value2), ...
```

### 2 元组的创建

```py
tuple(((value1), (value2), ...))
tuple()
```

### 3 只创建含一个元素的元组

```py
(value, )
```

### 4 元组中元素的提取

```py
tuple[n]
```

### 5 元组的指向 元组的指向的ID不可变

### 6 元组的遍历

```py
for i in tuple:
    (code)
```

## L29 set 集合

### 1 集合的创建

```py
{(key1), (key2), ...}
```

### 2 集合的创建

```py
set(range/list/tuple/str/set)
```

### 3 空集合的创建

```py
set()
set({})  # 我的评价是多此一举
```

### 4 集合的元素的判断

```py
in
not in
```

### 5 集合的单个元素增加

```py
set.add(key)
```

### 6 集合的多个元素增加

```py
set.update(range/list/tuple/str/set/blank)
```

### 7 删除集合中指定的元素

```py
set.remove(key)
set.discard(key)
```

### 8 删除集合中的任意元素

```py
set.pop()
```

### 9 清空集合

```py
set.clear()
```

### 10 两个集合是否相等

```py
set1 == set2
set1 != set2
```

### 11 判断set1是否为set2的子集

```py
set1.issubset(set2)
```

### 12 判断set1是否为set2的超集

```py
set1.issuperset(set2)
```

### 13 判断set1和set2是否没有交集

```py
set1.isdisjoint(set2)
```

### 14 求交集

```py
set1.intersection(set2)
set1 & set2
```

### 15 求并集

```py
set1.union(set2)
set1 | set2
```

### 16 求差集

```py
set1.difference(set2)
set1 - set2
```

### 17 求对称差集

```py
set1.symmetric_difference(set2)
set1 ^ set2
```

### 18  集合生成式

```py
{(关于i的表达式) for i in (可迭代对象)}
```

## L30 string 字符串

### 1 字符串的创建

```py
'(txt)'
"(txt)"
'''(txt)'''
```

### 2 字符串的驻留机制

### 3 强制使两者指向同一个对象

```py
a = sys.intern(b)
```

### 4 利用index方法查找子串第一次出现的位置

```py
string.index(substr)
```

### 5 利用rindex方法查找子串最后一次出现的位置

```py
string.rindex(substr)
```

### 6 利用find方法查找子串第一次出现的位置

```py
string.find(substr)
```

### 7 利用rfind方法查找子串最后一次一次出现的位置

```py
string.rfind(substr)
```

### 8 把所有字符都转换为大写

```py
string.upper()
```

### 9 把所有字符否转换为小写

```py
string.lower()
```

### 10 大写变为小写，小写变为大写

```py
string.swapcase()
```

### 11 第一个字符大写而其余小写

```py
string.capitalize()
```

### 12 每个单词首字母大写而其余小写

```py
string.title()
```

### 13 居中对齐

```py
string.center(width, (char))
```

### 14 左对齐

```py
string.ljust(width, (char))
```

### 15 右对齐

```py
string.rjust(width, (char))
```

### 16 右对齐且前面用0填充

```py
string.zfill(width)
```

### 17从左边开始劈分

```py
string.split()
```

#### 17.1 指定劈分字符

```py
string.split(sep='')
string.split('')
```

#### 17.2 指定劈分字符串时的最大劈分次数n

```py
string.split(sep='', maxsplit=n)
```

### 18 从右边开始劈分

```py
string.rsplit()
```

#### 18.1 指定劈分字符

```py
string.rsplit(sep='')
string.rsplit('')
```

#### 18.2 指定劈分字符串时的最大劈分次数n

```py
string.rsplit(sep='', maxsplit=n)
```

### 19 判断是否为合法的标识符

```py
string.isidentifier()
```

### 20 判断是否全部由空白字符组成

```py
string.isspace()
```

### 21 判断是否全部由字母组成

```py
string.isalpha()
```

### 22 判断是否全部由十进制数组成

```py
string.isdecimal()
```

### 23 判断是否全部由数字组成

```py
string.isnumeric()
```

### 24 判断是否全部由字母和数字组成

```py
string.isalnum()
```

### 25 字符串的替换

```py
string.replace(str1, str2, (n))
```

### 26 字符串的合并

```py
string.join(list/tuple/str)
```

### 27 字符串的比较

```py
>, >=, <, <=, ==, !=
```

### 28 字符串的切片

```py
string[(start):(end):(step)]
```

### 29 格式化字符串

#### 29.1 %占位 文本中为 %s %d %f

```py
string % (str0, str1, ...)
```

#### 29.2 {}占位 文本中为 {n}，字符串后使用format方法

```py
string.format(str0, str1, ...)
```

#### 29.3 f-string 文本中使用{var}占位

```py
string = f"txt"
```

### 30 占位符的格式控制

#### 30.1 %占位符指定宽度

`%(n)d, %(n)s, %(n)f` 指定宽度为n，右对齐

#### 30.2 %占位符指定浮点型的小数位数

`%.(m)f` 指定保留m位小数，不足则补零

#### 30.3 %占位符指定整型的宽度，不足则补零

`%.(m)d` 指定宽度为m，不足在前面补零

#### 30.4 {}占位符指定宽度

`{num/var:n}` 指定宽度为n，字符串左对齐，数字右对齐，超过则保留原字符串

`{num/var:.n}` 指定宽度为n，超过则截取

#### 30.5 {}占位符指定浮点型的小数位数

`{num/var:.mf}` 指定小数位数为m，不足则补零

#### 30.6 {}占位符同时指定宽度和小数位数

`{num/var:n.mf}` 指定宽度为n，小数位数为m

### 31 字符串的编码

```py
string.encode(encoding="(encoding_format)")  # 编码格式有"GBK", "UTF-8", "UTF-16"，得到为bytes类型
```

### 32 字符串的解码

```py
bytes.decode(encoding="(encoding_format)")  # 得到为string类型
```

## L31 函数

### 1 函数的创建

```py
def function_name ([input1, input2, ...]):
    code1
    code2
    ...
    [return var1 var2 ...]
```

### 2 位置传参

```py
function(i1, i2, i3, ...)
```

### 3 关键字传参

```py
function(input1=i1, input2=i2, ...)
```

### 4 混合传参

```py
function(i1, i2, input3=i3, input4=i4)
```

### 5 可以使用多个变量对多个值进行接收

```py
var1, var2, ... = output1, output2, ...
```

### 6 默认参数

```py
def function_name ([input1=default_value1, input2, ...]):
    ...
```

### 7 个数可变的位置形参

```py
def function_name ([*input, ...]):
    ...
```

### 8 个数可变的关键字形参

```py
def function_name ([**input, ...]):
    ...
```

### 9 调用函数时将列表的每个元素转换为位置实参

```py
function(*list)
```

### 10 调用函数时将字典的每个键值对转换为关键字实参

```py
function(**dict)
```

### 11 限制为关键字实参传递

```py
def function_name ([input1, input2, *, input3, ...]):
    ...
```

## L32 局部变量和全局变量

```py
global var  # 将局部变量转换为全局变量（在函数体内使用）
```

## L33 迭代函数

## L34 try 异常处理

```py
try:
    (code0)  # 可能出现异常的代码
    ...
except (ErrorType1):
    (code1)  # 出现ErrorType1时执行的代码
    ...
except (ErrorType2) as string:  # 将错误信息以str类型送给string
    (code2)  # 出现ErrorType2时执行的代码
    ...
else:
    (code3)  # 无异常时执行的代码
    ...
finally:
    (code4)  # 无论如何最终都会执行的代码，可用于释放try中申请的资源
    ...
```

## L35 错误类型

## L36 使用traceback模块打印错误信息

```py
traceback.print_exc()
```

## L37 类与对象

### 1 创建类（包括创建类属性、实例属性、实例方法、类方法、静态方法）

```py
class Classname：  # 类名为Classname，可由多个单词组成，但要求每个首字母均大写，其余小写
cls_attr1 = value1  # 直接写在类里的变量，称为类属性，为所有实例共有
...
def __init__(self, (attr1), ...)  # 初始化方法，必须包含self，使所有该类的实例都具有这些属性
    self.attr1 = attr1 # self.attr1为实例属性，这里将局部变量attr1赋值给了实例属性
    ...
# 实例方法既可以获取构造函数定义的变量，也可以获取类的属性值
def fun1(self, (input1), ...):  # 定义类的实例方法，必须包含self
    (code1)
    ...
# 类方法不能获取构造函数定义的变量，可以获取类的属性
@classmethod  # 使用该句修饰，以定义类方法
def fun2(cls):  # 类方法中必须包含cls
    (code2)
    ...
# 静态方法不能获取构造函数定义的变量，也不可以获取类的属性
@staticmethod  # 使用该句修饰，以定义静态方法
def fun3((var)):  # 静态方法中不包含self，可以有其余输入
    (code3)
    ...
```

### 2 创建类对象（实例）

```py
obj = Classname(var1, var2, ...) # 与Classname中__init__一一对应
```

### 3 获取实例的属性

```py
obj.var # var为obj对应类中的实例属性
```

### 4 对实例应用实例方法

```py
obj.fun(...)
Classname.fun(obj, ...)
```

### 5 获取类属性

```py
Classname.cls_attr
obj.cls_attr
```

### 6 调用类方法或静态方法

```py
Classname.fun()
obj.fun()
```

### 7 动态绑定属性

```py
obj.attr = value
```

### 8 动态绑定方法

```py
obj.fun1 = fun2  # fun2 为在类外定义的函数
```

## L38 分装

### 将类的实例属性私有化

```py
class Classname:
...
def __init__(self, attr1, ...):  # 定义实例属性attr1
    self.__attr1 = attr1  # 将实例属性attr1私有
    ...
```

## L39 类的继承

```py
class Classname(Father1, (Father2), ...):  # 可以继承多个父类
...
def __init__(self, attr1, attr2, attr3, ...)
    super().__init__(attr1, attr2)  # attr1和attr2为父类Father1拥有的实例属性
    # Father1.__init__(attr1, attr2)  # 该句效果同上，如果只有一个父类则可用super()代替，多个则不能
    self.attr3 = attr3
    ...
```

## L40 方法重写（类的继承中）

### 子类中有与父类名字相同的方法，在实际调用该子类的方法时不会使用父类的方法

### 子类重写时可以通过 `super().method()` 调用父类的方法

## L41 Object类

### object类是所有类的父类，因此所有类都有object类的属性和方法

### 方法·`__str__`，用于返回对于对象的描述，print输出的信息

## L42 多态

## L43 特殊属性

### 1   `__dict__`

```py
ex/obj.__dict__  # 查看实例绑定的属性或类绑定的属性和方法，以dict形式输出
```

### 2   `__class__`

```py
ex.__class__  # 输出实例所属的类，为type
```

### 3   `__bases__`

```py
obj.__bases__  # 输出类的所有父类，为tuple
```

### 4   `__base__`

```py
obj.__base__  # 输出类的第一个父类，为type
```

### 5   `__mro__`

```py
obj.__mro__  # 输出类的层次结构，为tuple
```

### 6   `__subclasses__`

```py
obj.__subclasses__  # 输出类的子类，为list
```

## L44 特殊方法

### 1 实现 + 运算

```py
obj.__add__
```

### 2 实现 - 运算

```py
obj.__sub__
```

### 3 实现len()

```py
obj.__len__
```

### 4 定义类的实例属性

```py
obj.__init__
```

### 5 创建实例对象

```py
obj.__new__
```

## L45 拷贝

### 1 浅拷贝

```py
copy.copy(ex/obj)
```

### 2 深拷贝

```py
copy.deepcopy(ex/obj)
```

## L46 模块

### 1 创建模块 一个 _*.py_ 文件就是一个模块

### 2 导入模块

```py
import ModuleName [as AnotherName]
```

### 3 导入模块中的函数/变量/类

```py
from ModuleName import fun/var/class
```

### 3 导入自定义模块

#### _PyCharm_ 中，右键该文件夹 - 将目录标记为 - 源代码根目录

### 4 以主程序方式运行

```py
if __name__ == '__main__':
    (code)
    ...
```

## L47 包

### 1 导入包

```py
import PackageName
```

### 2 导入包中的模块

```py
import PackageName.ModuleName
from PackageName import ModuleName
```

### 3 导入包中的模块的内容

```py
from PackageName.ModuleName import fun/var/class
```

## L48 常用模块

### 1 __sys__ 与Python解释器及其环境操作相关的标准库

#### 1.1 查看对象占用的内存

```py
sys.getsizeof(obj)
```

#### 1.2 查看Python版本信息

```py
sys.version
```

#### 1.3 查看文件路径信息

```py
sys.path
```

### 2 __time__ 提供与时间相关的各种函数的标准库

#### 2.1 得到当前时间，单位为s

```py
time.time()
```

#### 2.2 得到当前时间信息

```py
time.localtime(time.time())
```

### 3 __os__ 提供了访问操作系统服务功能的标准库

### 4 __calendar__ 提供与日期相关的各种函数的标准库

### 5 __urllib__ 用于读取来自网上（服务器）的数据标准库

#### 5.1 读取网页内容

```py
urllib.request.urlopen(url).read()
```

### 6 __json__ 用于使用JSON序列化和反序列化对象

### 7 __re__ 用于在字符串中执行正则表达式匹配和替换

### 8 __math__ 提供标准算术运算函数的标准库

### 9 __decimal__ 用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算

### 10 __logging__ 提供了灵活地记录事件、错误、警告和调试信息等日志信息的功能

## L49 第三方模块的安装

### 进入 _cmd_ 输入 `pip install ModuleName` 在线下载模块 ModuleName

## L50 文件的打开与读写

```py
file = open(filename, (mode, encoding=""))
```

## L51 文件对象的使用

### 1 读取文件

```py
file.read((size))
```

### 2 读取一行内容

```py
file.readline()
```

### 3 将每一行内容作为一个字符串对象，形成列表

```py
file.readlines()
```

### 4 将str内容写入文件

```py
file.write(str)
```

### 5 将字符串列表写入文件

```py
file.writelines(strlist)
```

### 6 把文件指针移动到新的位置

```py
file.seek(offset(, whence)))
```

### 7 返回文件指针的当前位置

```py
file.tell()
```

### 8 把缓冲区的内容写入文件，但不关闭文件

```py
file.flush()
```

### 9 把缓冲区的内容写入文件，同时关闭文件

```py
file.close()
```
