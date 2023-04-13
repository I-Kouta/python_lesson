# 日付と時刻
import datetime

dt1 = datetime.datetime(2022, 4, 13)
print(dt1)  # 2022-04-13 00:00:00
dt2 = datetime.datetime(2022, 4, 13, 13, 22, 31)
print(dt2)  # 2022-04-13 13:22:31
tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
dt3 = datetime.datetime(2022, 4, 13, 13, 22, 31, 551, tokyo_tz)
print(dt3)  # 2022-04-13 13:22:31.000551+10:00
