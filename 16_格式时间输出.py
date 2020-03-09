#https://www.runoob.com/python/python-exercise-example16.html
#输出指定格式的日期。

##分析
#以前写过：
#就是以一个python相关的时间模块，提取当时具体的年，月，日，时，分，秒进行
#然后就可以随意输出了
#程序规模：随便写

import datetime

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
hour =datetime.datetime.now().hour
minute =datetime.datetime.now().minute

print("当前时间：%d-%d-%d %d:%d"%(year,month,day,hour,minute))

##总结
#1.查了下，datetime比time模块更高级一些，是根据dt是根据t封装的
#python中时间日期格式化符号：
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
##%% %号本身


print(1)
print(datetime.date.today().strftime("%d/%m/%A/%z"))


#3.strftime 是格式化显示时间
#4.可以创建时间对象，用以在做时间上的处理，如：

 # 创建日期对象
miyazakiBirthDate = datetime.date(1941, 1, 5)
print(miyazakiBirthDate.strftime('%d/%m/%Y'))

# 日期算术运算
miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

# 日期替换
miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)
print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))