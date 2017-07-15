# coding=utf-8

# Title:最大整数

# 设有n个正整数,将他们连接成一排,组成一个最大的多位整数.
# 例如:3个整数13,312,343,连成的最大整数为:34331213
# 又如:4个整数7,13,4,246连接成的最大整数为7424613
# 现在给你一个正整数列表L，请你输出用这些正整数能够拼接成的最大整数。
# note:测试数据已于2014年11月13日更新，以前通过的代码不一定能够再次通过。

# Test
L=[13,312,343]
# L=[7,13,4,246]

# Answer
# permutations(L,len(L) 全排列列表
# map(str,elem)--列表中元素变成字符串
# '',join 将列表转换成字符串
# int()在转换成整形
# max选取最大的数
from itertools import *
newL = [int(''.join(map(str,elem))) for elem in permutations(L,len(L))]
print (max(newL))
