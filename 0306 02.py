# 匿名函数
'''
关键字 lambda
不换行
'''

fun1 = lambda x: x**3
fun2 = lambda: 3
print(fun1(3))  # 27
print(fun2())  # 3

# 与内置函数合用 常用的：max min sorted fillter map
# 求字典中 key值最大是key
dic = {'k1': 100, 'k2': 300, 'k3': 50}
print(max(dic))  # k3  直接取为key名
print(max(dic, key=lambda k: dic[k]))  # 匿名函数



