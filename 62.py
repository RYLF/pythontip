# coding=utf-8

# Title:IP判断

# 互联网上的每台计算机都有一个IP，合法的IP格式为：A.B.C.D。
# 其中A、B、C、D均为位于[0, 255]中的整数。为了简单起见，我们规定这四个整数中不允许有前导零存在，如001这种情况。
# 现在给你一个字符串s(s不含空白符),请你判断s是不是合法IP，若是，输出Yes,否则输出No.
# 如：s="202.115.32.24", 则输出Yes;
#     s="a.11.11.11", 则输出No.

# Test
s="202.115.32.24"
# s="a.11.11.11"

# Answer
def isok(s):
    if s.isdigit() and int(s)>=0 and int(s)<=255 : #判断字符为数字，判断字符大于0，小于255
        return 1
    else:
        return 0

if sum(map(isok,s.split('.')))==4: # 计算返回序列的和
    print ('Yes')
else:
    print ('No')