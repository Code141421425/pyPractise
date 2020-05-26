#https://www.runoob.com/python/python-exercise-example26.html
#利用递归方法求5!。

# 评估：I-
# 碎碎念：简单复习下递归，快快写完
# 思路：


def py26(input):
    if input == 1:
        return input

    return py26(input-1)*input
        



if __name__ == "__main__":
    print(py26(5))

#总结：
# 差不多，还可以