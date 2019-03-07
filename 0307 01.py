# 常用模块
'''
re  正则表达式
collection 扩展数据类型
time   时间模块
random  随机数模块
os  操作系统
sys python解释器沟通
序列化 数据类型和str转换
'''

# collection
# from collections import namedtuple
# Point = namedtuple('point', ['x', 'y'])  # 声明 可命名元组
# p = Point(3, 6)
# print(p, p.x, p.y)  # point(x=3, y=6) 3 6
# import sys
# print(sys.platform)  # win32


# JSON
# dumps 序列化   loads 反序列化
import json
# dic1 = {'k1': 'tt'}
# str1 = json.dumps(dic1)
# print(str1)  # 转字符串  {"k1": "tt"}
#
# dic2 = json.loads(str1)
# print(type(dic2), dic2)  # 转字典 <class 'dict'> {'k1': 'tt'}


# dump load  文件读写
# dic1 = {'k1': 'tt', 'k2': 'tttt'}
# f = open('0307.txt', 'r+', encoding='utf-8')
# json.dump(dic1, f)
# f.close()

f = open('0307.txt')
res = json.load(f)
print(type(res), res)  # <class 'dict'> {'k1': 'tt', 'k2': 'tttt'}
f.close()














