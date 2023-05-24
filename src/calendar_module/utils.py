import calendar

def calendar_module():
    month, day, year = map(int, input().split(' '))
    d = calendar.weekday(year, month, day)
    print(calendar.day_name[d].upper())
    return calendar.day_name[d].upper()