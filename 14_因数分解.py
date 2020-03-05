# https://www.runoob.com/python/python-exercise-example14.html
# 问题:将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

## 分析
# 因数分解:将一个正整数,一直整除,至其分解后的乘数不能整除为止
# 注意点: 1和自身不能作为除数,需要特殊处理
#         当无法分解时,可能需要特殊处理
# 流程分析: 接一个数,循环整除2至自身-1，
#           如果可以整除，则打破循环，输出该数，并使得除完之后的数，作为新的被除数合循环总数，
#           循环至不符合条件为止
# 核心算法：循环整除
#           while tag = true时，结束循环
#           Dividend Divisor

tag = True
inputNumber = 100
Dividend = inputNumber
Divisor = 2
reslut = []

#因数分解
while True:    
    a = Dividend/Divisor
    #判断是否被整除
    if a-int(a)==0 and a!=1:
        reslut.append(Divisor)
        Dividend = a
        Divisor = 2
    else:
        if Divisor < Dividend:    
            Divisor += 1
        else:
            if reslut !=[]:
                reslut.append(int(Dividend))
            break

# 打印结果
if reslut !=[]:
    print(str(inputNumber)+"=",end="")
    for i in range(len(reslut)):
        print(reslut[i],end="")
        if i<(len(reslut)-1):
            print("*",end="")
else:
    print("不可分解")
    

##总结
# 1.真正输入的边界是需要判断的，比如这次的输入：需要是大于0的int
# 2.分析的思路大致一样，不过这次的分析不足（思路不能理顺），是靠实践摸索出来的。虽然感觉也还可以，但是如果可以的话，还是把思路理顺比较好
# 3.写法上，实例中运用了两个循环的嵌套，而我是用一些条件语句进行数值的重置，已达到归零的效果，虽然我认为这种方法比较理货，但是更难测试，
#   写起来风险更大，而且不易读。如果能把思路理顺，用两层嵌套应该是更好的选择
# 4.都有了+=的写法，当然还有-=,*=和/=
# 5.打印方法的话，我认为我的写法更好些，由于是集中输出，所以更加易读一些，而且模块化，更好维护