## https://www.runoob.com/python/python-exercise-example38.html

## 求一个3*3矩阵主对角线元素之和。


## 

## 碎碎念：肯定是需要一个数据结构来保存这个矩阵，二维数组好了；然后就是对角线的描述，xy表示行列的话，对角线应该就是第x行的第x列个元素，也就是，然后相加应该就可以了
##       等下，对角线是两条啊！，emmmmmm，那就应该所所有对角线上的元素的和。



def py38(matrix):
    # 方法定义为输入一n*n的二维数组，返回其两条对角线上元素的和
    sumDiagonal = 0
    for x in range(0,len(matrix)):
        for y in range(0,len(matrix)):
            if x == y or x == (len(matrix)-1)-y:
                print(matrix[x][y])
                sumDiagonal += matrix[x][y]
    return sumDiagonal

if __name__ == "__main__":
    ## 1 2 3
    ## 4 5 6
    ## 7 8 9 
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(py38(matrix))
    pass


## 总结
## 1.我还以为我审题严禁，没想到漏看了一个主对角线的主字= = 
## 2.不过确实，如果只要一个参数的话，确实没有必要循环x和y，直接matrix[i][i]，就完事了
