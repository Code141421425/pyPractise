

# https://www.runoob.com/python/python-exercise-example32.html

# 按相反的顺序输出列表的值。

# I
# 应该是一个基础语法的应用，可以去找一下List的属性


a = [0,1,2,3,4,5,7]
print(a[-2:2:-1])

def py32(list1):
    list1.reverse()
    return  list1




if __name__ == "__main__":
    l1 = ["1","2","3"]
    ##print(py32(l1))



# 总结
# 他用了一个a[::-1]的表示
# 其实是python的一个写法：a[i:j:k],表示从i到j，步进为k复制一个新的数组，缺省分别为，0，len（a），1
# 可以接受负数，i&j表示倒数第几个，k表示到反向取。逻辑不对，会取成空数组