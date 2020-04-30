#https://www.runoob.com/python/python-exercise-example23.html
#打印出菱形

##分析
# 简单，思路完备
# 思路：
#   所需要输入的是最大宽maxWidth（需要个大于3的奇数），
#   然后把maxWidth，放到数组Reslut中
#   循环，次数为maxWidth - 1,将maxWidth - 2，从前后压入数组（根据数组中间+-i）
#   之后maxWidth - Reslut中的对应数量 ，再除以2，打印空格，之后打印按照reslut中的数量打印星星

import math

#data
#   所需要输入的是最大宽maxWidth（需要个大于3的奇数），
maxWidth = 7
Reslut = []

#   然后把maxWidth，放到数组Reslut中

Reslut.append(maxWidth)
addNumber = maxWidth-2

#   循环，次数为maxWidth - 1,将maxWidth - 2，从前后压入数组（根据数组中间+-i）
# for i in range(1,maxWidth-1):
#     prePos = int(math.ceil((len(Reslut)/2) - i ))
#     proPos = int(math.floor((len(Reslut)/2) + i ))
#     Reslut.insert(prePos,(addNumber-2))
#     Reslut.insert(proPos,(addNumber-2))
#     addNumber -=2

# 【new】 一起处理太麻烦了，还是先处理比较小的，一致第0为insert，之后append

while(1):
    if addNumber >0:
        Reslut.insert(0,addNumber)
        Reslut.append(addNumber)
        addNumber-=2
    else:
        break

print(Reslut)
#   之后maxWidth - Reslut中的对应数量 ，再除以2，打印空格，之后打印按照reslut中的数量打印星星

for a in Reslut:
    times = math.ceil((maxWidth-a)/2)
    for b in range(times):
        print(" ",end="")
    for c in range(a):
        print("*",end="")
    print()


##总结
# 思路一开始想得就没有问题：结果生成算法，跟思路比，还了一种实现方式，打印算法还可以
# 一共花了半个小时，虽然感觉还可以，但是觉得应该可以更快才对，可以优化的点有：
#       换了一次思路：这个不应该，应该在分析的时候，多想想，虽然不能排除写完更好会怎么样，但是还是之前能够做到想得更明白一点会更好
#       想法：由于现在的写法————现将思路写成注释，然后逐行实现。的这种方式感觉还不错，但是由于想得时候，就光顾着写了，所以注释还是写的
#               更清楚一点会比较好。否则就会出现写的边界值什么的都没怎么写好，debug的时候bug会比较多