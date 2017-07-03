#coding=utf-8
#Title:输出字符奇数位置的字符串
# 给你一个字符串 a， 输出a中奇数位置字符构成的字符串（位置编号从1开始）。
# 例如：a=‘xyzwd’
# 则输出:xzd

#Test
a = 'abcde'
#Answer
print(a[::2])