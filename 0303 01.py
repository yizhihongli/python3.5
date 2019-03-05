# 迭代器
'''
可被for循环的数据类型
list
dic
str
set
tuple
f = open()
range
enumerate 枚举


'''

# 可用dir()函数打印出数据类型的可用函数
# print(dir({})) # ['__class__', '__contains__',  …… , 'clear', 'copy', 'fromkeys', 'update', 'values']
#
# # 双下划线方法
# print([1].__add__([2]))
# print([1]+[2])


'''
迭代器：
Iterable 可迭代的  ---> __iter__ 只要含有__iter__方法都是可迭代的
[].__iter__()迭代器 --> __next__ 可从迭代器中一个一个的取值

可迭代协议：只要含有__iter__方法都是可迭代的
迭代器协议：内部含有__iter__和 __next__的方法就是迭代器
可for循环的都是可迭代的
可迭代的.__iter__()方法就可以得到一个迭代器

迭代器的好处
1. 可以一个一个取值
2.节省内存空间
'''


# 生成器函数

'''
1.含有yield的函数就是生成器函数
2.yield不能与return共存
3.yield只能用在函数中
'''

# def generator():
#     print('1')
#     yield 'aaaaa'
#     print('2')
#     yield 'bbbb'


# g = generator()
#g()  # 输出为错误 与return 不同，yield是返回的一个迭代器，不能直接调用


#g.__next__()   # 输出为1
#g.__next__()   # 输出为2

# print(g.__next__())   # 输出为1
# print(g.__next__())   # 输出为2

# 可用for循环
# for i in g:
#      print(i)


# 文件监听输入   如果输入的一行字符串中包含hhh  着输出此行内容
def tail(filename):
    f = open(filename, encoding='utf-8')
    while True:
        line = f.readline()
        if line.strip():  # 去回车
            yield line.strip()

g = tail('1.txt')
for i in g:
    if 'hhh' in i:
        print('11111', i)

