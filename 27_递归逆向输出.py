#https://www.runoob.com/python/python-exercise-example27.html
#题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

# 评级：I
# 碎碎念：没太懂要递归掉用啥？输入递归？处理递归？输出递归？算了，递归就完事了，这个也不是很难。不过递归的话，应该就是禁止用循环的了吧



def py27(times):
    a = []

    def func(times):
        if times == 0:
            print(a)
            return 
        else:
            a.insert(0,input("输入"+str(times)+":"))
        return func(times-1)

    func(times)

if __name__ == "__main__":
    py27(5)


#总结
# 因为很简单：所以实现方法很多，不过目的是递归的话= = 
# 1.return 可以后边啥都不写
# 原来递归只要自己掉自己就行了，没有必要非得卸载return里= =
# 实例写的是递归print a[-1]