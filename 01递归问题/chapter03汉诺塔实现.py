# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 13:00
# @Author  : Eric Lee
# @Email   : li.yan_li@neusoft.com
# @File    : chapter03汉诺塔实现.py
# @Software: PyCharm
# 让谁来搬




# index 老几
# A B  C
# start, mid, end  从哪个柱子开始， 经过哪个柱子， 哪个柱子结束
def move(index, start, mid, end):
    if index == 1:
        print("{}-->{}".format(start, end))
        return 1
    else:
        move(index-1, start, end, mid)
        print("{}-->{}".format(start, end))
        move(index-1, mid, start, end)
move(5, "A", "B", "C")