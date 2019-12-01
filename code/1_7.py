# 根据 变量的范围求分段函数的值。
# 
#注意格式化输出的原理
#
while True:
        input_x = float(input('x = '))

        if input_x > 1:
                output_y = 3 * input_x - 5
        elif input_x >= -1:
                output_y = input_x + 2
        else:
                output_y = 5 * input_x + 3

        print('f(%.2f) = %.2f'%(input_x,output_y))
