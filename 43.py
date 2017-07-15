# coding=utf-8

# Title:斐波那契数列

# 斐波那契数列为1,1,2,3,5,8...。数列从第三项起满足，该项的数是其前面两个数之和。
# 现在给你一个正整数n（n < 10000), 请你求出第n个斐波那契数取模20132013的值（斐波那契数列的编号从1开始）。

# Test
n=4

# Answer
def fib(n):
    x,y=1,1
    while(n-1):
       x,y,n=y,x+y,n-1
    return x
print fib(n)%20132013