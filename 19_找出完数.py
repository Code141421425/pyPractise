#https://www.runoob.com/python/python-exercise-example19.html
#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

##分析
# 1.整体流程：算出因数分解，因数求和判断是否符合条件，循环

from functools import reduce

tag = True
inputNumber = 100
Dividend = inputNumber
Divisor = 1
reslut = []
perfect = []

#因数分解
def fenjie(Dividend=28,Divisor = 1):
    while True:    
        a = Dividend/Divisor
        #判断是否被整除
        if a-int(a)==0 and a!=1:
            reslut.append(Divisor)
        if Divisor > Dividend:
            break
        Divisor += 1


for i in range(1,1000):
    fenjie(i)
    if reslut != []:
        Sn = reduce(lambda x,y : x+y,reslut)
        if  Sn==i:
            perfect.append(i)
        reslut = []

print(perfect)