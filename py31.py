#
#请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

# III++++
# III：由稍多的逻辑组成的结构，稍显复杂，注释需要写2级
# +有较多隐藏逻辑
# +死循环有点儿多，不太好写
# +代码量感觉有点儿大，需要一定的代码结构设计
# （+）针对字典匹配如果再做算法优化的话...
# （+）增加新的需求：当没有匹配到输入的时候，返回一定的结果，nil或者备选答案   ——先不做了，已经挺复杂的了，这个可以当做V2来做，先做出一个版本再说吧[捂脸哭]
# +间隔的时间太长了。。。

# r1
# 1、觉得使用不会变化的全称作为key来说，不是更好么！

# 碎碎念：首先需要有个星期1到7的库，然后把所有的首字母提取出来，如果有重复的就多录取一位，直到不重复为止,形成一个简称和全称的字典.虽然感觉会很麻烦看，
#       但是鉴于是练习也就不管了。
#       然后，跟与这个生成好的字典，按照输入进行匹配，如果匹配到了就终止循环break，如果没有就返回一个输入，然后继续匹配下一位。
#       从测试的角度来说，第二次的输入应该继续从在第一位的输入基础上，进行匹配。
#
# 流程：初始数
#

# 初始数据制作输入
weekInput = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weekDir = {}
weekPreAdd = []

# 初始数据处理
def py31():
    ## 循环读取所有的字符串
    ## 将字符串拆出第1位，如果字典中没有重复的value，就将全称做为key，简称为value，在字典中新add一条
    weekPreAdd = []
    for day in weekInput:
        if weekDir =={}:
            weekDir[day]= getLetter(day,1)
        else:
            #拆出第1个字母，和所有的值对比，如果不重复，就增加到weekDir中，如果重复，就多一个字母，直到不重复，或者到达自身长度
            reIn = True
            letterPos = 0 
            while(1):                
                if reIn:
                    if letterPos <= len(day):
                        letterPos += 1
                        checkLetter = getLetter(day,letterPos)
                    else:
                        print("repeat input a same word" + day)
                        break
                    #对比cl 和所有weedDir的value，如果有重复就break以多增加一位输入，否则就标记不重复
                    for v in weekDir.values():                    
                        if checkLetter == v:
                            reIn = True
                            break                        
                        else:
                            reIn = False
                else:
                    weekPreAdd.append(day)
                    weekPreAdd.append(checkLetter)
                    break
            weekDir[weekPreAdd[0]] = weekPreAdd[1]
            weekPreAdd = []


    inputStr = input("输入星期几的首字母")
    reslut = {}
    isFirst = True
    #将输入的input和所有的weekDir中的value中的第一个字母进行对比，如果没有则提示，break,如果有则把所有的符合情况的答案全都收集起来，打印
    #之后再需要输入下一个字母进行判断，直到只剩一个答案为止
    while(1):
        if isFirst:
            if reslut.__len__() !=1:
                reslut =  diffWordsInDir(inputStr,weekDir)
                isFirst = False
        else:
            if reslut.__len__() == 0:
                print("没有对应的星期")
                break
            elif reslut.__len__() != 1:
                print(reslut)
                inputStr = input("需要更多字母进行判断")
                reslut = diffWordsInDir(inputStr,reslut)
            else:
                break

    #print(reslut.__len__())S
    print(reslut)

def getLetter(word,pos):
    letter = word[0:pos]
    ### 得到单词中对应位置的字母，返回该字母
    return letter

def diffWordsInDir(w,dir):
    #将w对比dir中的所有的value，并将返回包含所有value的dir
    resDir = {}
    for k,v in dir.items():
        if v[0] == w:
            print(v[0])
            resDir[k] = v            
    return resDir

def dirGetMorePos(dir,key1,key2):
    #将字典中的key1和key2的键值，往后延伸一位
    pass


# 输入匹配循环
## 首先获取一位的输入
## 【匹配规则】将输入遍历字典——與字典中的value值的首位進行對比，之後返回結果。若有1個結果則輸出結束，兩個以上需要再次輸入一個字母，0個提示並結束。
### ps1:若果在dir中，增加一些特殊数据作为匹配的标准，比如单词的最大深度什么的，会不会对匹配有有所帮准呢？
def traversalDir(dir,input):
    #将输入遍历整个字典对比input，如果能够匹配成功，则返回对应key的字符串，若没有匹配到，返回-1
    reslut = ""
    return reslut

def GetDirValueLetter(pos,value):
    #返回value中的第pos位字母
    letter = ""
    return letter

##

if __name__ == "__main__":
    py31()


## 总结

# 1、在放下很久重新拿起来的的时候的流程：先看题目，然后就是看的是流程，然后就是看断点，然后看断点所在章节出代码继续。
#    所以主要流程是要在分层注释解析前，写好的。
#    然后就是断点的地方，最好断的比较利落，然后又特出表示：【【断点】】
#    而且断点的tag时，应该稍微写下下一步干啥
# 2、在第一次新出先的，比较有疑惑性的标记，如这次的ps1，应该加上标注