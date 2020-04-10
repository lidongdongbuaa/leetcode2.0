#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 9:41
# @Author  : LI Dongdong
# @FileName: 191. Number of 1 Bits.py
''''''
'''
题目分析
1.要求：Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
    Input: int 
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
2.理解：
    求一列数中，1的个数
    input: int, only 0, 1? Y length range? <32 outpu: int
3.类型：位运算
4.边界条件：input: None?  -> output: None
5.方法及方法分析： brute force - count '1', bit manipulation - mask, bit manipulation - detect 0, bit manipulation - detect 0
time complexity order: 均O(1)
space complexity order: 均O(1)
'''

'''
A.
思路： brute force - count '1'
方法： 
    1. transfer as bit string
    2. count '1'in bit string
time complex: O(1)  
space complex: O(1)
易错点：bin(n)返回的是string
'''
class Solution:
    def hammingWeight(self, n: int) -> int:  # calculate hamming Weight, output weight
        if n == None:  # corner case
            return None
        return bin(n).count('1')


x = Solution()
print(x.hammingWeight(-3))

'''
B.
思路： bit manipulation - mask
方法： 
    1. loop every bit of n, 
        if find 1, add to numb
time complex: O(1)  Because nn in this piece of code is a 32-bit integer, the time complexity is O(1).
space complex: O(1)
易错点：corner case的判断不能为not n，因为n=0时，not n为1，满足条件
'''

class Solution:
    def hammingWeight(self, n: int) -> int:  # calculate hamming Weight, output weight
        if n == None:  # corner case
            return None

        numb = 0
        for i in range(32):
            numb += (n >> i) & 1
        return numb


x = Solution()
print(x.hammingWeight(3))

'''
C. 
优点：不必对每个bit位进行判断，遇0为止
缺点：还是要依次判断到最后一个1
思路： bit manipulation - detect 0
方法： 
    1. loop every bit of n, 
        if n == 0, return numb
        if find 1, add to numb
time complex: O(1)  Because nn in this piece of code is a 32-bit integer, the time complexity is O(1).
space complex: O(1)
易错点：注意，leetcode默认数字最大为31位 + 符号位
'''

class Solution:
    def hammingWeight(self, n: int) -> int:  # calculate hamming Weight, output weight
        if n == None:  # corner case
            return None

        numb = 0
        for i in range(32):
            tmp = n >> i
            if tmp == 0:
                return numb
            numb += (n >> i) & 1
        return numb

x = Solution()
print(x.hammingWeight(3))

'''
D. 
优点：只进行1的数量个的判断
缺点：
思路： bit manipulation - flips 1
方法： 
    judge the n == 0
        flip least-significant 1 bit to 0
        record the numb of 1 
time complex: O(1)  
space complex: O(1)
易错点：消掉最后一个有效的1： n & n - 1
'''

class Solution:
    def hammingWeight(self, n: int) -> int:  # calculate hamming Weight, output weight
        if n == None:  # corner case
            return None

        numb = 0
        while n != 0:
            n = n & n - 1  # 将 n 和 n - 1 做按位与运算，把最后一个 1 的位变成 0，得到新的n
            numb += 1
        return numb

x = Solution()
print(x.hammingWeight(3))