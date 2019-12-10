#完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
#例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。
#找1000以内的完美数

re_value = 0

for per_value in range(1,100000):
	for i in range(1,per_value):
		if per_value % i == 0:
			re_value += i
	if re_value == per_value:
		re_value = 0
		print('%d is perfect number'%per_value)
	re_value =0