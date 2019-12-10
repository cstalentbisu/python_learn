# 字符串和常用数据结构
#
#

#字符串可以使用单引号，双引号，三引号，其中，三引号，表示可以换行，输入也是换行输出
s1 = 'hello world!'

s2 = "hello,world"

s3 = '''
hello,
world
'''

print (s1,s2,s3,end= '')


s1 = "hello world\'"
print(s1)

s1 = ''' heloo ''"  "'' world '''
print(s1)

# \ 表示转义，如果不希望转义，可以在字符串前面加上r

s1 = r'\n\t\\'
s2 = '\n\t\\'
print(s1)
print(s2) #注意比较 字符串前边加了r和没有r的区别

#注意切片操作的几个技巧
s1 = 'abcdefg'
print(s1[1:1])			#无输出
print(s1[1:2])			#输出b
print(s1[::-1])			#逆序输出，gfedcba
print(s1[1::2])			#bdf ,从下表为1开始，每两个输出
print(s1[-3:-1])		#最后一个下表为-1，一次类推，输出为：ef
print(s1[::2])			#步长为2 输出

#python中对字符串有用的内置函数

str1 = 'hello world!'

print(len(str1))				# 获取字符串的长度
print(str1.capitalize())		#Hello world! 获得字符串首字母单词大小的copy，记住一定是copy
print(str1.title())				#Hello World! 每一个单词的首字母大写的copy
print(str1.upper())
print(str1.lower())
print(str1.find('shit'))
print(str1.index('ll'))
print(str1.startswith('hel'))
print(str1.endswith('!'))
print(str1.center(50,'*'))
print(str1.rjust(50,'*'))
print(str1.ljust(50,'*'))	
print(str1.isdigit())
print(str1.isalpha())
print(str1.strip())


s3 = '''
a
b
c'''

print(len(s3))

print(len(' '))

s1 = 'abc 		def'
print(s1)
print('abc\t\t\tdef') #注意和70 71行的区别

#print('a'+1) #这是错误的，会报错的
input('>>')