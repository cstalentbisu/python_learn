#嘉定用户名是admin 密码是：123456
#如果验证通过，打印成功，否则打印用户名或者 密码错误
#
#需要特别注意： eval(input('请输入'))，将会出错：
#eval('3*2') 返回6
#eval('hello') 会出错
#eval() 用来执行一个字符串表达式，并返回式的值
#x = 7 ,eval(x *3) 返回21
#eval(pow(2,3)) 返回8 ，整形
#n = 81 eval("n+4"),返回85，整形

while True:
	name = input('请输入用户名：')
	passwd = input('请输入密码')
	if name == 'admin' and passwd == '123456':
		print('登录成功')
	else:
		print('用户名或者密码错误')
