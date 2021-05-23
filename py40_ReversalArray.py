# https://www.runoob.com/python/python-exercise-example40.html

# 讲一个数组逆序输出

# I
# 碎碎念：这不就是直接将自己最后一位，给一个新的数组的第一位，以此类推就行了么


def py40(array):
    reversalArray = []

    for i in range(len(array), 0, -1):
        reversalArray.append(i)

    return reversalArray


if __name__ == "__main__":
    list = [1, 2, 3]
    print(py40(list))
    pass

# ------实例答案--------
# if __name__ == '__main__':
#     a = [9,6,5,4,1]
#     N = len(a)
#     print (a)
#     for i in range(len(a) // 2):
#         a[i],a[N - i - 1] = a[N - i - 1],a[i]
#     print (a)

# -----优秀参考答案-----------
    # a = [9,6,5,4,1]
    # print a[::-1]

# --------
# a = [9,6,5,4,1]
# a.reverse()

# 总结
# - 这个实例答案看起来有点儿迷，大概是想不靠已经存在的算法，基础实现吧，写的逻辑还算是有点儿意思
# - 看起来好像很便捷的编写，不过主要还是在易维护上吧，能够更好的表达逻辑
# a = [1, 2, 3, 4]
# a[0], a[3], a[2] = a[3], a[0], a[1]
# print(a)
