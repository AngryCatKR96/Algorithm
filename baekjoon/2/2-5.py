hour, minute = map(int,input().split())


if minute < 45:
    alarm_hour = hour - 1
    alarm_min = 60 - (45-minute)
    if alarm_hour < 0:
        alarm_hour = 24 + alarm_hour
    print(alarm_hour,end=' ')
    print(alarm_min)
else:
    print(hour,end=' ')
    print(minute-45)
    