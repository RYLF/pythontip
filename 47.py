# coding=utf-8

# Title:杨辉三角

# 还记得中学时候学过的杨辉三角吗？具体的定义这里不再描述，你可以参考以下的图形：
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# ..............
# 先在给你一个正整数n，请你输出杨辉三角的前n层
# 注意：层数从1开始计数,每层数字之间用一个空格隔开，行尾不要有空格。
# 如n=2,则输出：
# 1
# 1 1

# Test
n=5

# Answer
def triangles():                    # 每行看成一个list生成器
    ret = [1]                       # 第一个元素为1
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]# 当前元素等于上两个相邻元素和
        ret.append(1)               # 最后一个元素为1
        pre = ret[:]

i = 0
for t in triangles():
    print( ' '.join(str(i) for i in t))    #list 转换字符串
    i += 1
    if i == n:  #第n行，退出
        break