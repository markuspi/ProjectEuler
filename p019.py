from datetime import datetime, timedelta

c = 0
day = datetime(1901, 1, 1)
while day.year < 2001:
    if day.day == 1 and day.weekday() == 6:
        print(day)
        c += 1
    day += timedelta(days=1)
print(c)