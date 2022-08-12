# written by zyf in 2022/07/19 09:43
# 第三方模块
# 1 第三方模块的安装
# pip install ModuleName
# 进入cmd进行在线下载安装
"""
pip install schedule
"""
# Collecting Schedule
#   Downloading schedule-1.1.0-py2.py3-none-any.whl (10 kB)
# Installing collected packages: Schedule
# Successfully installed Schedule-1.1.0
# WARNING: You are using pip version 22.0.4; however, version 22.1.2 is available.
# You should consider upgrading via the 'C:\Users\10737\AppData\Local\Programs\Python\Python310\python.exe
# -m pip install --upgrade pip' command.

import schedule
import time


# 1.ex schedule模块的使用
def job():
    print("哼哼")


schedule.every(5).seconds.do(job)  # 每5秒执行一次job()
while 1:
    schedule.run_pending()
    time.sleep(2)  # 休眠2秒
