#打印三角形


for i in range(0,6):
	for j in range(0,i):
		print('*',end='')
	print('')

for i in range(1,6):
	print(' '*(5-i),end = '')
	print('*'*i,end = '')
	print('')

for i in range(1,6):
	print(('*'*(2*i - 1)).center(9))
	print('')


for i in range(5,0,-1):
	print(('*'*(2*i - 1)).center(9))
	print('')