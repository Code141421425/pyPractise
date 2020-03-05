
##https://www.runoob.com/python/python-exercise-example2.html


input = 6

l = [10,20,40,60,100]
lr = [0.1,0.075,0.05,0.03,0.015,0.01]

reslut = 0

def getLevel(bones):
    level = 0

    if bones <= l [0]:
        level = 0
    elif  bones > l[0] and bones<=l[1]:
        level = 1
    elif  bones > l[1] and bones<=l[2]:
        level = 2
    elif  bones > l[2] and bones<=l[3]:
        level = 3
    elif  bones > l[3] and bones<=l[4]:
        level = 4
    elif  bones > l[4]:
        level = 5
    
    return level

def getBones(level):
    bones = 0

    if level > 0:
        for i in range(level):
            if i == 0:
                bones += l[i] * lr[i]
            else:                    
                temp = (l[i]-l[i-1]) * lr [i]
                bones = bones + temp
        bones += (input - l[level-1])*lr[level]
    else:
        bones = input * lr[0]
    
1
def run():
    #getLevel(input)
    a = getLevel(input)
    print(getBones(a))

run()


# case1
input = 10000
ret = getBones(input)
assert(ret == 10, "test error")
#总结：没有分析直接写的，真是日了
#可以将减数递减设置