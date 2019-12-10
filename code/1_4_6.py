#计算两个输入值，x,y的最大公约数和最小公倍数
#

x = int(input('x= '))
y = int(input('y= '))

if x > y:
	x,y = y,x

for factor in range(x,0,-1):
	if x % factor == 0 and y %factor == 0:
		print('%d 和 %d 最大公约数是%d'%(x,y,factor))
		print('%d 和 %d 最大公倍数是%d'%(x,y,x*y//factor))
		break
