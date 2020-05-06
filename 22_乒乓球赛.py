#两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
# 有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

#分析
#流程：遍历所有的结果，并按照需要进行筛选
#核心方法：遍历比赛结果
#          甲乙两队装入数组，输入两个数组，循环嵌套，压入结果 —— x （取出）
#          既然是取出，可以使用数组中的pop：循环从A中弹出1个，然后循环B弹出一个，组成一队，AB弹出所有为止
#          new: 列出所有的结果，最后根据输出的条件进行筛选：
#               列出所有结果：
#                       流程：A中弹出第1个，B中弹出第1个，之后，在A中弹出第2个，B中弹出第2个....弹完后，重置数组
#                       【算法归总】
#                           1.先得出所有的随机顺序，在根据结果计算所结果
#                           2.将未完结果压占，计算完所有情况再弹出，以此得到所有结果。
#               筛选：将三个条件放到一个数组中，在所有结果中循环这个数组，删除包含条件的结果，得出最后的比赛名单

#          new：还是列出所有结果
#               1.将所有A中循环1个，和B匹配，匹配完成后，将这两个结果存入结果。作为第1层的节点，和结果的第1层
#               2.循环第一个结果，将符合结果的两个数，从A，B中POP出去后，执行步骤1
#               3.循环上述两步骤，直到数组为空
#          PS：结果是用三维数组存储，在循环完成之后，再打印出来
#               
#核心玩法梳理：
#       首先需要一个起始项，
#       根据起始项，配对
#       配对完成后，记录为1个节点（node），节点计入结果（reslut）中，结果计入结果集（resluts）中
#
#       根据上边的结果，循环将resluts中的reslut中的node，按照下边的方法
#       def 将一个输入的节点，从AB数组中弹出对应值，并将自己弹出记录为preNode
#       
#       之后循环根据A组第1个作为起始项（for），配对，并根据当前节点，append到对应的reslut中，resluts中
#       没有需要另加一个新的reslut
#       
#       循环至所有节点弹完节点后，AorB为空
#   
#循环梳理：
#       弹出上层节点，
#       A对B进行循环，
#       和上层节点一起记录本层节点，
#       循环完为止
#核心方法2：条件筛选

import copy

#数据初始化
A = ["a","b","c"]
B = ["x","y","z"]

resluts = []
reslut = []
node = []
ifFrist = True

##
def zhushi():
    # #for x in range(len(A)):
    # node.append(A[0])
    # for y in range(len(B)):
    #     node.append(B[y])
    #     reslut.append(copy.deepcopy(node))
    #     resluts.append(copy.deepcopy(reslut))
    #     node.pop()
    #     reslut.pop()


    # node = []
    # reslut = [] 

    # resluts.append("text")

    # for x in resluts:
    #     for y in x:
    #         pass
    #         #print(y)
    #         #print("========")
    pass
    #===================================new=======================================


#基础方法
## 根据结果，处理tempA or B，弹出对应值
## 在OperateList中，弹出所有reslut中的第nodePosInAB项
def forAB(reslut,OperateList,nodePosInAB):
    List = OperateList #copy.deepcopy(OperateList)

    #在OperateList中，循环弹出relust中的对应节点  
    for i in reslut:
        try:
            List.pop(List.index(i[nodePosInAB]))
        except:
            pass
        #tempList.pop(upNode[nodePosInAB])
        #pass
    return List

## 在B中，匹配A的结果，并且记录在resluts中
## 把nodeAL和ListB中的每一项合并为一个节点，加入到preReslut中
def matchAB(preReslut,nodeAL,ListB):
    node = []
    thisReslut = copy.deepcopy(preReslut)
    node.append(nodeAL)
    for i in ListB:
        node.append(i)
        thisReslut.append(node)
        node = []
        node.append(nodeAL)

        resluts.append(thisReslut)
        try:
            resluts.pop(resluts.index(preReslut))
        except:
            pass
        thisReslut = copy.deepcopy(preReslut)

## 打印结果
def reslutPrint(resluts):
    for i in resluts:
        print("reslut:"+ str(i))

#=====匹配结果=====#
for i in range(len(A)):
    #从AB中，弹出之前的结果，处理tempAB

    if resluts == []:
        ## 重置数组
        tempA = copy.deepcopy(A)
        tempB = copy.deepcopy(B)

        OperateA = forAB(reslut,tempA,0)#
        OperateB = forAB(reslut,tempB,1)

        matchAB(reslut,OperateA[0],OperateB)
        ifFrist = False
    else:
        thisTimeResluts = copy.deepcopy(resluts)
        for r in thisTimeResluts:
            ## 重置数组
            tempA = copy.deepcopy(A)
            tempB = copy.deepcopy(B)

            OperateA = forAB(r,tempA,0)#)
            OperateB = forAB(r,tempB,1)
            #匹配AB，记录结果
            matchAB(r,OperateA[0],OperateB)
            # for nodes in OperateA:
            #     matchAB(r,nodes,OperateB)

#=====根据结果筛选=====#
outCondition = [["a","x"],["c",'x'],['c','z']]
popList = []


for oc in outCondition:
    for r in resluts:
        if r.count(oc) != 0:
            popList.append(r)
        # try:
        #     outId = r.index(oc)
        #     resluts.pop(resluts.index(r))  
        # except:
        #     pass

for pl in popList:
    try:
        resluts.pop(resluts.index(pl))
    except:
        pass

reslutPrint(resluts) 

#print(resluts)


#总结


#循环

## 深复制AB，得到tempAB
## 处理AB，得到弹出上次节点以上的值（resluts中的一个reslut的），的tempAB
## 并将在结果中弹出该节点
## 在处理完的tempAB中，从A中随机一个，然后在B中配对，计入结果


#【思路总结】

# 存储结构：是一个以节点，结果和结果集的三维数组
# 主要思路：先对两个数组进行所有的不放回匹配，再进行条件的筛选


#【示例对比】

# 主要思路：他是利用三层的循环签到输出全部的结果，然后根据if实现的结果筛选
#   1、比较骚的是，他是用了文字的ASCII码进行数据的匹配，将数据的对应关系放到了底层，使得上层代码没有使用复杂的数据结构，最后的代码比较简单
#   2、还有一个就是其中的对应关系，他似乎用了循环结构的执行顺序作为其中的一半的键值（a,b,c）作为对比

# 【总结】
# 1.使用越复杂的（数据）结构，会导致最后的代码越复杂。

#啊啊啊啊啊啊啊啊啊   TMD终于写出来了  
#   2020/4/28