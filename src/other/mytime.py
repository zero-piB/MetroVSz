import time

def dateTotimeStamp(date = "2020-04-01 12:35:50", DateFormat="%Y-%m-%d %H:%M:%S"):
    if type(date) != str:
        date = date.strftime(DateFormat)
    #转换成时间数组
    timeArray = time.strptime(date, DateFormat)
    print(timeArray.tm_hour)
    #转换成时间戳
    return time.mktime(timeArray)

def timestampToDate(timestamp,DateFormat="%Y-%m-%d %H:%M:%S"):
    #转换成localtime
    time_local = time.localtime(timestamp)
    #转换成新的时间格式(2016-05-05 20:28:54)
    return time.strftime(DateFormat, time_local)

def minutesToSec(min):
    return min*60

def getHours(date = "2020-04-01 12:35:50", DateFormat="%Y-%m-%d %H:%M:%S"):
    if type(date) != str:
        date = date.strftime(DateFormat)
    #转换成时间数组
    timeArray = time.strptime(date, DateFormat)
    return timeArray.tm_hour


print(getHours())