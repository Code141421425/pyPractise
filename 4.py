


# https://www.runoob.com/python/python-exercise-example4.html

#输入某年某月某日，判断这一天是这一年的第几天？

##分析
#根据输入的年判断这年是平年还是闰年
#根据输入的月份，按照135781012和31，30,28,29的配置，计算累计到当月多少天
#在根据输入的日期，增加出最后的日期

iy = 2015
im = 6
id = 7

month = [[1,31],[2,28],[3,31],[4,30],[5,31],[6,30],[7,31],[8,31],[9,30],[10,31],[11,30],[12,31]]

def ifLeapYear(year):
    if year%4 == 0:
        return True
    else:
        return False
    

def mounthAddTo(m):
    total = 0

    if ifLeapYear(iy):
        month[1][1]+=1

    for i in range(m-1):
        total += month[i][1]

    return total

print(mounthAddTo(im)+id)

#dc

def dc():
    pass