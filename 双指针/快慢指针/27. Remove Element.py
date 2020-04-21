#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 12:23
# @Author  : LI Dongdong
# @FileName: 27. Remove Element.py
''''''
'''
题目概述：原位删除与目标值相同的数字
题目考点：快慢指针， 把后一位前移到本位；对撞对开指针，把最后一位替换到本位；
解决方案：针对removed的数字特别少的情况，用对撞指针；针对remove特别多的情况，用快慢指针
方法及方法分析：
time complexity order: O(n)
space complexity order: O(1)
如何考
'''
'''
input: 
    nums, list; length range is from 0 to inf; have repeated value; no order
    val, int, value range, may out of range of nums
output:
    int, removed length of nums
corner case
    nums is None, return 0
    value is out of range of nums; return len(nums)

A. slow-fast pointer
    Method:
        1. set slow(s) and fast(f) pointer at 0,0
        2. while f < len(nums)
            if f= target, move f to right
            else:
                s value = f value
                s += 1
        3. return s + 1
    Time complexity: O(n), n is lenght of nums
    Space: O(1)
易错点：注意在while循环弹出时，输出值s在的位置
'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:  # corner case
            return 0
        if val not in nums:
            return len(nums)

        s = f = 0
        n = len(nums)
        while f < n:
            if nums[f] == val:
                f += 1
            else:
                nums[s] = nums[f]
                s += 1
                f += 1
        return s


'''
val = 2
 [0,1,3,0,4,0,4,2]
            s

[3,2,2,3]
'''
'''
之前的方法是把遇到需要删除的元素时，就把后一位的元素前移, 此时元素的顺序不发生变化
现在的方法是遇到删除的元素时，把最后一位的元素放到当前位，此时元素的顺序发生了变化
本种方案的优势在于移除元素很少时的情况

input:
    nums
    val
output: int, length of removed nums
corner case:
    nums is None, return 0
易错点：
    1. 注意l <= r的细节条件-》 解决元素完全等于tager的情况
Time: O(n)
Space: O(1)
'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1 and nums[0] == val:
            return 0
        if len(nums) == 1 and nums[0] != val:
            return 1

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        return l


'''
test case
 val = 3,
 [2,2,2,3]
    l
    r

val = 3
 [3, 3]
  l
  r
'''
