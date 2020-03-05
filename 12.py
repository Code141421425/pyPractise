#https://www.runoob.com/python/python-exercise-example12.html
#判断101-200之间有多少个素数，并输出所有素数。

##分析
#质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。
#既然如此肯定需要一个判断是不是素数的方法，便是核心，之后，利用for循环101-200即可

#核心算法1——判断素数
#循环除以小于自己的数，若能整除，且不是1或者本身，则返回False

#核心算法2——能否整除
#如果被整除后，余数是0，则返回TRUE，反之返回Flase

#规模分析：使用两个方法即可，无需架构类等

def ifExcatDivision(n1,n2):
    if n1%n2==0:
        return True
    else:
        return False

def ifPrime(n):
    if_Prime = True
    for i in range(2,n-1):
        if ifExcatDivision(n,i):
            if_Prime = False
            break

    if if_Prime:
        return True
    else:
        return False

total = 0
for i in range(101,200):
    if ifPrime(i):
        total+=1
        print(i)


print("Total:%d"%total)


##总结：
#1.分析到位，写的挺顺的
#2.最好多利用一下相关的库，比如本例中使用的：math.sqrt
    

