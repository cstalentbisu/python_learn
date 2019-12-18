'''
# 高阶函数
# 高阶函数应该满足至少一个条件
   1、接收一个或多个函数作为参数
   2、返回（输出）一个函数


# exampl1
def counter(base):
    def inc(step = 1):
        nonlocal base               # 需要使用nonlocal闭包
        base += step
        return base
    return inc

f1 = counter(5)
f2 = counter(5)

print(id(f1) == id(f2))             # 打印false

print(f1())                        # 打印 6,7,8
print(f1())
print(f1())

# example 2 仿照内建函数sorted ，能够为列表元素排序

import random

def sort_own(interable,*,key = None,reverse = False):
    #构建一个返回的新列表
    newlist = [ ]
    #遍历传入的列表
    for x in interable:
        for i ,y in enumerate(newlist):
            if x > y:
                newlist.insert(i,x)
                break;
        else: #else语句必须要有，否则，newlist中有的元素被重复添加了
            newlist.append(x)
    return newlist
lst_test = [random.randint(0,9) for i in range(9)]
print(lst_test)
print(sort_own(lst_test))

# example 3 仿照实现sort功能，进一步实现reverse功能
import random

def sort_own(iterable,*,key = None,reverse = False):
    newlist = [] # 构建一个新列表
    cmp = '>' if reverse else '<'
    for x in iterable:
        for i,y in enumerate(newlist):
            if eval(str(x) + cmp + str(y)):
                newlist.insert(i,x)
                break;
        else:
            newlist.append(x)
    return newlist

lst_test = [random.randint(0,9) for i in range(9)]
print(lst_test)
print(sort_own(lst_test,reverse = True))



# 自定义一个sort函数实现内建函数sort的功能，实现 reverse的功能，改进一：

import random

def sort_own(iterable,*,key = None,reverse = False):
    newlist = []
    for x in iterable:
        for i,y in enumerate(newlist):
            cmp = x > y if reverse else x < y
            if cmp:
                newlist.insert(i,x)
                break
        else:
            newlist.append(x)
    return newlist

lst_test = [random.randint(0,9) for i in range(9)]
print(lst_test)
print(sort_own(lst_test,reverse = True))

# 自定义一个sort函数，实现内建函数sort的功能，进一步实现key的功能

def sort_own(iterable,*,key = None,reverse = False):
    newlist = []
    for x in iterable:
        cx = key(x) if key else x
        for i,y in enumerate(newlist):
            cy = key(y) if key else y
            cmp = cx > cy if reverse else cx < cy
            if cmp :
                newlist.insert(i,x)
                break
        else:
            newlist.append(x)
    return newlist

lst_test = ['1',1,'b','a',2,3]
print(sort_own(lst_test,key = str,reverse = True))

# 过滤filter的用法
# 定义：filter(function,iterabel)
# 对可迭代对象进行遍历，返回一个迭代器
# funciton 参数是一个函数的参数，且返回值应当是bool类型，或者返回值等效bool类型
# funciton 参数如果是None，可迭代对象的每一个元素自身等效布尔值

def print_own(iterable):
    for i in iterable:
        print(i)

g = filter(lambda x : x%3 == 0 ,range(10))
#print_own(g)
g = filter(None,range(10))
#print_own(g)                    # 注意 0 没有返回

def fn(x):
    return x-1
g = filter(fn,range(5))         # 注意function只是把iterable的元素带入运算，结果为true的返回，否则不反悔
print_own(g)

# 映射 map的用法
# 定义 map(fucntion *iterable)  ---->map object
# 返回一个迭代器
lst1 = list(map(lambda x : 2*x +1 ,range(10)))
print(lst1)
dic1 = dict(map(lambda x:(x%5,x),range(500)))
print(dic1)
set1 = set(map(lambda x: x**2,range(3)))
print(set1)
dic2 = dict(map(lambda x,y:(x,y),range(4),'abcfd'))         # 两个可迭代对象，取少，取尽为止
print(dic2)

# 柯里化
def add(x):
    def _add(y):
        return x+y
    return _add

print(add(4)(5))
print(add('a')('b'))
# 柯里化的例子
# add(x,y,z) 改造成 add(4)(5,6)
def add(x):
    def _add(*iterable):
        nonlocal x
        for i in iterable:
            x += i
        return x
    return _add

print(add(4)(5,6,8,9))
# 柯里化的例子
# add(4)(5)(6)
def add(x):
    def _add(y):
        def __add(z):
            return x+y+z
        return __add
    return _add
print(add(4)(5)(6))
'''
# 柯里化的例子
# add(4,5)(6)
def add(*iterable):
    def _add(x):
        for i in iterable:
            x += i
        return x
    return _add
print(add(4,5)(6))
