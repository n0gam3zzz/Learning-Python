# written by zyf in 2022/7/8 09:36
# break
# 用于结束本次循环，进行下一次循环

# 求得1~100中所有13的倍数
i = 1
mul = 13
for n in range(1, 100):
    if n % mul:
        continue
    print(n)
