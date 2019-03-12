# staticmathod 静态方法
# classmethod 类方法

# classmethod 涉及静态变量的时候使用
'''
默认参数 cls 代表这个类
'''

# class Power:
#     __n = 3
#     def __init__(self,num):
#         self.__num = num
#
#     @property
#     def count(self):
#         return self.__num**Power.__n
#
#     @classmethod
#     def changeN(cls, newN):
#         cls.__n = newN
#
#
#
# num1 = Power(2)
# print(num1.count) # 计算3次方  8
#
# # 修改内部__n 计算4次方
# Power.changeN(4)
# print(num1.count)# 计算4次方  16


# staticmathod 静态方法
'''
函数与类中的其他东西无任何关系可以用staticmathod 将函数变成一个静态方法
'''

class Power:
    def __init__(self, name):
        self.name = name


    @staticmethod
    def inPut():
        name = input('输人名：')
        Power(name)

Power.inPut()