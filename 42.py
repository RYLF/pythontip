# coding=utf-8

# Title:分拆素数和

# 把一个偶数拆成两个不同素数的和，有几种拆法呢？
# 现在来考虑考虑这个问题，给你一个不超过10000的正的偶数n，
# 计算将该数拆成两个不同的素数之和的方法数，并输出。
# 如n=10，可以拆成3+7，只有这一种方法，因此输出1.

# Test
n=10

# Answer
def prime_number(p):
	for i in range(2,p):
		if p %i == 0:
			break
	else:
		return True

count = 0
for i in range(2,n/2):
	if  prime_number(i) == True and prime_number(n-i) == True :
		count +=1
print count