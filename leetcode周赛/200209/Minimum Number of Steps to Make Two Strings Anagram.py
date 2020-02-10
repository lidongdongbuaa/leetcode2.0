#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 12:21
# @Author  : LI Dongdong
# @FileName: Minimum Number of Steps to Make Two Strings Anagram.py
''''''
'''
题目分析
1.要求：
    Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.
    Return the minimum number of steps to make t an anagram of s.
    An Anagram of a string is a string that contains the same characters with a different (or the same) ordering
    Input: s = "bab", t = "aba"
    Output: 1
    Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
2.理解：change less t elem to make t as s in words and its times
3.类型：dic
4.确认输入输出及边界条件：
    input： string， 1 <= s.length <= 50000, s.length = t.length, repeated word? Y order？ N. all word is low-case
    output: int
    corner case: only one word？ Y
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：brute force - dic record
方法：
    1. use dic to record word as key and its times in t and s tO(N) sO(N)
    2. calculate t diff times res of word with s tO(N**2) sO(1)
    3. return res
time complex: tO(N**2)
space complex: sO(N)
易错点：
'''
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if len(s) == len(t) == 1:  # corner case
            if s == t:
                return 0
            else:
                return 1

        dicS = self.transferDic(s)  # transfer as dic
        dicT = self.transferDic(t)  # transfer as dic

        res = 0
        for key, times in dicT.items():  # calculate diff
            if key in dicS:
                if times > dicS[key]:
                    res += times - dicS[key]
            else:
                res += times
        return res

    def transferDic(self, string):  # transfer string as dic
        if not string:  # corner case
            return {}

        dic = {}
        for elem in string:  # calculate times
            if elem in dic:
                dic[elem] += 1
            else:
                dic[elem] = 1
        return dic

x = Solution()
print(x.minSteps("anagram",  "mangaar"))




