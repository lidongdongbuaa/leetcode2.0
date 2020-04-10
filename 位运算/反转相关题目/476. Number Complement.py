# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 15:48
# @Author  : LI Dongdong
# @FileName: 476. Number Complement.py
''''''
'''
题目分析
1.要求：Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
    The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    You could assume no leading zero bit in the integer’s binary representation.
    Input: 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
2.理解：求二进制数的补，没有前导0
3.类型：bit
4.确认输入输出及边界条件：
    input: int
    ouput: int
    corner case: None?Yes -> None
4.方法及方法分析： brute force - bin - string change,  XOR n×1
time complexity order: O(1)
space complexity order: O(1)
'''
'''
A.
思路： brute force - bin - string change
方法：
    1. use string in binary to show the int
    2. change 1 to 0, 0 to 1
    3. recover the string to int
time complex: O(32) = O(1)
space complex: O(32) = O(1)
易错点： string不支持s[i] = 'a'替换
'''
class Solution:
    def findComplement(self, num: int):
        if num == None:  # corner case
            return None

        strBit = bin(num)[2:]
        newString = ''
        for i in range(len(strBit)):  # flip 1 and 0
            if strBit[i] == '1':
                newString += '0'
            else:
                newString += '1'

        return int(newString, 2)

'''
B.
思路： XOR n×1
方法：
    1. get size of binary of numb
    2. build '1' in the size
    3. '1' XOR num
time complex: O(1)
space complex: O(1)
易错点： 
'''
class Solution:
    def findComplement(self, num: int):
        if num == None:
            return None

        mask = 1
        res = 0

        while num >= mask:
            res = res | mask # 除首位全为1的数
            mask = mask << 1 # # 只有首位为1的数

        return num^res


