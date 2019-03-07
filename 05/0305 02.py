# 内置函数

'''
dir 查看变量拥有的方法
callable 查看是否是函数
help 查看帮助
'''

# print(dir(int))  #  ['__abs__', '__add__', ……
# print(callable(print))  # True
# print(help(int))

# 打印进度条  可用progress Bar插件做
# import time
# for i in range(0, 101, 2):
#     time.sleep(0.1)
#     per_str = '\r%s%%:%s' % (i, '*' * i)
#     print(per_str, end='', flush=True)
