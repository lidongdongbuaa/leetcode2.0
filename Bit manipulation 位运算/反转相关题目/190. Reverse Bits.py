#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 9:12
# @Author  : LI Dongdong
# @FileName: 190. Reverse Bits.py
''''''
'''
题目分析
1.要求：Reverse bits of a given 32 bits unsigned integer.
    Input: 00000010100101000001111010011100
    Output: 00111001011110000010100101000000
    Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
2.理解：转置数字的二进制表示
3.类型：bit
4.确认输入输出及边界条件：
    input: int < 2**31 - 1
    output: int
    corner case: None？ Y - output None
4.方法及方法分析：brute force - bit list and reverse, change 0 bit based on n
time complexity order: O(1)
space complexity order: O(1)
'''
'''
A.
思路： brute force - bit list and reverse 
方法：
    1. transfer as binary string, fill 0 in left
    2. reverse the string
    3. recover to decimal
time complex: O(32) = O(1)
space complex: O(1)
易错点：别忘记 bin(n)[2:]
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        if n == None:
            return None

        string = bin(n)[2:].zfill(32)
        reverse_string = string[::-1]
        return int(reverse_string, 2)

'''
B.
优点：技巧性太强
思路：change 0 bit based on n
方法：
    1. scan n， res = 0
        if ith == 1, change (31-i)th to 1 of res (res 原本全为0)
time complex: O(32) = O(1)
space complex: O(1)
易错点：原来可以通过方法，改变一个数(e.g. 0)的bit位的
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        if n == None:  # corner case
            return None

        res = 0
        mask = 1
        for i in range(32):
            if n >> i & 1 == 1:
                res  = res | 1 << 31 - i
        return res
