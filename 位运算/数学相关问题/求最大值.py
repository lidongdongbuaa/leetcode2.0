#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 20:31
# @Author  : LI Dongdong
# @FileName: 求最大值.py
''''''
'''
题目概述：
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
import sys


def calculateRes(input):

    res = 0
    return res

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        # for v in values:
        x = values[0]
        res = calculateRes(input)
        print("%s\n"%res)



