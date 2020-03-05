#https://www.runoob.com/python/python-exercise-example9.html
#暂停一秒输出。

##分析：
# 去时间相关的函数里边找找什么延迟启动的东西，是在不行就搞个python库（应该不至于）
# 可能还得去看看进程相关的东西

import time

time.sleep(3)
print(1)


##总结
#确实就是sleep