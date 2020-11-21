## https://www.runoob.com/python/python-exercise-example37.html

## 对10个数进行排序。

## I
## 碎碎念：what？ 那就实现一波基础算法，以求难度上升吧.写个冒泡？
##        难度没想到有点点高- - 



def py37(inputNumbers):
    list = inputNumbers 
    for i in range(0,len(list)-1):
        for i in range(0,len(list)-1):
            if(list[i]>list[i+1]):
                temp = list[i+1]
                list[i+1] = list[i]
                list[i] = temp
    

    return inputNumbers


# def smallNumberFirst(number,list):
#     # 在一个数列中，把一个数，冒泡到结束为止
#     for i in range(number,len(list)-1):
#         if(inputNumbers[i]>inputNumbers[i+1]):
#             temp = inputNumbers[i+1]
#             inputNumbers[i+1] = inputNumbers[i]
#             inputNumbers[i] = temp
#         else:
#             break
#     pass

if __name__ == "__main__":
    inputNumbers = [3,2,4,8,10,56,44,28,36,11,120,5]
    print(py37(inputNumbers))



# 总结

## 1.之前的一些养成的好习惯，没有贯彻到底，比如根据评级，对于不同难度的工程，进行直接写->稍微理一下思路与->注释大纲后扩充编写 ，还有标记断点，还有编写代码时的态度 等
## 2.虽然目标金金就是回忆一下很久之前的冒泡算法， 但是因为写的时候态度很浮躁，一直写不好，之后冷静下来之后，没有一会儿就写完了
## 3.对于代码的设计上来说，就一个排序嵌套了两层完整的循环，所以，效率应该挺低的。
## 4.实例用的是选择法，通过比较先选出一个最小的数，然后依次排序，也是嵌套了两层循环，不过和我写的这个冒泡相比的话，似乎好些，毕竟数值变换的次数似乎没有那么多？