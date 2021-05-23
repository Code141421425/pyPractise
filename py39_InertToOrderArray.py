# https://www.runoob.com/python/python-exercise-example39.html

## 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。


## II 
## 碎碎念：首先是测序，给根据强两个数来判定吧，正序和倒序，判定规律的时候，相等的情况应该也是需要考虑的,不过这么一想，似乎也还要验证他是否是顺序的
##        之后是根据之后的顺序来进行插入，根据规则和其他的数进行对比，然后满足条件就插入，之后的数往后顺位移动。后边这步虽然使用数组自带的insert应该就可以了，不过还是实现基础算法吧
##         不过规则根据之前的测序怎么写之后的逻辑？写个IF就是双倍的代码量，感觉很不好啊。明明区别只有一个大小于号。
##         2)等下，可以测个序，然后直接把新元素加入序列，然后直接排序啊[滑稽]，虽然平白无故的拍了个序列，用了两层循环，但是新写的代码量就很少了，可以用py38。不过为了锻炼，还是算了


def py39(targetList,insertNumber):
    #测序
    list = targetList[:]
    positiveOrder = -1

    ## 是数组
    if len(list) >=2 :
        for i in range(len(list)-1):
            if list[i] < list[i+1]:
                positiveOrder = 1
            elif list[i] > list[i+1]:
                positiveOrder = 0
            else:
                pass

    else:
        print("no list")

    #插入
    ## 正序数组
    if positiveOrder == 1 :
        for i in range(len(list)):
            if insertNumber < list[i]:
                list.insert(i,insertNumber)
                break
            else:
                if i == len(list)-1:
                    list.append(insertNumber)
                else:
                    pass                
    ## 倒序数组
    elif positiveOrder == 0:
        for i in range(len(list)):
            if insertNumber > list[i]:
                list.insert(i,insertNumber)
                break
            else:
                if i == len(list)-1:
                    list.append(insertNumber)
                else:
                    pass 
    else:
        print("not order list")
        return

    return list


def test():
    return 


if __name__ == "__main__":
    list1 = [1,3,3,5,8]
    list2 = [5,2,1,-1]
    number = -10
    print(py39(list2,number))



# 写完后：
# 用时45min+
# - 在进行插入的时候，没有判断这个数组是否是有序的。不过这个问题倒不大；
# - 有些问题的点是，在进行排序的时候，在正序或者逆序的时候，同样的代码进行了复制粘贴，而且对比的逻辑，也有些啰嗦

# 对完答案后：
# - emmmmmmm写的真死
# - 不过占位符的想法，感觉可以借鉴，说不定在哪儿就能够用上
# - 然后比起使用列表中的insert，用两个暂时的变量，把整个数组以此往后的想法也还不错
# - 其他人写的答案中，深复制想法不错，我虽然意识到了，但是写错了
# - 把len函数的结果存起来，不重复调用，也是不错的地方
# - 不过到头的时候，数组似乎也会爆掉
#----------深拷贝------------
# a = [1,3,4]
# b=a[:]
# b.append(3)
# c=a
# c.append(4)
# print(a) #[1, 3, 4, 4]
# print(b)#[1, 3, 4, 3]
# print(c)#[1, 3, 4, 4]
#-------------------

# 实例答案
# if __name__ == '__main__':
#     # 方法一 ： 0 作为加入数字的占位符
#     a = [1,4,6,9,13,16,19,28,40,100,0]
#     print ('原始列表:')
#     for i in range(len(a)):
#         print (a[i])
#     number = int(input("\n插入一个数字:\n"))
#     end = a[9]
#     if number > end:
#         a[10] = number
#     else:
#         for i in range(10):
#             if a[i] > number:
#                 temp1 = a[i]
#                 a[i] = number
#                 for j in range(i + 1,11):
#                     temp2 = a[j]
#                     a[j] = temp1
#                     temp1 = temp2
#                 break
#     print ('排序后列表:')
#     for i in range(11):
#         print (a[i])


# 优秀参考答案
# a = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
# b = 18
# a.append(b)
# c = a[:]
# l = len(c)

# # 从后面开始，如果比倒数第二个数大，那就将新加入的数填在倒数第一的位置，否则倒数第二的数位置后移
# for i in range(l,0,-1):
#    if (b>c[i-2]):
#       c[i-1] =b
#       break
#    else:
#       c[i-1] = c[i-2]
# print c