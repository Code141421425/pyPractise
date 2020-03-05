#测试随机出的读取
#生成随机数，若10%以外，大于4次，则开始计数，计数小于10%停止，共生成1w个随机数

import random

targetLimt = 10
realLimit = 0

targetRate = 10
count = 0
ifChouka = False

b = [50,50,50,50,50,50,5,50]
reslut = 0
realReslut = 0
TotalTimes = 10000


for i in range(TotalTimes):
    a = random.randint(0,100)
    if a <= targetRate:
        realReslut+=1
    #print(a)
    #a = b[i]

    #若大于4次，则进行付费抽卡
    if realLimit >= targetLimt:
        ifChouka = True
    
    if ifChouka:
        #抽卡直至出货位置
        realLimit = 0
        count +=1

        if a <= targetRate:
            reslut+=1
            ifChouka = False
        else: 
            pass
        
    else:
        #不付费抽卡时，判断是否大于4次
        if a > targetRate:
            realLimit +=1
        else:
            realLimit = 0

    


print("=====================")

print(reslut)
print(realReslut/TotalTimes)
print(count)
print(reslut/count)