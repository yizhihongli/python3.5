# 函数进阶  命名空间和作用域
'''
内置命名空间：
          python启动时可以使用的名字存储在内置的命名空间 例如print()函数

全局命名空间：
          程序重上到下执行时加载到内存的  自己设置的变量或函数
局部命名空间：
          函数调用时加载的

在局部可设置 global 将局部变为全局的
'''
# a = 1  # 全局命名空间
#
# def fun():
#     a = 2  # 局部命名空间
#
#
#
#
# '''
# nonlocal 应用于嵌套函数内作用域中的一个名称
# 在声明nonlocal名称的时候，它必须存在于该嵌套函数的作用域中，
# 并且不能由def中的第一次赋值创建。
# '''
# def make_counter():
#     count = 0
#     print('第一个：%d'%(count))
#     def counter():
#         nonlocal count
#         count += 1
#         print('第二个：%d'%(count))
#         return count
#     return counter


'''
结果：
第一个：0
第二个：1
1
第二个：2
2
第二个：3
3


不是均为1
执行顺序为:
1.执行 mc = make_counter() 此时 输出 print('第一个：%d'%(count))
  此时 mc =
2.执行 print(mc()) 相当于执行 print(counter()) 这就是为什么返回counter ，而且print时mc要加括号
3.print(mc()) 直接执行make_counter()函数中的counter()函数，这就是为什么 ‘第一个：0’只执行一次
4.nonlocal count 相当于在 去掉make_counter()函数，把count作为一个全局变量放入了counter()函数，即逐个累加

'''
# mc = make_counter()
# print(mc())  # 1
# print(mc())  # 2
# print(mc())  # 3


'''
函数名：
     1.可以赋值
     2.可以作为容器类型的元素
     3.可以作为函数的返回值
     4.可以作为函数的参数
'''

# # 可以赋值
# def fun1():
#     return 1111
#
# fun2 = fun1
# print(fun2())
#
# # 可以作为容器类型的元素
# def fun3():
#     return 3333
#
# def fun4():
#     return 44444
#
# list1 = [fun3, fun4]
# for i in list1:
#     print(i())
#
#
# # 可以作为函数返回值和参数
# def fun5():
#     return 5555
#
# def fun6(f):
#     f()
#     return f
#
# fun7 = fun6(fun5)
# print(fun7())

#
# # 闭包 嵌套的函数，且内部函数调用了外部函数的变量
#
# def fun8():
#     a = 1
#     def fun81():
#         print(a)
#     return fun81
#
# fun9 = fun8()
# fun9()
#

# 获取网页代码
from urllib.request import urlopen
ret = urlopen('https://www.hao123.com/index.html').read()
print(ret)






