# 集合 无序
set1 = {1, 'aaa', '哈哈哈'}

# 增
set1.add('呵呵呵')     # {1, '呵呵呵', 'aaa', '哈哈哈'}
set1.update('嘿呵哼嘿呵哼')       # {'哈哈哈', 1, '哼', '呵', '呵呵呵', 'aaa', '嘿'} 重复不增加
set1.update(['嘿呵哼嘿呵哼', '嘿呵哼嘿呵哼'])       #{1, '哈哈哈', '呵', '嘿呵哼嘿呵哼', '呵呵呵', 'aaa', '嘿', '哼'}

# 删除
set1.remove('aaa')  # 删除一个元素
set1.pop()  # 随机删除一个元素
set1.clear()  # 清空集合 输出set()
del set1  # 删除集合

# 集合运算
set1 = {'a', 'b', 'c', 'dddd', 111, 2121}
set2  = {'a', 'b', 'e', 'ffff', 111, 2121}

# 交集 & 或者 intersection()
set3 = set1 & set2  # {'a', 2121, 'b', 111}
set3 = set1.intersection(set2)

# 并集 | 或者 union()
set3 = set1 | set2  # {'a', 2121, 'dddd', 111, 'e', 'b', 'ffff', 'c'}
set3 = set1.union(set2)

# 差集 - 或者 difference
set3 = set1 - set2  # {'dddd', 'c'}
set3 = set2 - set1  # {'ffff', 'e'}
set3 = set2.difference(set1)

# 反交集。 ^ 或者 symmetric_difference()
set3 = set1 ^ set2  # {'e', 'c', 'dddd', 'ffff'}
set3 = set1.symmetric_difference(set2)

# 子集与超集
set1 = {'a', 'b', 'c', 'dddd', 111, 2121}
set2 = {'a', 'b'}

# 返回均为True  set2是set1的子集
print(set2 < set1)
print(set2.issubset(set1))

# 返回均为True  set1是set2的超集
print(set1 > set2)
print(set1.issuperset(set2))
