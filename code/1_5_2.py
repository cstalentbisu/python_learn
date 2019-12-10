# 把一个输入的数字例如：123456，转换成654321
#

value_input = 123.456
#int(input('请输入一个整数 '))

reverse_value = 0

while value_input > 0:
	reverse_value = reverse_value * 10 + value_input%10
	value_input //= 10

print('result reversed is %d'%reverse_value)
