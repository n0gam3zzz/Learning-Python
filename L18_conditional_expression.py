# written by zyf in 2022/7/7 20:10
# 条件表达式
# 格式: (为真时的表达式) if (判断式) else (为假时的表达式)

# 判断大小
num1 = float(input("Please enter number 1:"))
num2 = float(input("Please enter number 2:"))
print(str(num1)+"≥"+str(num2) if num1 >= num2 else str(num1)+'<'+str(num2))

# 判断一元二次方程是否有实根
print("一元二次方程 ax^2 + bx + c = 0")
a = float(input("请输入系数a："))
b = float(input("请输入系数b："))
c = float(input("请输入系数c："))
delta = b * b - 4 * a * c
print("该一元二次方程有实根。" if delta > 0 else "该一元二次方程无实根。")
