# coding=utf-8

# Title:101位自复制数

# 什么叫自复制数呢？我们看看下面的例子：
# 625×625=390625
# 376×376=141376
# 9376×9376=87909376
# 90625×90625=8212890625
# 如果一个数的平方末尾还是这个数本身，那么它就是自复制数。
# 现在告诉你长度为101位的自复制数只有一个，你能把它找出来吗？请输出这个101位的自复制数。


# Test

# Answer
# 判断是否为自复制数
def copy(i):
    lista=list(str(i)) # 乘数
    listaa = list(str(i**2)) # 结果
    listaa_last = listaa[len(listaa)-len(lista):] # 结果末尾数字
    return True if listaa_last == lista else False # 判断结果末尾数字是否与乘数相同


def copymain(N):
    while (len(str(N))<101):
        for i in range(1,10000):
            out=N+10**(len(str(N)))*i # N + 10^len(N)*i
            if copy(out):  # 判断是否为自复制数
                N = out
                if len(str(N))==101: # 判读自复制数位数
                    print (N)
                break

copymain(5)     # 复制数大于10，末尾为5或者6
copymain(6)     # 复制数大于10，末尾为5或者6
