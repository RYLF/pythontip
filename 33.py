# coding=utf-8

# Title:大幂次运算

# 给你两个正整数a(0 < a < 100000)和n(0 <= n <=100000000000)，计算(a^n) % 20132013并输出结果

import math

# Test
a,n =10000,10000000

# Answer
ret = 1 #余数
def PowerMod(a, n, ret):
    if n == 0:          
        return ret
    if n % 2:           # n为奇数
        ret = ret * a % 20132013
    return PowerMod(a*a%20132013, n/2, ret)  #n为偶数。a^n %m = (a^2^n/2)%m = ((a^2%m)^n/2)%m

print PowerMod(a, n, ret)