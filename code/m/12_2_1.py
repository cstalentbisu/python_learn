# (lambda *args:args)()                                  # 返回一个空元组

# (lambda *args:*args)()                                  # 会报错，报错原因,参数解构不能单独使用

# print((lambda *args:(*args))())                       # 出错，*args不能使用（）结构，（）被解释成生成器

# print((lambda *args:[*args])(range(10)))                # 正确，*args可以使用[] 列表解构

# print((lambda *args:[*args])(range(10)))                # 打印[range(0,10)]

# print((lambda *args:[args])(range(10)))                # 打印[(range(0,10),)]

# print((lambda *args:[args])(*range(10)))                # 打印[(1,2,3,4,5,6,7,8,9)]

# print((lambda *args:[*args])(*range(10)))               # 打印[0,1,2,3,4,5,6,7,8,9]

print((lambda *args:[x for x in args])(range(10)))          # [range(0,10)]

print((lambda *args:[x for x in args])(*range(10)))         # [0,1,2,3,4,5,6,7,8,9]

print((lambda *args:{x for x in args})(*range(10)))         # {0,1,2,3,4,5,6,7,8,9}

print((lambda *args:{x%2 for x in args})(*range(10)))       # {0,1} 注意去重

print((lambda *args:(x for x in args))(*range(10)))         # ()注意不在是元组，是一个生成器表达式

