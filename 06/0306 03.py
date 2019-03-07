# re模块和正则表达式
'''
正则表达式： 字符串匹配
'''

import re

# search函数
'''
从前往后匹配  返回结果要用group才能显示结果
如果不存在，直接调用group会报错
'''
# ret = re.search('aab','sjdfhksjdghfaadlghlsdkfjaa')
# if ret:
#     print(ret.group())

# match函数
'''
从第一个往后匹配  返回结果要用group才能显示结果
如果不存在，直接调用group，同样会报错
'''
# ret = re.match('aab','aabsjdfhksjdghfaabdlghlsdkfjaa')
# if ret:
#     print(ret.group())


# split函数
'''
根据正则分割
'''
# 先按a分割  再按b重新分割
# ret = re.split('[ab]','sdbsdadcdbavvb') # ['sd', 'sd', 'dcd', '', 'vv', '']
# print(ret)

# sub 替换
# 数字替换为H  加参数表示替换几次
ret = re.sub('\d', 'H','asdfh454dlkjfgdkjh9009dkljfgn',3 )
print(ret)  # asdfhHHHdlkjfgdkjh9009dkljfgn

# subn 替换
# 数字替换为H  返回结果和次数 也可加参数
ret = re.subn('\d', 'H','asdfh454dlkjfgdkjh9009dkljfgn')
print(ret)  # ('asdfhHHHdlkjfgdkjhHHHHdkljfgn', 7)


