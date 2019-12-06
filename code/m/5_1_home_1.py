# 依次接受用户输入的三个数，排序后打印
# 使用分支结构完成

list1 = [3,1,1]

list_index = [0,1,2]

#完成接受用户的三次输入
#for i in range(3):
#	list1.append(int(input('>>>')))



if list1[0] > list1[1]:
	if list1[1] > list1[2]:			# 0>1 1>2
		list_index = [2,1,0]
	else:							#0>1 2>1				
		if list1[0] > list1[2]:		# 0>2 2>1
			list_index = [1,2,0]
		else:						# 2>0>1			
			list_index = [1,0,2]
else:								# 1> 0
	if list1[0] > list1[2]:			# 1>0>2
		list_index = [2,0,1]
	else:							# 1>0 2>0
		if list1[1] > list1[2]:		# 1 > 2 > 0
			list_index = [0,2,1]
		else:						# 1>0,2>0 1<2
			list_index = [0,1,2]

for i in list_index:
	print(list1[i])
	