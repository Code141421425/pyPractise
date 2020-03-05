#https://www.runoob.com/python/python-exercise-example7.html
#将一个列表的数据复制到另一个列表中。

#分析：for i in range(): a[i] =b[i]   或者 说不定有些python封装好的东西可以用
# 

a = [1,2,3]
b = []
c= a[:]

for i in range(len(a)):
    b.append(a[i])

for i in range(len(b)):
    print(b[i])



#a 和 a[:] ，浅复制和深复制，引用和值的复制的关系