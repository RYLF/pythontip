# coding=utf-8

# Title:回文数 II

# 又是回文数！但这次有所不同了。
# 给定一个N进制正整数，把它的各位数字上数字倒过来排列组成一个新数，然后与原数相加，如果是回文数则停止，如果不是，则重复这个操作，直到和为回文数为止。
# 如果N超过10，使用英文字母来表示那些大于9的数码。例如对16进制数来说，用A表示10，用B表示11，用C表示12，用D表示13，用E表示14，用F表示15。
# 例如：10进制87则有：
# STEP1: 87+78=165
# STEP2: 165+561=726
# STEP3: 726+627=1353
# STEP4: 1353+3531=4884
# 给你一个正整数N(2<=N<=16)和字符串M（"1"<=M<="30000"(10进制)）,表示M是N进制数，输出最少经过几步可以得到回文数。
# 如果在30步以内（含30步）不可能得到回文数，则输出0。输入的数保证不为回文数。
# 如N=10, M="87", 则输出4.注意：M是以字符串的形式给定的。

# Test
N, M = 10, "87"


# Answer
# N进制转换为10进制
def ntt(num,base):
    result = 0
    for i in range(len(num)):
        result += int(num[i], 16)*base**(len(num)-1-i)   # int(num[i],16) --将16进制字符串转换成10进制
    return str(result)


# 10进制转换为N进制
def ttn(num,base):
    a = []
    num = int(num)
    while num != 0:
        b = num % base       # 求余
        a.append('%X'% b)   # 将末尾加入列表
        num = int(num/base)
        result = ''.join(str(i) for i in a[::-1])   #逆序列表为结果赋值
    return result

step = 0
while step <= 30:
    P = M[::-1]         # 反转
    M = int(ntt(M, N))  # 进制转换
    P = int(ntt(P, N))  # 进制转换
    M = M + P           # 求和
    M = ttn(str(M), N)  # 进制转换
    step += 1
    if M == M[::-1]:    # 对比结果
        break

if step < 30:
    print(step)
else:
    print(0)