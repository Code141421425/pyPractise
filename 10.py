#https://www.runoob.com/python/python-exercise-example10.html
#暂停一秒输出，并格式化当前时间。

##分析：
#和实例9相比，多了个格式化当前时间，这不是我今天刚在tkw优化做的东西么= = 

import datetime
import time

class Timer():
    def printNowTime():
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        hour =datetime.datetime.now().hour
        minute =datetime.datetime.now().minute
        secend = datetime.datetime.now().second

        print("时间：%d-%d-%d %d:%d:%d"%(year,month,day,hour,minute,secend))


# Timer.printNowTime()
# time.sleep(1)
# Timer.printNowTime()

##test

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(time.strftime(time.localtime(time.time())))


##总结
#抄自己的代码还真是又快有爽= = 


