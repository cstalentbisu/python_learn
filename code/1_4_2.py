#使用while循环
#while 循环使用时候，可以不用知道循环次数，while True:
#可以使用break，终止循环
#可以使用continue，结束本次循环，进入下一次循环
#

#猜数游戏
#

import random

answer = random.randint(1,100)

count = 0

while True:
	value = float(input('请输入结果：'))
	if value > answer:
		print('答案偏大，需要小一点')
		count += 1
	elif value < answer:
		print('答案偏小，需要大一点')
		count += 1
	else:
		if count > 7:
			print('次数偏多，加油补智商')
		else:
			print('回答正确')

		break
