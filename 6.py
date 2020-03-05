#https://www.runoob.com/python/python-exercise-example6.html
#斐波那契数列。

#解题：这个数列从第3项开始，每一项都等于前两项之和。
#分析：给出初始数组[1,1],由通项公式，数组的新值等于前两项之和

l = [1,1]

for i in range(3,20):
    #print(i)
    l.append(l[i-2]+l[i-3])

for i in range(len(l)):
    print(l[i])



#总结：小心for 中的range的界限，应该是从2起
#2、为了保证循环的完整性，可以把特例写成if的形式