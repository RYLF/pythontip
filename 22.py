# coding=utf-8

# Title:时间就是金钱

# 给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 请你给出这两个时间间隔的秒数。
# 如：st="00:00:00", et="00:00:10", 则输出10.

# Test
st,et="00:00:00","00:00:10"
# Answer
def str_second(str):
    list = str.split(":")
    return int(list[0])*3600 +  int(list[1])*60 + int(list[2])

interval = str_second(et)-str_second(st)
print interval
