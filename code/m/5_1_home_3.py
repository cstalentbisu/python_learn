#使用冒泡算法对列表内的数进行升序排列，并输出


''' 基本的冒泡算法
#num1 = [5,3,4,1,7,9,8,2,6]

num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count1 = 0
count2 = 0
num1_len = len(num1)

for i in range(num1_len):
	for j in range(num1_len - 1 - i):
		if num1[j] > num1[j+1]:
			value = num1[j]
			num1[j] = num1[j+1]
			num1[j+1] = value
			count2 += 1
	count1 += 1
print(num1)
print(count1)
print(count2)
'''

# 改进后的冒泡算法，如果恰好是顺序的，可以提高效率
num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count1 = 0
count2 = 0
num1_len = len(num1)

for i in range(num1_len):
	flag = True
	count1 += 1
	for j in range(num1_len - 1 - i):
		if num1[j] < num1[j+1]:
			value  = num1[j]
			num1[j] = num1[j+1]
			num1[j+1] = value
			flag = False
			count2 += 1
	if flag:
		break

print(num1)
print(count1)
print(count2)