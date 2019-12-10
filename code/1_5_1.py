#寻找水仙花数
#水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
#它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，
#例如：$1^3 + 5^3+ 3^3=153$。

for value in range(100,1000):
	hun_bit = value // 100
	ten_bit  = value %100 //10
	one_bie  = value %100 %10
	#注意python中的幂运算的法则
	if hun_bit **3 + ten_bit **3 + one_bie **3 == value:
		print('%d is right number'%value)