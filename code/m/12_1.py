# 给定一个列表 lst1 = [1,2,'a','b'], 按照元素的ascii码进行排序，使用sorted函数
lst1 = ['1',1,2,'a','c','b']

# 使用sorted函数，str函数方法排序
#print(sorted(lst1,key=str))

# 定义一个fn函数
def fn(x):
    if isinstance(x,str):
        return ord(x)
    return x
#print(sorted(lst1,key=fn))


# 注意sorted函数 key后面放的是函数对象
print(sorted(lst1,key = lambda x : ord(x) if isinstance(x,str) else x))
