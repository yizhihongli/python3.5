# 函数动态参数 *args  **kwargs

# * 可动态接收参数个数， 组成元组，但不能接收按照关键字传参
def addNum1(*args):
    num = 0
    for i in args:
        num += i;
    return num

print(addNum1(2, 4))
print(addNum1(2, 4, 6))

# ** 可动态接收按照关键字传参，  组成字典
def addNum2(**kwargs):
    return kwargs

print(addNum2(a=2, b=4))  # {'b': 4, 'a': 2}
print(addNum2(a=2, b=4, c=6))  # {'b': 4, 'c': 6, 'a': 2}


# 传元组或字典

def addNum3(*L):
    return L

set1 = [1, 3, 'ss']
print(addNum3(*set1))  # (1, 3, 'ss')

def addNum3(**L):
    return L

set1 = { 'a' : 1, 'b ': 3, 'c' : 'ss'}
print(addNum3(**set1))  # {'b ': 3, 'c': 'ss', 'a': 1}