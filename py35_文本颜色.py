## https://www.runoob.com/python/python-exercise-example35.html

## 35 文本颜色设置

# 碎碎念：这个查一下就好了吧，应该只是一个设置之类的东西
#         试了一下，不太行啊，看看实例




#!/usr/bin/env python
#-*- coding:utf-8 -*-
print("\034[40m感受痛苦！\033[0m")
print('*' * 50)
print("\033[1;31;40m您输入的帐号或密码错误！\033[0m")  




#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)



# 总结
# 实例也不行，也没有什么实质的用处，跳过
# 好像说windows的不支持，再见