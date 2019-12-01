#编写程序，完成以下要求
#将一串字符串'132569874'转换成列表并将其输出
#对其中偶数下边的元素进行降序排列，技术下表的元素不便


num = list ('132659874')
print(num)
num_even_list = num[::2]
print(num_even_list)
num_even_list.sort(reverse = True)
print(num_even_list)
num[::2] = num_even_list
print(num)
