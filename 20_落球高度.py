#
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？


#分析：
#流程：根据输入次数，循环运算最高高度减半，叠加总路程，
#核心算法：路程 += 本次最高高度 *1.5  最高高度 *=0.5
#注意：根据此算法，需要额外处理最后的半程

#data
times = 10
fristHigh = 100
nowHigh = fristHigh
totalDistance = 0

def drop(high):
    global totalDistance,nowHigh
    totalDistance += high*1.5
    nowHigh *= 0.5

for i in range(times-1):
    drop(nowHigh)

totalDistance += nowHigh

print(totalDistance)
print(nowHigh/2)


#总结
#很简单的程序，需要仔细读题，直到最后需要输出的到底是哪个数
