str1 = 'df233y4kv;yRB*v'
str2 = str1.capitalize()    # 首字母大写
str3 = str1.upper()     # 全部大写
str4 = str3.lower()     # 全部小写
str5 = str1.swapcase()      # 大小写翻转
str6 = str1.title()     # 用特殊字符或数字隔开的单词首字母大写,其他字母全部小写
str7 = str1.center(77,'#')       # 居中 参数两个(长度，填充符号)  若长度小于字符长度，则全部显示，若大于则用填充符号填充，默认为空格

length1 = len('哈哈哈')        # 长度
b1 = str1.startswith('fl334kv;yRB*v', 1, 100)       # 判     断开头字符返回boll类型 ,可加参数，表示截取字符串的长度
b2 = str1.find('B')     # 返回元素位置，元素不存在返回 -1
b3 = str1.index('2')    # 返回元素位置，元素不存在报错

# strp rsrtp lstrp  前后删，前删，后删 函数
de1 = '    %&*skdjfhsdkj     sdjfhsdjh&^#         '
de2 = de1.strip()       # 默认删除前后空格
de3 = de1.lstrip('%#*^ ')    # 可加参数，循环删除前后的所有字符

num1 = str1.count('33')      # 统计字符个数
list1 = str1.split('y')     # 以y分割字符串，保存到list里面  其中y不存在了

# format函数
str8 = '哈哈哈{}呵呵呵{}哼哼哼{}嘿嘿嘿{}'.format('ha', 'he', 222, 'heihei')         # 按照顺序替换
str9 = '哈哈哈{0}呵呵呵{2}哼哼哼{2}嘿嘿嘿{2}'.format('ha', 'he', 222)         # 多次替换
str10 = '哈哈哈{ha}呵呵呵{he}哼哼哼{heng}嘿嘿嘿{hei}'.format(ha='ha', he='he', heng=222, hei='heihei')         # 键值替换

str11 = str1.replace('y', '这是y', 1)        # 替换，可加参数表示替换的个数 默认全替换

# 判断字符串组成
str12 = '3wsd'
b4 = str12.isalnum()        # 字母+数字组成
b5 = str12.isalpha()        # 字母组成
b6 = str12.isdigit()        # 数字组成

#取字符串str1 = 'df233y4kv;yRB*v'
str13 = str1[0:2]       # 取头不取尾
str14 = str1[-2]        # 取倒数第二个
str14 = str1[0:-2]        # 取倒数第二个之前的
str15 = str1[0:6:2]        # 在0到6之间，每隔2个取一个
str16 = str1[6:0:-2]        # 在6到0之间，每隔2个取一个


# 列表
# 增
list2 = ['asda', 23, [1, '333', 'sss']]
list3 = list2[2][2]
list2.append('dd')      # 添加
list2.insert(1, 'eee')      # 在1的位置前面插入eee
list2.extend('abc')      # 在后面插入a,b,c 单个元素
list2.extend([12, 'sdf',[1,3,4,['222',33]]])      # 在后面插入列表中元素，元素中的列表不再分割

# 删
list2 = ['asda', 23, [1, '333', 'sss'], 3334, 3434, 3434]
list2.pop()     # 默认删除最后一个
list2.pop(0)     # 删除第一个
#list2.clear()       # 清空
# del list2       # 删除列表
del list2[4:]       # 切片删除

# 改
list2 = ['asda', 23, [1, '333', 'sss'], 3334, 3434, 3434]
list2[1] = 'jkhkjhkj'
list2[1:4] = 'sdkjfh'       # 切片改   分割单个元素插入
list2[1:4] = [1, 2, 'sdkjfbh']       # 切片改  list单个元素插入


# 排序
list2 = [12, 4, 5656, 6767, 5, 677, 55, 4]
list2.sort()  # 正向排序
list2.sort(reverse=True)        # 倒序排序

list2 = [12, 4, 5656, 6767, 5, 677, 55, 4]
list2.reverse()     # 翻转


# join函数  返回结果为字符串 可用字符分割字符序列，不能分割整形
str1 = 'sldkjflijh'
str2 = '++'.join(str1)      # 将str1中每个元素用++隔开
list1 = ['ddd', '23', 'ddd', '34']      # 不能包含int
str2 = '+++'.join(list1)        # ddd+++23+++ddd+++34


# 字典
dic1 = {
    'name': 'aaa',
    'age': 16,
    'sex': 'nam'
}

# 增加键和键值  只有键不存在时才会增加，若键存在，不管键值是否为none，均不修改！
dic1.setdefault('tel', 123456)      # 函数返回键值  字典修改为{'sex': 'nam', 'age': 16, 'tel': 123456, 'name': 'aaa'}

# 删除 键不存在报错，防止报错可加参数，加上参数存不存在键值均返回参数，不加参数返回键值
dic1.pop('age', '不存在')     # 函数返回键值 16
dic1.popitem()      # 随机删除一个键   函数返回删除的键和键值的元组形式 例如('name', 'aaa')

#修改 update 本来存在的修改或保留，不存在的添加
dic1 = {
    'name': 'aaa',
    'age': 16,
    'sex': 'nam'
}
dic2 = {
    'name': 'bbb',
    'sex': 'woman',
    'emali': '123@qq.com'
}
dic1.update(dic2)       # dic1 {'age': 16, 'sex': 'woman', 'name': 'bbb', 'emali': '123@qq.com'}

#查  1.直接取键名的键值 没有回报错  2.get方法，设置默认参数，没有返回默认参数
value = dic1['name']
value = dic1.get('name1', '没有')

# 循环
# 单个返回
for key in dic1:
    print(key)
    print(dic1[key])

# 返回元组类型
for item in dic1.items():
    print(item)
'''
('name', 'bbb')
('emali', '123@qq.com')
('age', 16)
('sex', 'woman')
'''

# 返回str类型
for key, value in dic1.items():
    print(key, value)
'''
name bbb
age 16
sex woman
emali 123@qq.com
'''





























