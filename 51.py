# coding=utf-8

# Title:降序排序

# 给你一个list L, 如 L=[2,8,3,50], 对L进行降序排序并输出,
# 如样例L的结果为[50,8,3,2]

# Test
L=[2,8,3,50]

# Answer
L.sort()     	#排序（正序）
print L[::-1] 	#逆序