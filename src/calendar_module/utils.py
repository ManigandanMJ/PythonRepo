import calendar
import  logging
logging.basicConfig(filename = "c:\\logs\\calendar_log.log",filemode="w")
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def calendar_module():
    log.info("Calendar module function defined")
    month, day, year = map(int, input().split(' '))
    d = calendar.weekday(year, month, day)
    print(calendar.day_name[d].upper())
    return calendar.day_name[d].upper()