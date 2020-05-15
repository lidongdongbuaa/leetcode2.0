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
input:
    numbers, [int]; lenghth range is from 2 to inf; has repeated value; ascending order
    target, int; value range in sum range of numbers
output:
    1-index, [index1, index2]
corner case:
    length of number is 2, return [1, 2]

Two - pointer method
Step:
    1. set head i and end pointer j in numbers
    2. if head value + end pointer < target, head move right; if = target, return [i + 1,j + 1]; else, end j move left
    
    Time complexity: O(n), n is lenght of numbers
    Space: O(1)
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:  # corner case
            return [1, 2]

        n = len(numbers)
        i, j = 0, n - 1
        while i < j:
            total = numbers[i] + numbers[j]
            if total < target:
                i += 1
            elif target == total:
                return [i + 1, j + 1]
            else:
                j -= 1

'''
numbers = [2,7,11,15], target = 9

[2,7,11,15]
 i
    j
total = 9
return [1, 2]
'''
