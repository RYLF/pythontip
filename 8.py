# coding=utf-8

# Title:求中位数

# 给你一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）。
# 例如： L=[0,1,2,3,4]
# 则输出：2

# Test
L=[0,1,2,3,4]
# Answer
L.sort()
if len(L)%2==0:     #偶数
    print ((L[len(L)/2-1]+L[len(L)/2])/2.0)
else:               #奇数
    print L[len(L)/2]