# 依次接受用户输入的三个数，排序后打印
# 使用max完成

num1 = [1,3,2]

'''
while num1:
	#value = max(num1)
	value = min(num1)
	num1.remove(value)
	print(value)
'''

#num1.sort(reverse = True)
num1.sort()
print(num1)