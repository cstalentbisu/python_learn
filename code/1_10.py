#输入三角形的三个变长，求三角形的周长和面积
#注意两边之和大于第三边，两边之差小于第三边
#注意三角形三边的面积公式


def is_angle(a,b,c): 
	if a + b > c and a + c >b and b + c > a and a - b< c and a - c < b and b - c < a: 
		return True 
	else: 
		return False

def perm_angle(a,b,c):
	if is_angle(a,b,c):
		return a + b + c
	else:
		return 0

def aera_angle(a,b,c):
	if is_angle(a,b,c):
        p = perm_angle(a,b,c)
		return (p*(p-a)*(p-b)*(p-c)) ** 0.5
	else:
		return 0

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

print('the perim is %.2f , the aera is %.2f'%(perm_angle(a,b,c),aera_angle(a,b,c)))
