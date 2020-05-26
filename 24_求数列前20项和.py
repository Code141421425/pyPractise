#https://www.runoob.com/python/python-exercise-example24.html
#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
#

#分析：
# 总述：看到这题第一个反应，就是分子分母分别存在一个数组里求前n项和，
#       然后在通过一个合成函数将这两个数组合并起来，求和
#       不过问题是合并的时候，肯定是除完之后，用一个小数相加，这样势必会对精准度造成影响。如果求前n项和的最大公约数分母，又会非常复杂1
#       不过想想也可以看看有没有分数相关的函数库支撑一下
#       查了一下，有个fraction的函数，可以用下。感觉还不错.
#       不过这么一想，递归是不是也挺好的？



# # fraction 调研
# from fractions import Fraction

# f = Fraction(1,2)

# print(f)

# print(f.denominator) # 可以调取分母
# print(f.numerator) # 可以调取分子

# # 递归调研
# def a(x):
#     if x == 1:
#         return 1 
#     return x * a(x-1)

# print(a(100))

# 思路：由题可得，下一项的分子是前一项的分子与分母已和，分母是前一项的分子
#       ∴ an+1/bn+1 = (an + bn )/an
#       ∵ 首项 = 1/2  ∴

from fractions  import Fraction
f1 = Fraction(1,2)
#f2 = Fraction(2,3)


def py24(x):
    if x == 1:
        return Fraction(2,1)
    return Fraction(py24(x-1).denominator+py24(x-1).numerator,py24(x-1).numerator).real #+ py24(x-1)

sum =0
# for i in range(1,21):
#     a = py24(i)
#     print(a)
#     #sum += a
    
    
#print(998361233/60580520)
# 第1——10 项  998361233/60580520

# #
# 2
# 3/2
# 5/3
# 8/5
# 13/8
# 21/13
# 34/21
# 55/34
# 89/55
# 144/89
# 233/144
# 377/233
# 610/377
# 987/610
# 1597/987
# 2584/1597


#终于就像军少说的，递归写起来真的简单，但是性能消耗真的大。要是用一些数组来村，估计可以秒出



# 为了出个答案换种方法来一发

#
denominator = [1]
numerator = [2]
f = []
times = 20

#得出数列
for i in range(times):
    numerator.append(denominator[i]+numerator[i])
    denominator.append(numerator[i])

#合成二维数组
for x in range(times):
    f.append([numerator[x],denominator[x]])

print(f)

#公倍数
def getCommonMultiple(FA,FB):
    return [FA[0]*FB[1]+FA[1]*FB[0],FA[1]*FB[1]]

# 得出分数
sum = 0
for b in range(times-1):
    if b == 0:
        sum = getCommonMultiple(f[b],f[b+1])
    else:
        sum = getCommonMultiple(sum,f[b+1])

print(sum)
print(sum[0]/sum[1])

#302163077445280087617864490505  /  9251704366605890848773498384


# 实际上最后并没有区别[捂脸哭]