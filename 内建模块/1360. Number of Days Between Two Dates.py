#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 11:36
# @Author  : LI Dongdong
# @FileName: Number of Days Between Two Dates.py
''''''
'''
题目分析
1.要求：Write a program to count the number of days between two dates.

    The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
    
     
    
    Example 1:
    
    Input: date1 = "2019-06-29", date2 = "2019-06-30"
    Output: 1
    
    Example 2:
    Input: date1 = "2020-01-15", date2 = "2019-12-31"
    Output: 15
    Constraints:
    
    The given dates are valid dates between the years 1971 and 2100.
2.理解：find the dif of two date
3.类型：time calculate of python
4.确认输入输出及边界条件：
    input: two string, from 1971 to 2100 year, repeated? Y, order? biggner or smaller? N 1> 2 or 2 > 1
    output: int(dif of dates)
    corner case: None? N Same string? Y 
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
A. python date module
方法：
    transfer string as time format, t1, t2
    find abs(t1 - t2)
time complex: O(1)
space complex: O(1)
易错点：
'''
from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 == date2:  # corner case
            return 0

        d1 = datetime.strptime(date1, '%Y-%m-%d')  # transfer as datetime
        d2 = datetime.strptime(date2, '%Y-%m-%d')

        dif = abs(d2 - d1).hours  # 重点
        return dif

X = Solution()
print(X.daysBetweenDates(date1 = "2019-07-29", date2 = "2019-06-30"))