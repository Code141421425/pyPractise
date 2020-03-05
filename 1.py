
#https://www.runoob.com/python/python-exercise-example1.html


# stack = []
# for i in range (1,5):
#     stack.append(i)

# print(stack[1])

# for i in range(4):
#     #a = stack.pop()
#    print(stack.pop())

i = 0

# 方法1
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a != b: 
                if a !=c:
                    if b != c:
                        i=i+1
                        print(str(a)+str(b)+str(c))

print(i)


#总结：关注and 和&，|，等的区别