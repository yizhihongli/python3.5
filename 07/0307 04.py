# 异常处理  try

# try 和 except
# int('aaaa') # 输出 ValueError: invalid literal for int() with base 10: 'aaaa'
# try:
#     int('aaaa')
# except ValueError: # 对应错误类型
#     print('非int类型')

# try 和 except Exception
# try:
#     int('aaaa')
#     [][4]
# except Exception: # 万能错误
#     print('代码有误')
# else:
#     print('没有异常的时候输出此句话')


# try 和 finally
# def fun1():
#     try:
#         f = open('0307.txt', 'w')
#         return True
#     except Exception: # 万能错误获取
#         return False
#     else:
#         print('没有异常的时候输出此句话')
#     finally:
#         print('return 以后还会调用finally的代码')
#         f.close()
#
# print(fun1())
'''
return以后不会执行else代码   但会执行finally代码
'''


# 获取错误信息
def fun1():
    try:
        int('aa')
        return 1
    except Exception as error:  # 万能错误 并获取错误信息
        print(error)

print(fun1())

