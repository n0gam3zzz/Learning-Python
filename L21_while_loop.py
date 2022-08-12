# written by zyf in 2022/7/7 20:53
# while 循环

# 有限长等差数列求和
a1 = float(input("输入a1: "))
an = float(input("输入an: "))
k = float(input("输入公差: "))
while k == 0:
    k = float(input("公差不能为0，请重新输入: "))
ans = i = a1
while i < an:
    i += k
    ans += i
print('从', a1, "以公差", k, "累加到", i, "的结果为", ans)

# 有限长等比数列求和
a1 = float(input("输入a1: "))
an = float(input("输入an: "))
k = float(input("输入公比: "))
while k == 1 or k == 0:
    k = float(input("公比不能为0或1，请重新输入: "))
ans = i = a1
while i < an:
    i *= k
    ans += i
print('从', a1, "以公比", k, "累加到", i, "的结果为", ans)

# 有限长等差数列累乘
a1 = float(input("输入a1: "))
an = float(input("输入an: "))
k = float(input("输入公差: "))
ans = i = a1
while i < an:
    i += k
    ans *= i
print('从', a1, "以公差", k, "累乘到", i, "的结果为", ans)
