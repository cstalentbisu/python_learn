# 字典set使用总结

## 字典的概述及初始化

1. 字典是 **可变的，无序的**容器

## 字典的初始化
```
d1 = dict()  # 空字典 dict() -> new empty dictionary
d2 = {} # 大括号用于dict，而不是set

d3 = dict(name = 'bisu',year = '1964',addr = 'dingfuzhuang')
 #注意name不能用单引号，双引号
 #dict(mapping) -> new dictionary initialized from a mapping object's
 #(key, value) pairs
d4 = {'a':1,'b':2,'c':3,'e':['a','b','c'],'f':(1,2),'g':(1,)}
# value可以是任意类型，key一定要是能hash的
# dict(**kwargs)
d5 = dict(d3)
d5 == d3  # True
d6 = dict.fromkeys(['a','b','c'],0)
d6
d7 = dict(((1,2),))
d8 = dict(([1,2],('a','b'),{'e','f'})) # 注意 e 和 f 谁是key，谁是value不清楚
# dict.fromkeys(iterable, value=None, /)
```

## 字典元素的访问及遍历
```
d4 = {'a':1,'b':2,'c':3,'e':['a','b','c'],'f':(1,2),'g':(1,)}
d4['a']
#d4[2]  会出错，字典是无序的，所以不能索引访问
# d4.get('M') # 如果key不在字典中，不会报错
# d4['M'] # 如果key不在字典中，会报错

# 取得key的方法

for k in d4:
    print(k)    #注意取出来的是key

for k,_ in d4.items():
    print(k)

for k in d4.keys():
    print(k)
    
# 取得value的方法

for _,v in d4.items():
    print(v)

for k in d4:
    print(d4[k])

for v in d4.values():
    print(v)

```

## 字典的修改和删除
```
d3 = dict(name = 'bisu',year = '1964',addr = 'dingfuzhuang') #注意name不能用单引号，双引号
d4 = {'a':1,'b':2,'c':3,'e':['a','b','c'],'f':(1,2),'g':(1,)}

d3.setdefault('abc','test')  #需要注意返回值，如果key在keys中，就地修改后返回test，否则返回'abc'对应的value
d3.update(d4) update，是一个可以迭代的对象，

d3['abc'] = 'test_update'

其实字典没有所谓的修改：如果key在keys中，则更新value值，否则增加新的key value对

```