# coding=utf-8

# Title:相同数字

# 给你一个整数列表L,判断L中是否存在相同的数字，
# 若存在，输出YES，否则输出NO。

# Test
L = [1,2,3,2]

# Answer
for i in L:
    if L.count(i) != 1:
        print("YES")
        break
else:
    print("NO")