'''
面向对象的特征： 继承 多态 封装
'''

# 继承
'''
一个类可被多个类继承
一个类可以继承多个父类  python独有
'''
class A: pass  #父类 基类 超类
class B: pass  #父类 基类 超类
class A_son(A): pass  # 子类 派生类
class AB_son(A,B): pass  # 子类 派生类

# __bases__ 查看继承的谁
# print(A.__bases__)  # (<class 'object'>,)
# print(A_son.__bases__)  # (<class '__main__.A'>,)
# print(AB_son.__bases__)  # (<class '__main__.A'>, <class '__main__.B'>)

# 实现
# class Person:
#     def __init__(self,name, sex, tel):
#         self.name = name
#         self.sex = sex
#         self.tel = tel
#
# class Man(Person): pass
# class Woman(Person): pass
#
# Mrli = Man('li', '男', 123456)
# print(Mrli.name)  # li

# 单继承 和 派生
'''
父类中没有的属性 子类中出现 叫派生属性
父类中没有的方法 子类中出现 叫派生方法
父类和子类都有 调用子类的  想调父类的要指出父类名称调用
'''
'''
super函数  找父类
python新式类中有  python3所有类都是新式类
'''
# class Person:
#     def __init__(self,name, sex, tel):
#         self.name = name
#         self.sex = sex
#         self.tel = tel
#
# class Man(Person):
#     def __init__(self, name, sex, tel, high):
#         #Person.__init__(self, name, sex, tel) #  调用父类变量
#         super().__init__(name, sex, tel)  # 可以用super方法代替上面的方法  可以省略父类名和self
#         self.hight = high      # 派生属性
# class Woman(Person): pass
#
# Mrli = Man('li', '男', 123456,175)
# print(Mrli.hight)  # 175


# 多继承   逐级找函数
