#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 11:02
# @Author  : LI Dongdong
# @FileName: 371. Sum of Two Integers.py
''''''
'''
题目分析 -- 背下来
1.要求：Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
    Example 1:Input: a = 1, b = 2 Output: 3
    Example 2:Input: a = -2, b = 3 Output: 1
2.理解：不用+-进行加减运算
3.类型：bit manipulation
4.确认输入输出及边界条件：
    input: int range
    output: int
    corner case: 0? yse
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
A.
思路：change bit of 2**31 - 1 based on a and b
方法：
我们可以把 a + b 的问题拆分为 (a 和 b 的无进位结果) + (a 和 b 的进位结果)：

无进位加法使用异或运算计算得出
进位结果使用与运算和移位运算计算得出
循环此过程，直到进位为 0。

注意：由于 Python 整数不是 32 位，为了让负数结果能够正确表示，需要做一定处理。

time complex: O(32) = O(1)
space complex: O(1)
易错点：
'''


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 2^32
        MASK = 0x100000000
        mask1 = 1 << 32
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        maxNum = (2 ** 31) - 1

        while b != 0:
            # 不考虑进位加法
            sums = a ^ b
            # 进位
            carry = (a & b) << 1

            # 取余, 范围限制在 [0, 2^32-1] 范围内
            a = sums % MASK
            b = carry % MASK

        # 处理Python整数不是32位问题（负数的正确表示）
        if a <= MAX_INT:
            return a
        else:
            return ~((a % MIN_INT) ^ MAX_INT)

x = Solution()
x.getSum(1, 3)