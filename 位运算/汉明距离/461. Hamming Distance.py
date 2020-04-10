#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 20:33
# @Author  : LI Dongdong
# @FileName: 461. Hamming Distance.py
''''''
'''
题目分析
1.要求：The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Input: x = 1, y = 4 Output: 2 Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different
2.理解：求两个数的相同位置上不同数的发生次数和
3.类型：bit manipulation
4.边界条件：0 ≤ x, y < 2**31.
4.方法及方法分析：bit compare， XOR + count 1
time complexity order: O(1)
space complexity order: O(1)
'''
'''
A.
思路：brute force - bit compare
方法：
    1. compare bit one by one
        if dif, add numb 
time complex: O(32) = O(1)
space complex:  O(1)
易错点：
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        numb = 0
        for i in range(32):
            if (x >> i & 1) != (y >> i & 1):
                numb += 1
        return numb

x = Solution()
print(x.hammingDistance(1, 4))

'''
B.
优点：不用32位遍历
思路：XOR + count 1 （可用191的各种方法替换）
方法：
    1. transfer dif value to 1
    2. count 1 
time complex: O(i) = O(1), i is numb of 1
space complex:  O(1)
易错点：
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        numb = 0
        while z != 0:
            z = z & z - 1
            numb += 1
        return numb