# https://www.runoob.com/python/python-exercise-example43.html
# 模仿静态变量（static）的另一案例

# I
# 碎碎念：这种东西还是直接看实例吧，完全就是知识点的考察

def py43_StaticVariate2():
    inst = A()
    num = 10

    for i in range(3):
        num += 1
        inst.output()
        print(num)


class A():
    num = 1

    def output(self):
        self.num += 1
        print(self.num)


if __name__ == "__main__":
    py43_StaticVariate2()

# 实例
# 程序分析：演示一个python作用域使用方法
# class Num:
#     nNum = 1
#     def inc(self):
#         self.nNum += 1
#         print ('nNum = %d' % self.nNum)
#
# if __name__ == '__main__':
#     nNum = 2
#     inst = Num()
#     for i in range(3):
#         nNum += 1
#         print ('The num = %d' % nNum)
#         inst.inc()

# 总结
# 看了一眼实例，是关于变量作用域的，为什么感觉就是一堆废话的感觉。。。
