# coding=utf-8

# Title:回文子串

# 给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。
# 回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba".

# Test
a,n = "aba",1
# a,n = "abc",1

# Answer
for i in range(len(a) - n+1):
    if a[i:i+n] == a[i:i+n][::-1]:
        print 'YES'
        break
else:
        print 'NO'
