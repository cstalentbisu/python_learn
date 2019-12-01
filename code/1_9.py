#练习 if elif else用法
#如果输入的成绩在90分以上，则是A
#如果输入成绩大于等于80 小于90 ，则是B
#如果输入成绩大于等于70 ，小于80 则是C
#如果输入成绩大于等于60 ，小于79 则是D
#如果输入成绩小于60 则是E
#如果输入成绩小于0 ，则提示输入错误 
#注意 str.isdigit()的方法，是数字返回True ，否则返回False

while True:
	value_input  = input('请输入成绩 ')

	if not value_input.isdigit():
                print('请输入数字')
                continue
    value_input = float(value_input)   
	if value_input >= 90:
		print('A')
	elif value_input >= 80:
		print('B')
	elif value_input >= 70:
		print('C')
	elif value_input >= 60:
		print('D')
	elif value_input >=0:
		print('E')
	else:
		print(输入成绩错误)
