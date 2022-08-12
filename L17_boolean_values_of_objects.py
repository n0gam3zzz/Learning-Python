# written by zyf in 2022/7/7 17:20
# 对象的布尔值
# 不为空的对象的布尔值一般为True
a = [1, 2]
print("a:", a, bool(a), type(a))
a = [0]
print("a:", a, bool(a), type(a))
a = [None]
print("a:", a, bool(a), type(a))
s = 's'
print("s:", s, bool(s), type(s))
s = '0'
print("s:", s, bool(s), type(s))
# 不为零的数的布尔值为True
n = 233
print("n:", n, bool(n), type(n))
# 为False的对象
a = None
print("a:", a, bool(a), type(a))
a = []
print("a:", a, bool(a), type(a))
a = ()
print("a:", a, bool(a), type(a))
a = {}
print("a:", a, bool(a), type(a))
a = set()
print("a:", a, bool(a), type(a))
s = ""
print("s:", s, bool(s), type(s))
n = 0
print("n:", n, bool(n), type(n))
n = 0.0
print("n:", n, bool(n), type(n))