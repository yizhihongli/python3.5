# 内置函数

# reverse() 和 reversed()函数
'''
reverse() 翻转输出
 reversed() 不改变原来列表顺序，返回是反序迭代器
'''
# list1 = [1, 2, 34, 6666]
# list1.reverse()
# print(list1)  # 翻转输出  [6666, 34, 2, 1]
#
# list2 = [1, 2, 34, 6666]
# list3= reversed(list2)
# print(list3)  # 翻转输出  <list_reverseiterator object at 0x00000176F2919588>
#
# for i in list3:
#     print(i)   # 输出 6666 34 2 1

'''
all() 函数 判断可迭代的数据类型中的数据是否含有bool为假的数据
any() 函数 判断可迭代的数据类型中的数据是否含有bool为真的数据
'''
# print(all([1, 333]))   # True
# print(all([1, 333, '']))  # False
# print(all((1, 2, 0)))  # False
#
# print(any([1, 333]))   # True
# print(any((0, 0, 22)))  # True
# print(any((0, 0, 0)))  # False
# print(any(('', '', '')))  # False

# zip 函数 将可操作的数据类型以拉链形式 取纵向数据，排在一起
# list1 = [1, 'c', 0, 4]
# set1 = ('a', 'b', 9, [1, 'd'])
# dic1 = {'k1': 22, 'k2': 'ddddd', 'k3': {'k1': 0, 'k2': 'vvv'}, 'k4': 'ffff', 'k6': 22, }
# for i in zip(list1, set1, dic1):
#     print(i)
'''
(1, 'a', 'k1')
('c', 'b', 'k2')
(0, 9, 'k3')
(4, [1, 'd'], 'k4')
'''

'''
filter函数 和 map函数
filter： 将可迭代是数据作为参数传递给函数  返回迭代器 迭代器中是使函数返回True的参数的值
map：  迭代器中是使函数返回的结果
'''

# filter和map 例1
# def is_odd(x):
#     return x % 2 == 1   # 若为偶数，不等于1 返回0   为奇数返回1
#
# # ret = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# # for i in ret:
# #     print(i)  # 1 3 5 7 9
#
# ret2 = map(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# for i in ret2:
#     print(i)  #  True False True False True False True False True

# filter和map 例2
# def test(x):
#     if x % 2 == 1:
#         return x
#     else:
#         return '偶数'
#
# ret = filter(test, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# for i in ret:
#     print(i)  # 均为true   输出 1, 2, 3, 4, 5, 6, 7, 8, 9
#
# ret2 = map(test, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# for i in ret2:
#     print(i)  # 1 偶数 3 偶数 5 偶数 7 偶数  9

'''
sort函数 和 sorted函数
sort 在原列表排序 改变原来序列
sorted  不改变原来顺序 直接返回排序的序列  注：不是返回迭代器
'''

list1 = [1, 4, 9, -4, 8]
list1.sort(key=abs)  # 可传参  按照绝对值排序
print(list1)  # [1, 4, -4, 8, 9]

list2 = [1, 4, 9, -4, 8]
print(sorted(list2, reverse = True))  # [9, 8, 4, 1, -4] 直接返回排序的序列
print(list2)  # [1, 4, 9, -4, 8]  不改变原来顺序






