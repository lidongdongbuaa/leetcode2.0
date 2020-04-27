#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 22:21
# @Author  : LI Dongdong
# @FileName: 402. Remove K Digits.py
''''''
'''
题目概述：求去除k个元素后，最小的数
题目考点：stack保存值，贪心去除目前的元素，让当前值最小
解决方案：stack保存遍历的数，elem比较stack[-1]
方法及方法分析：
time complexity order: O(n)
space complexity order: O(n)
如何考
'''
'''
input:  nums, string; length range is from 0 to 10002; value range, no leading zero; have repeated value; no order
    k, is int, value < = length of nums
output:
    string, the smallest value
corner case:
    nums is None, return None

超时
A. greedy - get k times smallest number
    Method:
        run k times
            find the min value of delete one elem from nums
                delete the last value of increasing part
            use the min value to renew the nums
    num = "1432219" k = 3

    k = 1, num = 132219
    k = 2, num = 12219
    k = 3, num = 1219
    Time complexity ：O(n^2) in worst case, the number elem is increasing
    Space: O(1)
'''


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:  # corner case
            return ''

        def delete(num):  # delete one elem to make num minimal
            time = 1
            res = [num[0]]
            for elem in num[1:]:
                if int(res[-1]) > int(elem):
                    if time == 1:
                        res.pop()
                        res.append(elem)
                        time -= 1
                    else:
                        res.append(elem)
                else:
                    res.append(elem)
            if time == 1:
                res.pop()
            return ''.join(res)

        for _ in range(k):
            num = delete(num)
        return str(int(num)) if num else '0'


'''
B. greedy + stack
    Method:
        use list res to save num[0], times = 1
        traversal elem in num[1:]
            while last res' elem > elem 
                if times <= k, res pop the last elem and add the elem, times += 1
                else:
                    res.append(elem)
            else
                res append elem
        while times:
            res.pop()
        transfer res to string
        if res = '', return '0', else, return  str(int(res))
    Time complexity: O(n)
    Space:O(n)
易错点：
    在找到转折点时，要继续往前pop k个比elem大的数
    结果是’’时，补充为‘0’
'''


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:  # corner case
            return '0'

        res = [num[0]]
        for elem in num[1:]:
            while res and res[-1] > elem and k > 0:
                res.pop()
                k -= 1
            res.append(elem)

        while k:
            res.pop()
            k -= 1

        res = ''.join(res)
        return str(int(res)) if res else '0'
