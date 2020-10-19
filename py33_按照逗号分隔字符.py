
# https://www.runoob.com/python/python-exercise-example33.html
# 按逗号分隔列表。

# I
# 分析：查下list的属性里边我记得有，如果没有就循环读取list里边的每一个元素，然后if逗号，就新建一个列表，最后全部输出

# 碎碎念：列表是？

def py33(prelist):
    reslut = []
    opList = []
    for i in prelist:
        print(i)
        opList.append(i)
        if i == ",":
            reslut.append(opList[0:-1])
            opList = []
    reslut.append(opList)
    return reslut

if __name__ == "__main__":
    l1 = ["1",",","3","2"]
    #print(py33(l1))


# 总结
# 感觉写的不太好啊，代码逻辑最后还补了一句= = ，而且也挺复杂的，顺带一提，没找到
# 看了实例
L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
#print(type(s1))

# 非常有种文不对题的感觉，不过算了，学习下他这里边的算法
# 这个最后吧这个List的元素中间，每两个元素间都插了一个“，”，变成了一整个字符串
# string.join(seq)以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
# join里边的参数填了一个for循环，其实是为了将每一个元素都转成str，直接是一个list也是可以的

a = ["1","2","3","4"]
s = "!".join(a)
print(s)