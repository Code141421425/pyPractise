#www://www.runoob.com/python/python-exercise-example29.htreturn一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

# 思路：常规思路，将这个数分别除以10000，1000......后，存入数组，反向输出
# 碎碎念：是不是过于简单了- - ,搞那啥一点，不写死多少位。递归整除10eX,至到得出多少位为止

def py29(inputNumber):

    if __name__ == "__main__":
        inputNumber = 25641831

    resluts = []

    def getNumbers(inputNumber):
        if inputNumber//10 ==0:
            resluts.append(inputNumber%10)
            return
        else:
            resluts.append(inputNumber%10)
            return getNumbers(inputNumber//10)
            
    getNumbers(inputNumber)

    if __name__ == "__main__":
        print(len(resluts))
        print(resluts)

    return resluts


if __name__ == "__main__":
    py29(12345)

# 总结
# 示例好水！不过递归和循环的差别到底是啥呢？总觉得我写的这个递归，应该用循环写也可以，甚至更好= = 
# 顺带一提，d = x % 100 / 10 可以得到所需的位数