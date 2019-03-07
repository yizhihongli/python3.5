'''
对于非文本文件，只能使用b模式，"b"表示以字节的方式操作
r 读  返回字符串
rb 非文字文件

w 写
wb

a 追加

+ 模式（就是增加了一个功能）
r+， 读写【可读，可写】
w+，写读【可写，可读】
a+， 写读【可写，可读】
'''

# 读
# f = open('1.txt', mode='r', encoding='utf8')
# cont = f.read()
# f.close()
# print(cont)

# 写 有文件覆盖重写   无文件创建
# f = open('2.txt', mode='wb',encoding='utf-8')
# f.write('skfjdsdfh')
# f.close()

# 追加
# f = open('1.txt', mode='a', encoding='utf-8')
# f.write('追加的')
# f.close()

# +
# f = open('1.txt', mode='a+', encoding='utf-8')
# f.write('aaa')
# f.seek(0) # 光标移到到开头 不然读不出来
# cont = f.read()
# f.close()
# print(cont)r


# 常见函数
'''
seek() 设置光标位置
tell() 读光标位置
readable() 是否可读
readline() 按行读
readlines() 读多行

'''
#
# f = open('1.txt', mode='r+', encoding='utf-8')
# cont = f.readlines()
#
# f.close()
# print(cont)
#
#
# # with open  打开文件 不用关闭
# with open('1.txt', mode='r+', encoding='utf-8') as f:
#     print(f.read())

print('欢迎注册！')
name = input('请输入用户名：')
password= input('请输入密码：')
with open('1.txt', mode='a+', encoding='utf-8') as f:
    f.writelines(name + '###' + password + '\n')
    print('注册成功！')
print('请登录：')
i = 1
while i < 4:
    name = input('请输入用户名：')
    password= input('请输入密码：')
    with open('1.txt', mode='r+', encoding='utf-8') as f:
        lines = f.readlines()
        dataBool  = 0
        for line in lines:
            if name + '###' + password + '\n' == line:
                dataBool = 1
                break
        if dataBool:
            print('登录成功')
        else:
            print('用户名或密码不正确,还剩%s次机会！' % (3-i))
    i += 1
else:
    print('登录失败！')









