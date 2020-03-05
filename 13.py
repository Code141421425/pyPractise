
#https://www.runoob.com/python/python-exercise-example13.html
#打印出所有的"水仙花数"，

##分析
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# 整体思路：循环所有三位数，将其拆开，利用math中的乘方，判断各位数字立方和是否等于该数本身，是则存储
# 范围分析：由于是3位数，所以循环的范围就是100~999
# 算法分析：核心算法就是水仙花数的判定，而核心算法中的核心方法，就是将一个3位数拆开
#           而3位数的拆解，就用该数分别除以100,10,1取整数
# 规模分析：小规模

import math

def ifNarcissistic(sourceNumber):
    a = math.floor(sourceNumber/100)
    b = math.floor(((sourceNumber%100)/10))
    c = sourceNumber - a*100-b*10

    if sourceNumber == math.pow(a,3)+math.pow(b,3)+math.pow(c,3):
        print(sourceNumber)
    
for i in range(100,1000):
    ifNarcissistic(i)

#test
# for i in range(1,5):
#     print(i)




##总结：
#1.for的range，包含上线，但是不包括下线
#2.立方的写法**，还有math.pow(a,3)
#3.n/10%10 就是取十位数

    
