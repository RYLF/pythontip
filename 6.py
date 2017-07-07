# coding=utf-8

# Title:求解100以内的所有素数

# 输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）。

# Test

# Answer
result = []
for i in range(2,101):  #100以内的数
    for j in range(2,i):#2到该数之间的数遍历
        if (i % j)== 0: #判断是否为素数
            break
    else:
        result.append(i)
print(' '.join(str(c) for c in result))