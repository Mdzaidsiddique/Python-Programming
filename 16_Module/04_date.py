import datetime

dt = datetime.datetime
print(dt.now())

print(dt.now().year)
print(dt.now().strftime("%A"))

#  %A and other format we can use to specify the date format


import time
a = time.localtime()

print(a)