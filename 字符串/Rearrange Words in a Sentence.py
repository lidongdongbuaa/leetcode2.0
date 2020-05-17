#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 12:09
# @Author  : LI Dongdong
# @FileName: Rearrange Words in a Sentence.py
''''''
'''
题目概述：
题目考点：字符串的拆，并，排序，大写
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: string; length range is from 1 to 10^5; value range is letter and space; have repeated; no order
output: string
corner case
    length of text is 1, return text

Method: list save and order and join
Steps:
    1. split the text into list by space
    2. order the list by length
    3. reorginze the list to string
    4. turn the first letter to uppercase
    5. return

Time complexity: O(n), n is length of text
Space complexity: O(n)
'''


class Solution:
    def arrangeWords(self, text: str) -> str:
        if len(text) == 1:
            return text

        sList = text.split(' ')
        sList.sort(key=lambda x: len(x))
        res = ' '.join(sList)
        res = res.capitalize()
        return res
