# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 8:48
# @Author  : Eric Lee
# @Email   : li.yan_li@neusoft.com
# @File    : chapter02二分查找实现.py
# @Software: PyCharm
# 二分查找（折半查找）适合有序的数组进行查找
from random import randint, choice

data = [randint(1, 100) for _ in range(10)]
# 随机选择其中一个元素
target = choice(data)
data.sort()
print(data, "目标查找对象", target)


def bin_search_normal(data_list, target):
    """
    二分查找非递归实现
    :param data_list: 查找的目标数组
    :param target: 目标值
    :return: 如果找到返回索引位置，没找到返回-1
    """
    left = 0
    right = len(data_list) - 1
    target_pos = -1
    # 此处 循环条件时 left <= right 而不是 True的原因是
    # 比如目标数字是负数，那么执行倒数第一次的循环是 left 和 right都等于 0 那么mid也等于 0
    # 继续执行会进入 else 语句块, 此时right变成 -1 ， left（0） <= right（-1） 不成立，跳出循环
    while left <= right:
        mid = int((left + right) / 2)
        if data_list[mid] == target:
            print("数据在{}位置被找到".format(mid))
            target_pos = mid
            break
        elif data_list[mid] < target:
            # 中间值小于目标值， 在中间值右侧二分查找
            left = mid + 1
            print("中间值小于目标值， 在中间值右侧二分查找")
        else:
            # 中间值大于目标值， 在中间值左侧二分查找
            right = mid - 1
            print("中间值大于目标值， 在中间值左侧二分查找")
    return target_pos


def bin_search_by_recursion(left, right, data_list, target):
    """
    二分查找递归实现
    :return:所在位置
    """
    mid = int((left + right) / 2)
    if data_list[mid] == target:
        return mid
    elif data_list[mid] < target:
        return bin_search_by_recursion(mid + 1, right, data_list, target)
    else:
        return bin_search_by_recursion(left, mid - 1, data_list, target)


res1 = bin_search_normal(data, -99)
res2 = bin_search_by_recursion(0, len(data)-1, data, target)

print('*'*100)
print(res1)
print(res2)