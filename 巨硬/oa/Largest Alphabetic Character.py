#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 17:13
# @Author  : LI Dongdong
# @FileName: Largest Alphabetic Character.py
''''''
'''
Given a string S, find the largest alphabetic character, whose both uppercase and lowercase appear in S. 
The uppercase character should be returned. For example, for S = "admeDCAB", return "D". If there is no such character, return "NO".
题目概述：在S中存在字母x，其大小写形式都在S中，返回最大的x，如果没有这样的大小写都在S中的字符，返回NO
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考

Method:
    1. sorted the string - > ['A', 'B', 'C', 'D', 'a', 'd', 'e', 'm']
    2. traversal the upper character i
        if i's lower in string, res = i
        renew the i
    3.return i
'''
class String:
    def findLargest(self, s):  # return upper char whose has lower char in s
        new = sorted(s)
        ans = ''
        for elem in new:
            if elem.isupper():
                lower = elem.lower()
                if lower in new:
                    ans = elem
        if ans != '':
            return ans
        else:
            return 'NO'

X = String()
print(X.findLargest("admeDCAB"))