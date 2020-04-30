#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 20:50
# @Author  : LI Dongdong
# @FileName: Crop Words.py
''''''
'''
题目概述：按照要求，缩减字符串长度到k以内个，不能最后留空格，不能在一段单词中间
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考

corner case:
    1. s is None or '' -> ''
    2. k =0 -> ''
    4. k >= len(s)

Method: 
    1. corner case
    2. check i, i + 1, i -1...
        if i is blank
            while not arr[i] isalpha()
                i = i - 1
            return s[:i + 1]
        if i is alpha()
            if s[i + 1] = ''
                return s[: i + 1]
            else:
                while not arr[i] isalpha()
                    i = i - 1
                return s[:i]
'''
class String:
    def longString(self, s, k):
        if s is None or s == '':
            return ''
        if k == 0:
            return ''
        if k > len(s):
            return s

        if s[k-1] == '':
            while not s[k-1].isalpha():
                k = k - 1
            return s[:k ]
        else:
            if s[k] == '':
                return s[:k]
            else:
                while s[k-1].isalpha():
                    k = k -1
                return s[:k-1]
x = String()
print(x.longString('Codility me test coders', 14))

