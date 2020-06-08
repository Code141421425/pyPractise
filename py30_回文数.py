#https://www.runoob.com/python/python-exercise-example30.html
#题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。


# I+
# 碎碎念：判断回文数的话，感觉第一步就是要拆解输入的数，这时候，py29就有用了，之后只需要循环判断第一位和最后一位对比就完事了
#         看来军少说的还真没错，写程序得是一件有远虑的事情        
# 资料注释：偶数也可以有回文数

from py29_numberOperate import py29

# from test import test


def py30(inputNumber):

    #data
    ##调用py29
    ## 注：生掉py29不行，那个可是会反向输出的- - 
    ## 反注：反就反了，反正只是判断是不是回文数，不影响
    data = py29(inputNumber)
    dataLen = len(data)-1
    ifPalindrome  = -1 #回文数：Palindrome number

    #判断位数  
    #反注：单双数都可以是回回文数

    #回文数判定
    for i in range(0,dataLen):
        if i <= dataLen:            
            if data[i] == data[dataLen-i]:
                ifPalindrome = 1                
            else:
                ifPalindrome = 0
                break                
            pass
        else:
            break
    
    #返回结果
    return ifPalindrome

if __name__ == "__main__":
    print(py30(1221))


# 总结
# == 写时 ==  
# 调用其他方法的时候，居然会跑一边之前的代码，如：test.py中
# 靠，中文命名使用的py文件，居然没有办法import，真是..... 
# 靠更新：居然不是不能中文import，是不能数字起头import，nice........
# 这个封成模块的话，可以：
#       1、多利用__name__ = "__main__"
#       2、不能封的那么自闭，毕竟这个东西是给别人用的啊，输入当然要留了- - 

# == 写后 == 
# 1、这次因为比较简单，难度在III以下，所以直接写了，感觉也还算不错。所以这个评估的话，也是比较重要的。
# 2、主要是对于判断需求的解析，可能比较费劲了