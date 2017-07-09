# coding=utf-8

# Title:序列判断

# 给你一个整数组成的列表L，按照下列条件输出：
# 若L是升序排列的,则输出"UP";
# 若L是降序排列的,则输出"DOWN";
# 若L无序，则输出"WRONG"。

# Test
L = [1,2,3]
# L = [3,2,1]
# L = [3,1,2]

# Answer
if sorted(L) == L:
    print ("UP")
elif sorted(L,reverse=1) == L:
    print ("DOWN")
else:
    print ("WRONG")