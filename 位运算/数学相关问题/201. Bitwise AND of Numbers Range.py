#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 9:39
# @Author  : LI Dongdong
# @FileName: 201. Bitwise AND of Numbers Range.py
''''''
'''
题目分析
1.要求：Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
    Example 1: Input: [5,7] Output: 4
    Example 2:Input: [0,1]Output: 0
2.理解：二进制数字针对每一位数，相对应的与
3.类型：bit
4.确认输入输出及边界条件：
     input: list, int, inclusive,  0<= m <= n <= 2**31 - 1
4.方法及方法分析：& one by one, calculate same number in left of binary number 
time complexity order: calculate same number in left of binary number O(1) < & one by one O(1)
space complexity order: calculate same number in left of binary number O(1) = & one by one O(1)
'''
'''
思路：brute force
方法：& one by one
time complex:  O(n - m + 1)
space complex: O(1)
易错点：res = m 不能为 res = 1，因为1是00001，前面的数bitwise后就归零了
'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:  # corner case
            return m

        res = m
        for elem in range(m + 1, n + 1):
            res = (res & elem)
        return res

x = Solution()
print(x.rangeBitwiseAnd(0, 1))

'''
思路：calculate same number in left of binary number 
方法：
    1. build mask of 31* 1
    2. find the left common, output
    
time complex:  O(1)
space complex: O(1)
易错点：
'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:  # corner case
            return m

        mask = (1 << 31) - 1
        while (m & mask) != (n & mask):
            mask = mask << 1
        return n & mask

x = Solution()
print(x.rangeBitwiseAnd(26, 30))



