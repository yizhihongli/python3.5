# 封装和@property


# 私有属性的用法
'''
1. 隐藏属性  不被外部调用
2. 保护属性不被修改
3. 保护属性不被子类调用
'''

# class Car:
#     def __init__(self, speed, oil, time):
#         self.__speed = speed  # 私有
#         self.__oil = oil  # 私有
#         self.time = time
#     def length(self):
#         return self.__oil*self.__speed
#
# myCar = Car(20, 300, 300)
# print(myCar.length())  # 600
# # print(myCar.__speed)  # 私有的不能直接调用  报错
# print(myCar.time)  # 300


# 内置装饰器函数 @property
'''
1.将函数伪装成属性 调用时去掉小括号
2.不能传参
'''

#@property
# class Car:
#     def __init__(self, speed, oil, time):
#         self.__speed = speed  # 私有
#         self.__oil = oil  # 私有
#         self.time = time
#
#     @property
#     def length(self):
#         return self.__oil*self.__speed
#
# myCar = Car(20, 300, 300)
# print(myCar.length)  # 600



# @property 和 xxx.setter  对私有属性的修改
'''
1. 先有@property 才有xxx.setter
2.xxx 三名统一
3.xxx.setter下面的函数必须传一个且仅有一个参数
4.调用xxx.setter下面的函数用等号传递参数
'''

# class Car:
#     def __init__(self, speed, oil):
#         self.__speed = speed  # 私有
#         self.__oil = oil  # 私有
#
#     @property
#     def length(self):
#         return self.__oil*self.__speed
#
#     @length.setter
#     def length(self, new_speed):  #  修改__speed
#         self.__speed = new_speed
#
# myCar = Car(20, 300)
# print(myCar.length)  # 600
# myCar.length = 1
# print(myCar.length)  # 300



# @property 和 xxx.deleter  对私有属性的删除
'''
1. 先有@property 才有xxx.deleter
2.xxx 三名统一
3.del myCar.length  方法不能直接被删除，del时会自动调用class中的xxx.deleter下面的函数
4.xxx.deleter下面的函数中的功能，可以随意写，不仅仅是删除，而是调用这个函数，具体函数功能可以随意写
'''

class Car:
    def __init__(self, speed, oil):
        self.__speed = speed  # 私有
        self.__oil = oil  # 私有

    @property
    def length(self):
        return self.__oil*self.__speed

    @length.deleter
    def length(self):
        print('删除speed属性')
        del self.__speed

myCar = Car(20, 300)
print(myCar.length)  # 600
del myCar.length
print(myCar.length)




