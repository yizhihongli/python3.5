# # 反射
# # 用字符串的方式获取方法和属性
# class People:
#     dic = {'name':'Mr.li', 'sex':'男'}
#     def show_name(self):
#         print('姓名')
#
#     def show_sex(self):
#         print('性别')
#
#     @classmethod
#     def fun1(cls):
#         print('hhhhhhhh')
#
# # 直接获取
# # test = People.dic
# # for i in test:
# #     print(i)
#
# # 反射
# '''
# 三个函数：hasatter getattr delattr
# '''
# # 调用属性
# test1 = getattr(People, 'dic')
# print(test1)  # {'name': 'Mr.li', 'sex': '男'}
#
# # 调用方法
# test2 = getattr(People, 'fun1')
# test2()  # hhhhhhhh
#
# # 应用
# test3 = People()
# for i in People.dic:
#     print(i)
# key = input('输入键名：')
# if hasattr(test3, People.dic[key]):
#     func = getattr(test3, People.dic[key])
#     func()
#
# '''
# 通过反射k可获取
#  通过对象名：获取对象属性和普通方法
#  通过类名：  获取静态属性和类方法和静态方法
#
#  普通方法： self
#  静态方法： @staticmethod
#  类方法：   @classmethod
#  属性方法   @property
#
# '''


# '''
# 内置函数 isinstance和issubclass
#
# isinstance(obj, cls) : 检测obj是否是cls对象
#
# issubclass(sub, super) : 检查sub是否是super类的派生类
#
#
# '''
#
# # isinstance(a, A) 判断对象a是否是A的对象
# # issubclass(B, A) 判断B是否是A的子类
# class A:
#     pass
# class B(A):
#     pass
# a = A()
# print(isinstance(a, A))  # True
# print(issubclass(B, A))  # True


# 反射进阶
'''
 用字符串方式去操作变量
 1.反射类的函数和变量名
 2.反射自己模块函数和变量名
 3.反射模块的函数和变量名

四个函数 前两个常用
 hasatter 是否存在变量
 getattr  获取变量
 delattr  删除一个变量
 setattr 设置修改变量
'''

# 反射自己模块函数和变量名
import sys

def fun1():
    print('fun1')
n = 10

print(getattr(sys.modules['__main__'], 'n'))  # 10

getattr(sys.modules[__name__], 'fun1')()  # fun1  可改成变量__name__  为了取导入模块的方法和变量


















