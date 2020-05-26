#https://www.runoob.com/python/python-exercise-example25.html
#题目：求1+2!+3!+...+20!的和。

# 评估：I
# 目的：想用一个和以往实例都差不多的，看起来比较简单的方法实现
# 杂杂碎：虽然老规矩是写个函数算阶乘，然后循环20次相加就可以了。但是想创新下，毕竟只是一个相加的操作，搞到一起。


def py25(maxNum):
    sum = 0
    for i in range(1,maxNum+1):
        addNum = 1
        while(i>1):
            addNum *= i
            i -= 1
        sum+= addNum        
    return sum


if __name__ == "__main__":
    pass
    #print(py25(20))

# 总结
# 一个逻辑上没有想到的点是： 每一个加数不用重新算阶乘，只要把前一项乘下就可以了
# 有个自带的内置函数，sum 和map

map()


