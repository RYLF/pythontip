# coding=utf-8

# Title:结尾0的个数

# 给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数。(提示:不要直接相乘,数字很多,相乘得到的结果可能会很大)。
# 例如： L=[2,8,3,50],
# 则输出：2

# Test
L=[2,8,3,50]

# Answer
all = str(reduce(lambda x,y: x*y, L)) # 得出L列表值相乘结果并转换字符串
print len(all) - len(all.rstrip("0"))# 总长度-删除字符串末尾0后的长度