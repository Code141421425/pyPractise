#https://www.runoob.com/python/python-exercise-example3.html

#（x+100）= a^2  (a^2+168)= b^2

import math

for i in range(100):
     a2 = i+100

#是否是完全平方数
def ifASN(a):
    temp = math.sqrt(a)
    if float(temp) == math.trunc(temp):
        return True
    else:
        return False

# 单测
def dc_ifASN():
    if ifASN(25) == True:
        print(1)
    else:
        print(0)
    if ifASN(24) == False:
        print(1)
    else:
        print(0)
    print("==========")


for i in range(10000):
    a = i+100
    if ifASN(a):
        b = a+168
        if ifASN(b):
            print(i)
            #break
    a = 0
    b = 0
    
#结论：
#先登出方程，之后得出ab关系，然后根据ab的奇偶，整数等关系，得出ab其中一个的范围，之后进行循环即可