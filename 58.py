# coding=utf-8

# Title:最小公倍数I

# 给你一个正整数list L, 如 L=[2,8,3,50], 求列表中所有数的最小公倍数(不用考虑溢出问题）。
# 如L=[3,5,10], 则输出30

# Test
L=[3,5,10]

# Answer
def gcd(n1,n2):     #求最大公因数
    """greatest common divisor function """
    if(n1%n2 == 0):
        return n2
    return gcd(n2,n1%n2)
f = lambda a,b:a*b /gcd(a,b)    #求最小公倍数
print reduce(f,L)