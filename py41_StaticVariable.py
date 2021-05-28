# https://www.runoob.com/python/python-exercise-example41.html
# 模仿静态变量的用法

# I
# 碎碎念：静态变量，从字面上理解应该就是非动态的，也就是不变的变量，我记得类似的好像是全局变量（所有方法都可以使用的）还有常量（不变的量）？
# 我记得是全部用大写字母表示，然后其他的语言中，应该还有global，static的标志字符来着，去对一对
# 反正都是一些查的东西

def py41_StaticVariable():

    class A():
        static_number = 1

        def output(self):
            print(self.static_number)

    a = A()
    a.output()

    pass


if __name__ == "__main__":
    print(py41_StaticVariable())


# 总结
# 静态变量：在计算机编程领域指在程序执行前系统就为之静态分配（也即在运行时中不再改变分配情况）存储空间的一类变量。

# 实例
# !/usr/bin/python
# -*- coding: UTF-8 -*-

# def varfunc():
#     var = 0
#     print ('var = %d' % var)
#     var += 1
# if __name__ == '__main__':
#     for i in range(3):
#         varfunc()
#
# # 类的属性
# # 作为类的一个属性吧
# class Static:
#     StaticVar = 5
#     def varfunc(self):
#         self.StaticVar += 1
#         print (self.StaticVar)
#
# print (Static.StaticVar)
# a = Static()
# for i in range(3):
#     a.varfunc()
