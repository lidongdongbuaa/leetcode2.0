#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 8:44
# @Author  : LI Dongdong
# @FileName: 167. Two Sum II - Input array is sorted.py
''''''
'''
暴力解法和二分法参见二分搜索部分
题目概述：在有序列表里，求和等于target的某个数
题目考点：对撞对开指针；while一般放i，j的大体的判断条件，比如i < j，而在while内部放具体的判断条件
解决方案：对撞指针法
方法及方法分析：
time complexity order: O(N) 
space complexity order: O(1)
如何考
'''
'''
input: array; length range is from 2 to inf
    target: int
output: []
corner case:lenght of number is 2, return it

two pointer method
two pointer
    left one, if sum is smaller to target, move right
    right, if value right > target, move left
    until left + right = target
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:  # corner case
            return [1, 2]

        i, j = 0, len(numbers) - 1
        while i < j:
            if target < numbers[i] + numbers[j]:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i + 1, j + 1]

''''
优化代码 
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:  # corner case
            return [1, 2]

        i, j = 0, len(numbers) - 1
        while i < j:
            total = numbers[i] + numbers[j]
            if target < total:
                j -= 1
            elif total < target:
                i += 1
            else:
                return [i + 1, j + 1]