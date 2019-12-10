#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 18:57
# @Author  : LI Dongdong
# @FileName: 455. Assign Cookies.py
''''''
'''

1.要求：Assume you are an awesome parent and want to give your children some cookies. 
    But, you should give each child at most one cookie. 
    Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with;  
    and each cookie j has a size sj. 
    If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. 
    Your goal is to maximize the number of your content children and output the maximum number.
2.理解：
3.类型：Greedy algrithm
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.edge case: 
    input:
    output:
    class name:
    focus on time or space?
'''

'''
idea：
Method：
time complex: O(N2)
space complex: 
易错点：begin_numb = j + 1, begin 要从下一位做起
'''

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        if g == [] or s == []:
            return 0

        g.sort()
        s.sort()

        numb = 0
        begin_numb = 0
        for i in range(len(g)):
            for j in range(begin_numb, len(s)):
                if s[j] >= g[i]:
                    numb += 1
                    begin_numb = j + 1
                    break
                else:
                    pass
        return numb





