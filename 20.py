# coding=utf-8

# Title:信息加密

# 给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。这里将字母表的z和a相连，如果超过了z就回到了a。
# 例如a="cagy", b=3,
# 则输出 ：fdjb

# Test
a, b="cagy",3
e = []
# Answer
for i in range(0,len(a)):
    c = ord(a[i])+b      # 转换成整数
    if c> 122:           # 如果大于z则减去26
        c  -=  26
    e.append(chr(c))     #  加入到列表中
str = "".join(e)        # 列表和并成字符串
print str