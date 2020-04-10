#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 8:40
# @Author  : LI Dongdong
# @FileName: 260. Single Number III.py
''''''
'''
题目分析
1.要求：Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
    Input:  [1,2,1,3,2,5]
    Output: [3,5]
    The order of the result is not important. So in the above example, [5, 3] is also correct.
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
2.理解：一组数，有两个值只出现了一次，其余的都出现两次，求这两个值
3.类型：bit
4.确认输入输出及边界条件：
    input：list[int], repeated? Y order?N
    output：two value of once
    corner case：None? Y only one elem? N
4.方法及方法分析：dic store, XOR 
time complexity order: dic store O(N) = XOR O(N)
space complexity order: XOR(1) < dic storeO(N)
'''
'''
A.
思路：brute force - dic store
方法：
    1. scan list, store value and time in dic's key and value
    2. output 1 value's key
time complex: O(N)
space complex: O(N)
易错点：for k, v in dic.items(): 从value查key
'''


class Solution:
    def singleNumber(self, nums) -> int:
        dic = {}
        for elem in nums:  # store value, times in dic
            if elem in dic:
                dic[elem] += 1
            else:
                dic[elem] = 1

        res = []
        for k, v in dic.items():  # output 1 times key
            if v == 1:
                res.append(k)
        return res


'''
B.
优点：技巧性太强
思路：bit XOR
方法：
    1. 由于出现一次的两个数不等，故两数异或结果不为0，也就是说结果的二进制中至少有一位是1，
    记为第n位。
    2. 我们以第n位是否为1，来把输入分为两个数组，这两个为一的数分别在这两个数组中
    3. 对这两个数组分别求只出现一次的数，即我们要求的数，然后输出
time complex: O(N)
space complex: O(1)
易错点：0 和一个数异或后得到那个数，两个相同的数异或后则为 0。
'''


class Solution:
    def singleNumber(self, nums) -> int:
        if nums == []:  # corner case
            return None

        xor = 0
        for elem in nums:  # get a^b
            xor = xor ^ elem

        for i in range(32):  # find first dif value in bit
            if xor >> i & 1 == 1:
                loc1 = i
                break

        a = 0
        b = 0
        for val in nums:  # divide nums into two groups and find one elem in each group
            if val >> loc1 & 1 == 1:
                a = a ^ val
            else:
                b = b ^ val

        return [a, b]

x = Solution()
print(x.singleNumber([1,2,1,3,2,5]))