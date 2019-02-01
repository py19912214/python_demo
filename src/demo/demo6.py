import datetime
from pandas.tseries.offsets import Day

now_time =datetime.datetime.now()#获取当前时间
yes_time = (now_time -1*Day()).strftime('%Y-%m-%d')#格式化
print(yes_time.split("-")[2])
cur_time=now_time.strftime("%Y-%m-%d")
print(cur_time.split("-")[2]=='01')