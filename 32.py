# coding=utf-8

# Title:三角形形状

# 给以一个三角形的三边长a,b和c(边长是浮点数),请你判断三角形的形状。
# 若是锐角三角形，输出R,
# 若是直角三角形，输出Z，
# 若是钝角三角形，输出D，
# 若三边长不能构成三角形，输出W.

import math

# Test
a,b,c =3,3,3   # 锐角
# a,b,c =3,4,5 # 直角
# a,b,c =3,3,5 # 钝角
# a,b,c =3,3,6 # 不能构成三角形

# Answer
s=sorted([a,b,c]) #列表排序

#三角形最大边小于其余两边和
if s[0]+s[1]>s[2]:
    if s[0]**2+s[1]**2==s[2]**2:  #两边平方等于第三边平方是直角三角形
        print "Z"
    elif s[0]**2+s[1]**2>s[2]**2: #两边平方大于第三边平方是锐角三角形
        print "R"
    elif s[0]**2+s[1]**2<s[2]**2: #两边平方小于第三边平方是钝角三角形
        print "D"
else:
    print "W"