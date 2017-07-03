# coding=utf-8

# Title:公约数的个数

# 给你两个正整数a,b,  输出它们公约数的个数。
# 例如：a = 24， b = 36
# 则输出：6

# Test
a,b = 24,36

# Answer
count = 0
for i in range(1,min(24,36)):
    if (a%i == 0 and b%i == 0):
        count += 1
print count