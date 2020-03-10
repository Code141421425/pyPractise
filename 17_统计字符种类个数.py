
##https://www.runoob.com/python/python-exercise-example17.html
#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

##分析：
#1.总体流程：将输入分字符装入数组，按照ASCII码对每一个字符进行判断，之后进行统计
#2.说不定对于字符串，教程里有些可用的方法
#3.具体python查字符种类查下


#test
a = "ad:1 2 3d_+日"

# for i in a:
#     print (i)

#数据
chineseAmount = 0
englishAmount = 0 
spaceAmount = 0
numberAmount = 0
otherAmount = 0

#得到输入
inputStr = a

#将输入分解装入
opStr = inputStr

#将得到的数组，循环判断
for i in opStr:
    if '\u4e00'<= i <= '\u9fff':
        chineseAmount +=1
        pass
    #英文
    elif i.isalpha():
        englishAmount +=1
        pass
    elif i.isspace():
        spaceAmount +=1
        pass
    elif i.isnumeric():
        numberAmount +=1
        pass
    else:
        otherAmount +=1
        pass 

print("中文:%d"%chineseAmount)
print("英文:%d"%englishAmount)
print("空格数量:%d"%spaceAmount)
print("数字数量:%d"%numberAmount)
print("其他字符数量:%d"%otherAmount)


## 总结
#1.查了下字符串的内建函数，有些比较有意思的
# find()（字符串查找对应值），isalnum()（是否全部是数字），lower()（所有大写变小写）
# split()（分割字符串），
# string.splitlines([keepends])（按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。）
#2.和想法差不多，先用伪代码把结构写出来挺好的