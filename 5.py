#https://www.runoob.com/python/python-exercise-example5.html
#输入三个整数x,y,z，请把这三个数由小到大输出。

#排序问题：基础的算法可以是放入数组，然后用第1个和后边的数比，若比较小，则不动，若比另一个大，则放到更换被比数，放到第1个


x = 100
y = 1
z = 10

a = [x,y,z]


for i in range(len(a)-1):
    if a[i]<a[i+1]:
        pass
    else:
        temp = a[i]
        a[i] = a[i+1]
        a[i+1] = temp

for i in range(len(a)):
    print(a[i])




# def exchangeNumber(a,b):
#     temp = a 
#     global a 
#     a = b
#     global b
#     b = temp
#     print(a)
#     print(b)

# a1 = 1
# b1 = 2

# exchangeNumber(a1,b1)
# print(a1)
# print(b1)

#l.sort()  多多运用数组内置函数