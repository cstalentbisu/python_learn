#math.ceil() 比参数大一点的数，向上取整
#math.floor() 比参数小一点的数，向下取整
#round() round有进位的效果 四舍六入，5取偶数
#round()

import math

'''
print(math.ceil(2.1))
print(int(1//2))
print(int(-1//2)) # 需要特别注意

count = 0
for i in range(11,100):
	if i//10 < i%10 :
		count += 1
		print(i)
print('the count of number is %d'%count)



#列表的初始化的集中形式
l1 = list()
l2 = [1,23,3,'abc']
l3 = list(range(10))
l4 = []
l5 = [1,2,'a',[1,2],(1,2),{1,2,3},{'a':2,'b':2}]
print(l5)

lst = [i for i in range(10, 100) if i / 10 < i % 10]
print(len(lst), lst)
'''
#每日一练
#找出5位数范围内的所有回文数，
#回文数就是正着反着都一样的数，
#例如12321，12421，13531这样的

list1 = list()

num = 12522
flag = 1

while num:
	list1.append(num % 10)
	num = num // 10

l2 = list1.copy()
list1.reverse()
if l2 == list1:
	print('right')
else:
	print('wrong')