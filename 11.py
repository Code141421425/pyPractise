
#https://www.runoob.com/python/python-exercise-example11.html
#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

##分析：
#1.这个类似一个应用题，所以应该按照题干，得出对应的方程，之后在根据输入的变量，进行计算
#2.初始值a = 2,时间间隔为t = 3，生育数量为r=2
#3.若设每月的结果为T，则 T0 = 2，T1 =T0 + T0*2/2 = 4(if n>nt)    
#4.题干读错了，是每个月生1对

# class Rabbit():

#     fristRabbt = 2
#     brithDuration = 3
#     brithNumber = 2
#     newBornProtect = 3
#     RabbitStatus = [0,0,0] #距离还剩1，2，3天可生育
#     brithAvaliableRabbit = 0

#     def __init__(self):
#         self.toatlNumber= self.fristRabbt
#         self.inputTime = 0


#     #装填程序:将顶部弹出，并将新生的兔子入列,返回新生可生育数量
#     def monthPassNumber(self):
#         newBrithAvaliable = self.RabbitStatus.pop(0)
#         self.brithAvaliableRabbit += newBrithAvaliable
#         newBorn = (self.brithAvaliableRabbit/2)*self.brithNumber 
#         self.RabbitStatus.append(int(newBorn))

#         return newBrithAvaliable

#     def dc_mpn(self):
#         self.RabbitStatus = [1,2,3]

#         for i in range(5):
#             pass
#             #self.monthPassNumber(i+5)
#             #self.printStatus()
        

#     #print(RabbitStatus)
#     def run(self):
#         #第一次装填
#         self.RabbitStatus[2] = self.fristRabbt
#         #newbaby = 0
#         while True:
#             if self.inputTime > 0:
#                 self.inputTime -= 1
#                 self.brithAvaliableRabbit += self.monthPassNumber()
#                 #self.printStatus()
#             else:
#                 break

#         self.toatlNumber = self.brithAvaliableRabbit 

#         for i in self.RabbitStatus:
#             self.toatlNumber += i

#         #self.printStatus()

#     def printStatus(self):
#         print(self.RabbitStatus)#,end=" ")
    
#     def clear(self):
#         self.RabbitStatus = [0,0,0] 
#         self.brithAvaliableRabbit = 0
#         self.toatlNumber = 0

# a = Rabbit()
# # a.inputTime = 4
# # a.run()
# # print(a.toatlNumber)
# #a.dc_mpn()

# a.inputTime = 0

# for i in range(1,20):
#     a.inputTime = i
#     a.run()
#     #print("=========%d========="%i,end="")
#     print(int(a.toatlNumber/2))
#     a.clear()
#     pass

# #print(int(toatlNumber))



##总结
#太难了，真是坑死自己了，明天接着弄吧
#第3个月起，也就是说protect数列应该只有两组，妈蛋，审题错误

class Rabbit():

    fristRabbt = 2 #首批兔子
    brithDuration = 3 #等待周期
    brithNumber = 2 #出生数量
    newBornProtect = 2 #出生后，多长时间才可生育
    
    RabbitStatus = [0,0] #距离还剩1，2天可生育
    brithAvaliableRabbit = 0 #可生育兔子数量 

    def __init__(self):
        self.toatlNumber= self.fristRabbt
        self.inputTime = 0


    #装填程序:将顶部弹出，并将新生的兔子入列,返回新生可生育数量
    def monthPassNumber(self):
        newBrithAvaliable = self.RabbitStatus.pop(0)
        self.brithAvaliableRabbit += newBrithAvaliable
        newBorn = (self.brithAvaliableRabbit/2)*self.brithNumber 
        self.RabbitStatus.append(int(newBorn))

        return newBrithAvaliable

    def dc_mpn(self):
        self.RabbitStatus = [1,2,3]

        for i in range(5):
            pass
            #self.monthPassNumber(i+5)
            #self.printStatus()
        

    #print(RabbitStatus)
    def run(self):
        #第一次装填
        self.RabbitStatus[1] = self.fristRabbt
        #newbaby = 0
        while True:
            if self.inputTime > 0:
                self.inputTime -= 1
                self.brithAvaliableRabbit += self.monthPassNumber()
                #self.printStatus()
            else:
                break

        self.toatlNumber = self.brithAvaliableRabbit 

        for i in self.RabbitStatus:
            self.toatlNumber += i

        #self.printStatus()

    def printStatus(self):
        print(self.RabbitStatus)#,end=" ")
    
    def clear(self):
        self.RabbitStatus = [0,0] 
        self.brithAvaliableRabbit = 0
        self.toatlNumber = 0

a = Rabbit()
# a.inputTime = 4
# a.run()
# print(a.toatlNumber)
#a.dc_mpn()

a.inputTime = 0

for i in range(1,20):
    a.inputTime = i
    a.run()
    #print("=========%d========="%i,end="")
    print(int(a.toatlNumber/2))
    a.clear()
    pass

#print(int(toatlNumber))


##总结2 
#1.审题错误，最为致命
#2.没有好好分析至伪代码，更为致命（多bug，难调试，耗时变得极长）
#3.最基础的方法，是要做单测的，至少写完后直接测试确认完成
#4.代码复杂度一写上来，该有的最好都要有（单测，具体的实现与分析，完整的类写法）
#5.代码写到多复杂，也应该是一开始分析的时候决定的
#6.也就是说，分析包括：解题分析，程序规模预测，逻辑实现，伪代码实现（也就是之前老师说的话是真的：不要急着写代码，其实只占30%时间的感觉）
#7.对于应用题，我认为应该按照程序的方法做，多写写代买，毕竟我做这些是为了提升自己的代码水平，而不是数学水平
