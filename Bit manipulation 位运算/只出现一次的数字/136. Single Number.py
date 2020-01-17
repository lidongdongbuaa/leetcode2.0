#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 7:15
# @Author  : LI Dongdong
# @FileName: 136. Single Number.py
''''''
'''
题目分析
1.要求：Given a non-empty array of integers, every element appears twice except for one. Find that single one.
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
2.理解：数字只出现一次和两次，找出只出现了一次的数字，要求是tO(N), sO(1). 
3.类型：bit manipulation
4.确认输入输出及边界条件：
    1. input:list, repeated? Y order? N, range?N
    2. oupt: int value
    corner case: None? -> None Only one? yes
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
        if nums == []:  # corner case
            return None
        if len(nums) == 1:
            return nums[0]

        dic = {}
        for elem in nums:   # store value, times in dic
            if elem in dic:
                dic[elem] += 1
            else:
                dic[elem] = 1

        for k, v in dic.items():  # output 1 times key
            if v == 1:
                return k
        return 0

x = Solution()
print(x.singleNumber([4,1,2,1,2]))

'''
B.
思路：bit manipulation
方法：
    1. scan list, ^every elem
    2. output left value
time complex: O(N)
space complex: O(1)
易错点：0 和一个数异或后得到那个数，两个相同的数异或后则为 0。
'''
class Solution:
    def singleNumber(self, nums) -> int:
        if nums == []:  # corner case
            return None
        if len(nums) == 1:
            return nums[0]

        res = nums[0]
        for elem in nums[1:]:
            res = res^elem
        return res

x = Solution()
print(x.singleNumber([4,1,2,1,2]))