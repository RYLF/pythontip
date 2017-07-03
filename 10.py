# coding=utf-8

# Title:最小公倍数

# 给你两个正整数a和b， 输出它们的最小公倍数。
# 例如：a = 3, b = 5
# 则输出：15

# Test
a ,b = 3,5
# Answer
def gcd(n1,n2):
    """greatest common divisor function """
    if(n1%n2 == 0):
        return n2
    return gcd(n2,n1%n2)

print a*b /gcd(a,b)