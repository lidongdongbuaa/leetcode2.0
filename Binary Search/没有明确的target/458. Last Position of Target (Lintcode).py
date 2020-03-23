
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 18:52
# @Author  : LI Dongdong
# @FileName: 458. Last Position of Target (Lintcode).py
''''''
'''
题目分析
Description
    Find the last position of a target number in a sorted array. Return -1 if target does not exist.
    
    
    Example Given [1, 2, 2, 4, 5, 5].
    For target = 2, return 2.
    For target = 5, return 5.
    For target = 6, return -1.

理解：想象是在找一个比target大的且不存在的数的前值，即模板1的r值

方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''

'''
class Solution:
    def lastPosition(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:  # 因为要找末尾值，故继续往mid的右边寻找
                l = mid + 1
            if target < nums[mid]:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        if r < 0:
            return -1
        else:
            if nums[r] == target:
                return r
            else:
                return -1
