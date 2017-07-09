# coding=utf-8

# Title:加油站

# 一个环形的公路上有n个加油站，编号为0,1,2,...n-1,
# 每个加油站加油都有一个上限，保存在列表limit中，即limit[i]为第i个加油站加油的上限，
# 而从第i个加油站开车开到第(i+1)%n个加油站需要cost[i]升油,cost为一个列表。
# 现在有一辆开始时没有油的车，要从一个加油站出发绕这个公路跑一圈回到起点。
# 给你整数n，列表limit和列表cost,你来判断能否完成任务。
# 如果能够完成任务，输出起始的加油站编号，如果有多个,输出编号最小的。
# 如果不能完成任务，输出-1。

# Test
n = 5
limit = [1,1,1,1,1]
cost  = [1,1,1,1,1]

# Answer
gas=0
res=[]
for i in range(n):          # 从第0加油站开始遍历
    gas=0                    # 油量
    for j in range(n):      # 模拟绕一圈加油与耗油过程
        gas+=limit[(i+j)%n] # 每一站都加满油
        gas-=cost[(i+j)%n]  # 开到第i+j站的耗油
        if gas<0:break      # 小于0，不能完成任务，直接跳出循环
    if gas>=0:
        res.append(i)
if len(res)==0:             # 不能完成任务，列表里无值
    print -1
else :
    print sorted(res)[0]# 能完成任务，打印最小值