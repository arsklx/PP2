#1
import datetime as dt
x = dt.datetime.now()
print(x - dt.timedelta(5))
print("=======================")

#2
print(x - dt.timedelta(1))
print(x)
print(x + dt.timedelta(1))
print("=======================")

#3
print(x.strftime("%x"), x.strftime("%X"))
print("=======================")

#4
s = list(map(int, input().split()))
t = list(map(int, input().split()))
date1 = dt.datetime(*s)
date2 = dt.datetime(*t)
seconds = date2 - date1 if date2 >= date1 else date1 - date2
print(int(seconds.total_seconds()))
print("=======================")

#5




