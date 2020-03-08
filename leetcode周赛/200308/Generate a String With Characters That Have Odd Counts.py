#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 11:54
# @Author  : LI Dongdong
# @FileName: Generate a String With Characters That Have Odd Counts.py
''''''
'''
题目分析
1.要求：Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

    The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  
    
     
    
    Example 1:
    
    Input: n = 4
    Output: "pppz"
    Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".
    Example 2:
    
    Input: n = 2
    Output: "xy"
    Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".
    Example 3:
    
    Input: n = 7
    Output: "holasss"
     
    
    Constraints:
    
    1 <= n <= 500
2.理解：26之内的话，return n letters, more than 26, give repeated odd letter + 26 letters
3.类型：
4.确认输入输出及边界条件：
    input: int [1,500]
    output: string
    corner case:
        n = 1
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. brute force
    Method:
        1. if n<= 26, return chr(numb)
        2 if n > 26, 
            n is odd, return n * a
            n is even, return a - z + (n - 26) * a
易错点： a = chr(97)
'''
class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:  # corner case
            return 'a'

        if n <= 26:
            res = ''
            for i in range(1, n + 1):
                res += chr(i + 96)
        else:
            if n % 2 == 0:
                res = 'a' * (n - 26)
                for i in range(1, 27):
                    res += chr(i + 96)
            else:
                res = n * 'a'
        return res

x = Solution()
print(x.generateTheString(55))