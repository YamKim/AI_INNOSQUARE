


import datetime as d

now = d.datetime.now()

print("{}년{}월{}일".format(now.year, now.month, now.day))
print("{}시{}qns".format(now.hour, now.minute)

import calendar as cal

print(cal.calendar(2020))
print('----------------')
print(cal.month(2020, 10))

print(cal.weekday(2020, 9, 11))
print(cal.weekday(2020, 9, 12))
print(cal.weekday(2020, 9, 13))
print(cal.weekday(2020, 9, 14))

w = ['월', '화', '수', '목', '금', '토', '일']

print(w[cal.weekday(2020, 9, 11)], '요일')
print(w[cal.weekday(2020, 9, 12)], '요일')
print(w[cal.weekday(2020, 9, 13)], '요일')
print(w[cal.weekday(2020, 9, 14)], '요일')
