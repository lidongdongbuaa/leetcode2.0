# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 15:29
# @Author  : LI Dongdong
# @FileName: 1318. Minimum Flips to Make a OR b Equal to c.py
''''''
'''
题目分析
1.要求：Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
a -> 0010 b ->0110 c ->0101
a -> 0001 b -> 0100 c->0101
2.理解：翻转a和b的一些数，让a|b = c，求翻转的最小数量
3.类型：bit
4.方法及方法分析：
    input：a,b,c. 
    output: int
time complexity order: 
space complexity order: 
'''
'''
思路：bit manipulation
方法：
    1. get a|b = tmp, record index i where tmp dif from c in bit
    2. check i in c, a, b, number the flip times
        if c[i] is 0, a,b == 1, add 2
        if c[i] is 0, a or b == 1, add 1
        if c[i] is 1, add 1
time complex: O(32) = O(1)
space complex: O(1)
易错点：
'''
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        tmp = a | b  # or res

        dif = []
        for i in range(32):  # record dif in tmp and c
            if (tmp >> i & 1) != (c >> i & 1):
                dif.append(i)

        times = 0
        for elem in dif:  # number times needed to be flip
            c_tmp = c >> elem & 1
            a_tmp = a >> elem & 1
            b_tmp = b >> elem & 1
            if c_tmp == 0 and a_tmp == 1 and b_tmp == 1:
                times += 2
            elif c_tmp == 0 and (a_tmp == 1 or b_tmp == 1):
                times += 1
            elif c_tmp == 1:
                times += 1

        return times

x = Solution()
print(x.minFlips(1, 2, 3))