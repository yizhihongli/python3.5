# 类
# 类可以定义两种属性：静态和动态
class Person:
    def __init__(self, *args): #调用类时 自动调用此函数
        self.name = args[0]
        self.sex = args[1]
        self.qq = args[2]

alex = Person('哈哈哈', 'man', '123456')
print(alex.name)

'''
过程
  1. 对象 = 类名()  创建一个对象，并创建self变量
  2. 调用__init__函数，并接收参数
  3.返回self  不用return 自动返回
'''


'''
组合： 一个对象的属性是另一个类的对象
'''

