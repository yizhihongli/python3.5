# 生成器2
'''
send函数
1.send作用相当于__next__()
2.可传参数，参数传递给上面一个yield
3.第一个调yield必须用__next__()   最后一个yield不能获取外部的值

'''
# def fun1():
#     print(1)
#     yield 'aaaaa'
#     print('######')
#     print(2)
#     yield 'bbbbbbbbbbbb'

# g = fun1()
# ret = g.__next__()
# print(ret)
# ret = g.send(None)  # 此时send作用相当于__next__()
# print(ret)
'''
输出：
1
aaaaa
######
2
bbbbbbbbbbbb
'''

def fun2():
    print(1)
    count = yield 'aaaaa'
    print(count,'######')
    print(2)
    yield 'bbbbbbbbbbbb'
g = fun2()
ret = g.__next__()
print(ret)
ret = g.send('&&&&&&&&')   # 可将参数传递给上面一个yield
print(ret)
'''
输出：
1
aaaaa
&&&&&&&& ######
2
bbbbbbbbbbbb
'''

# 例子  移动平均值