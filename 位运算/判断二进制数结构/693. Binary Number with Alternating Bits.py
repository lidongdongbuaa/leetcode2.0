#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 12:03
# @Author  : LI Dongdong
# @FileName: 693. Binary Number with Alternating Bits.py
''''''
'''
题目分析
1.要求：Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
Example 1: Input: 5 Output: True
Explanation: The binary representation of 5 is: 101
Example 2: Input: 7 Output: False Explanation: The binary representation of 7 is: 111.
2.理解：判断一个数的二进制形式，是不是01相间
3.类型：bit manipulation
4.确认输入输出及边界条件：
    input: >0 int
    output: True or False
    corner case: NO
4.方法及方法分析： convert to string, bit manipulation
time complexity order: O(1)
space complexity order: O(1)
'''
'''
A.
思路：convert to string
方法：
    1. bin the n as string
    2. scan string, bits[i] != bits[i]
time complex: O(32) = O(1)
space complex: O(1)
易错点：
'''
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)[2:]
        for i in range(len(bits) - 1):
            if bits[i] == bits[i + 1]:
                return False
        return True

'''
B.
思路：bit manipulation
方法：
    1. n right move 1 bit as m， then n^m as a
    2. a & (a + 1), if == 0, True
time complex: O(1)
space complex: O(1)
易错点：a = n >> 1 减少一位，而不是加一位
'''
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n ^ (n >> 1)
        if a & (a + 1) == 0:
            return True
        else:
            return False