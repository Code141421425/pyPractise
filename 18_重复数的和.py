# https://www.runoob.com/python/python-exercise-example18.html
# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。


## 分析：
# 流程：获得输入，算出每项值，相加
# 核心算法_算出每项值:循环，如果n大于1，n=tempn,an *=10,然后在再去乘a，tempn -=1,然后再循环完n
# 程序规模：两个循环搞定


## data

a = 4
n = 4   # 几个数相加
an = 0
tempN = 0
tempI = 1
s = an


while n>=1:
    tempN = n
    n-=1
    #得出被加数
    while tempN>=1:
        #如果位数大于等于2，则开始循环位数乘a
        if tempN >1:
            tempI *= 10
            an += tempI*a
            tempN -=1
        elif tempN == 1:
            an += a
            break
    s += an
    an = 0
    tempI = 1
print(s)


##总结
# 1.如果涉及到了两层循环的嵌套，感觉一定至少要把逻辑理清楚，否则就会到测试打补丁修复的情况。会很恶心，而且也会有翻车的风险
# 2.在示例中，把被加数都放到了一个数组里边，我认为这样非常好。我是混这写的，但是这样的话会造成程序的可读性很差，测试难度大。
#   所以把程序在实现的时候分模块写，是非常好的。
# 3.reduce函数：reduce() 函数会对参数序列中元素进行累积，也就是按照参数中的函数，对参数中的数组逐对进行运算
#         语法：reduce(函数，可迭代对象[,初始参数])
#         示例：
from functools import reduce

def add(x, y) :            # 两数相加
    return x + y

Sn = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5 = 15
print(Sn)

# 4.lambda : 匿名函数
#      示例：

Sn = reduce(lambda x,y: x+y,[1,2,3,4,5])
print(Sn)
# 如此可知：在写一些非常简单的函数的时候，用匿名函数会减少代码行数，能够增加函数可读性

