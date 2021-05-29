# https://www.runoob.com/python/python-exercise-example42.html
# 学习使用auto定义变量的方法

# I
# 碎碎念：查
def py42_AutoSetVariate():
    autoNumber = 1
    auto_fuc()
    print(autoNumber)


def auto_fuc():
    auto_number = 10
    for i in range(3):
        print(auto_number)
        auto_number += 1


if __name__ == "__main__":
    py42_AutoSetVariate()

# 总结
# 网上搜了一下，应该是C语言时候的语法。大概说的是局部变量（函数体内）和全局变量的关系。总之应该是平时都在用，但是没有意识到，应该是没啥用。

# 实例
# num = 2
# def autofunc():
#     num = 1
#     print ('internal block num = %d' % num)
#     num += 1
# for i in range(3):
#     print ('The num = %d' % num)
#     num += 1
#     autofunc()