# written by zyf in 2022/7/8 09:46
# else, elif
# 选择结构

# 输入成绩判定等级
while 1:
    score = float(input("请输入成绩："))
    if 0 <= score <= 100:
        break
    else:
        print("数值无效！请重新输入！")
if 90 <= score <= 100:
    print("等级为A。")
elif 80 <= score < 90:
    print("等级为B。")
elif 70 <= score < 80:
    print("等级为C。")
elif 60 <= score < 70:
    print("等级为D。")
else:
    print("等级为Fail。")
