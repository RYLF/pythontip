# coding=utf-8

# Title:判断三角形

# 给你三个整数a,b,c,  判断能否以它们为三个边长构成三角形。
# 若能，输出YES，否则输出NO。

# Test
a,b,c = 3,4,5
# a,b,c = 3,4,1
# Answer
print 'YES' if a+b>c and a+c>b and b+c>a else 'NO'