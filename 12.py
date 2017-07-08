# coding=utf-8

# Title:结尾非零数的奇偶性

# 给你一个正整数列表 L, 判断列表内所有数字乘积的最后一个非零数字的奇偶性。如果为奇数输出1,偶数则输出0.。
# 例如：L=[2,8,3,50]
# 则输出：0

# Test
L=[2,8,3,50]

# Answer

all = str(reduce(lambda x,y: x*y, L)) # 得出L列表值相乘结果并转换字符串
if (int(all.rstrip("0")[-1]) % 2) == 0: # 判断结尾数字是否为偶数
    print 0
else:
    print 1