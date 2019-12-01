#判断输入的年份是不是闰年
#计算法则是：如果能被4整除且不能被100整除的，或者可以被400整除的
#

while True:
	year_input  = int(input('请输入年份：'))

	is_loop = year_input % 4 == 0  and year_input % 100 !=0 or year_input % 400 == 0

	if is_loop:
		print('%d 是闰年' %year_input)
	else:
		print('%d 不是闰年'%year_input) 
