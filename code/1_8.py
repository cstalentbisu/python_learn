#英寸与厘米之间的转换
#输入：单位是in 或者英寸 ，表示输入的事英寸
#输入的单位是cm或者厘米，表示输入的是厘米
# 1 in = 1 cm * 2.54
# 
'''
value = float(input('请输入长度数值'))
unit = input('请输入单位')

if unit == '厘米' or unit == 'cm':
	print('%.2f 厘米是 %.2f 英寸'%(value ,value / 2.54))
elif unit == '英寸' or unit == 'in':
	print('%.2f 英寸是 %.2f 厘米'%(value ,value * 2.54))
else:
	print('单位输入错误')
'''

value_input = input('请输入长度： ')
unit = value_input[-2:]
value = float(value_input[:-2])
if unit == '厘米' or unit == 'cm':
	print('%.2f 厘米是 %.2f 英寸'%(value ,value / 2.54))
elif unit == '英寸' or unit == 'in':
	print('%.2f 英寸是 %.2f 厘米'%(value ,value * 2.54))
else:
	print('单位输入错误')
