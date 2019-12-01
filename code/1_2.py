# 使用变量保存数据，并进行算术运算
#

a = 123
b = 321

print(a + b)
print(a * b)
print(a - b)
print(a / b)

#取整数运算
print(a // b)

#取模运算
print(a % b)

#指数运算
print(a ** 2) 

print('*'*20)

# 使用type() 检查变量类型
# 

a = 123

b = 12.345


# 1 + 5j   和 1 + 5J 是一样的
c = 1 + 5J

d = 'hello world'

e = True #注意首字母大小写的问题

print (type(a))
print (type(b))
print (type(c))
print (type(d))
print (type(e))

print('*'*20)

# 1、input 函数的使用
# 2、int()函数，办参数转换成整数
# 3、print() 函数输出带占位符的字符串
# 

a  = int(input('a = '))
b  = int(input('b = '))

print('%d + %d = %d'%(a,b,a+b))
print('%d  - %d = %d'%(a,b,a-b))
print('%d * %d = %d'%(a,b,a*b))
