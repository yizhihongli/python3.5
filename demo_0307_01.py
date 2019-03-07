

# print('hhhh')  # 若其他文件引用本文件，会执行此句话

# print(__name__)  # 其他页面执行会输出 demo_0307_01   在本页面执行会输出 __main__

if __name__ == '__main__':  # 只在本页面执行时输出
    print('hhhh')

