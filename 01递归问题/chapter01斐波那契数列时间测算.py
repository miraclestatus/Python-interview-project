# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 14:47
# @Author  : Eric Lee
# @Email   : li.yan_li@neusoft.com
# @File    : chapter01斐波那契数列.py
# @Software: PyCharm
# total = 0 #记录函数执行的次数
from collections import defaultdict
total = defaultdict(int)
# 1, 1, 2, 3, 5, 8, 13, 21, 34
def fibo(k):
    """
    使用递归求斐波那契数列指定位置的值
    :param k:代表位置序号
    :return:
    """
    assert k > 0, "K的值必须大于0"
    if k in [1, 2]:
        return 1
    global total
    total[k] += 1
    # 根据数列的规律我们知道res结果是
    # 这个位置的前一个元素
    # 加上这个位置的再往前的一个元素
    before1 = fibo(k-1)
    before2 = fibo(k-2)
    res = before1 + before2

    return res
# 1, 1, 2, 3, 5, 8, 13, 21, 34
def fibo2(k):
    """
    使用循环求斐波那契数列指定位置的值
    :param k:
    :return:
    """
    assert k > 0, "K的值必须大于0"
    if k in [1, 2]:
        return 1
    before1, before2 = 1, 1
    # 循环的目的是每次更改 before1, before2
    for i in range(3, k+1):
        tmp = before1
        res = before1 + before2
        before1 = res
        before2 = tmp

    return res
if __name__ == '__main__':
    # print(fibo(3)) # 2
    # print(fibo(7)) # 13
    # print(fibo2(7))
    from datetime import datetime
    start_time = datetime.now()
    fibo(34)
    print("递归耗时{}".format((datetime.now()-start_time).total_seconds()))
    print(total)  # 我们可以看到 fibo()函数执行的时间也是一个斐波那契数列
