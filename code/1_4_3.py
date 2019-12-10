#双重循环，打印99乘法表格
#注意print的用法，取消换行，可以使用end参数


for i in range(1,10):
	
	for j in range(1,i+1):
		print('%d * %d  = %d'%(j,i,i*j),end = '  ')
	print('')

