# 求1到100的和
#range(101),产生0 - 100 之间的整数，间隔为1
#range(1,100)产生1 - 99 之间的整数，间隔为1
#range（1,100,2）产生1到99之间的基数，步长为2
#

''' 求1到100 的和
sum = 0 

for i in range(101):
	sum = sum + i	
print('the result is %d'%sum)
'''

''' 求1 到100之间偶数的和 方法一
sum = 0
for i in range(0,101,2):
	sum += i
print('the result is %d'%sum)

'''
''' 求1 到100之间偶数的和 方法二
sum = 0

for i  in range (1,101):
	if i%2 == 0:
		sum += i
print('the result is %d'%sum)
'''

