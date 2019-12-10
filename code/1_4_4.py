#输入一个数，判断是否为素数
#素数的定义法则是：只能被1和自身整除的大于1的数
#

'''判断一个输入是否为素数
while True:
	value  = int(input('请输入一个整数'))
	flag = 0

	for i in range (2,value//2 + 1):
		if value % i  == 0:
			print('%d不是素数'%value)
			#注意这个标志的设置的作用
			flag = 0  
			break
		else:
			flag = 1
	if flag:
		print('%d 是素数'%value)
'''

# 输入一个判断小于它的有几个素数
# 

# 需要特别注意 range(2,2)是一个空迭代，不会报错
import math
def is_primeNmuber(num):	
	
	for i in range(2,int(math.sqrt(num) + 1)):
		if num % i == 0:
			return False
	return  True


value  = int(input('请输入一个整数'))


for i in range(2,value+1):
	if is_primeNmuber(i):
		print('%d is primerNumber'%i)
