# https://www.runoob.com/python/python-exercise-example28.html

#有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？


# II 
# 碎碎念：这个问题感觉可以用递归来搞，再加上之前的几道题都是用递归的。这5个人之间的关系，可以用数组存储，然后递归算出第5个人
#         关于条件的存储，就用正负x来表示,第多少个人，就用数组中对应的位置标示
def py28():
    ##data 
    condition = [2,2,2,2]
    first = 10
    reslut = 0

    def ageSum(reslut,pos):
        if pos < 0:
            return first+reslut
        else:
            return ageSum(reslut+condition[pos],pos-1)
    print(ageSum(reslut,len(condition)-1))

if __name__ == "__main__":
    py28()

# 总结
# 对于递归只能说是会用，但是还并不熟悉。现在还是有种应硬套公式的感觉
# 与示例相比，我在递归中多增加了一个参数，但是确实感觉真的是毫无用处的感觉（pos）