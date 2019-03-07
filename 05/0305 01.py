# 列表推导式和生成器表达式
'''
区别
1.有无括号
2.返回值不一样
3.生成器表达式几乎不占内存
'''
# list1 = ['hhh%s'%i for i in range(10)]  # 列表推导式  ['hhh0', 'hhh1',…, 'hhh9']
# print(list1)
#
# g = ('hhh%s' % i for i in range(10))
# for i in g:
#     print(i)  # 生成器表达式  hhh0 … hhh9


# 推导式进阶
'''
[每个元素或元素的相关操作 for 元素 in 可迭代数据类型]    遍历处理
[每个元素或元素的相关操作 for 元素 in 可迭代数据类型 if 元素相关条件 ]    遍历处理
 '''

# list2 = [i for i in range(31) if i % 3 == 0]
# print('31以内可被3整除的数%s' % list2)  # 31以内可被3整除的数[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


#生成器只能取一次，再取就为空

# 例1
def fun1():
    for i in range(4):
        yield i

g = fun1()
g1 = (i for i in g)
g2 = (i for i in g1)

'''
#case1
print(list(g1))  # [0, 1, 2, 3]
print(list(g2))  #g1已经取过了，g2要再从g1取 所以为  []
'''

'''
#case2
print(list(g1))  # [0, 1, 2, 3]
print(list(g1))  #g1已经取过了所以为 []
print(list(g2))  # []
'''

'''
#case3
print(list(g))  # [0, 1, 2, 3]
print(list(g1))  #g 已经取过了，g1要再从g取 所以为 []
print(list(g2))  # []
'''

# 例2

def fun1(n,i):
    return n+i

def fun2():
    for i in range(4):
        yield i

g = fun2()
for n in [1, 10]:
    g = (fun1(n, i) for i in g)

print(list(g))  # [20, 21, 22, 23]

'''
for n in [1, 10]:
    g = (fun1(n, i) for i in g)
可替换为
n = 1
 g = (fun1(n, i) for i in g) 但是此时g不执行

n = 10
g = (fun1(n, i) for i in g)

当list(g)时，会执行
n = 10
g = (fun1(n, i) for i in g) 寻找g
从
n = 1
g = (fun1(n, i) for i in g)取g
此时g从生成器取(0 1 2 3)
则
n = 10
g = (fun1(n, i) for i in g) 可化为
g = (fun1(n, i) for i in (fun1(n, i) for i in g)) 化为
g = (fun1(n, i) for i in (fun1(n, i) for i in (0 1 2 3)))
即：
g = (fun1(10, i) for i in (fun1(10, i) for i in (0 1 2 3)))
即：[20, 21, 22, 23]

意思就是当list的时候才从下到上寻找g  执行上面的代码，不list的时候 不做操作
'''















