#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 19:17
# @Author  : LI Dongdong
# @FileName: 167. Two Sum II - Input array is sorted.py
''''''
'''
题目目的概述 在一列sorted array中，寻找和等于target的两个数，返回i + 1和j + 1
方法及方法分析： traversal and count; binary search
time complexity order: binary search O(NlogN) < traversal and count O(N^2)
space complexity order: O(1)
如何考
'''
'''
find two integer adding up a target, integer is sorted, return these two integer's index (not zero based)

input: array[int], repeated value? N order? Y
output: [index (1-), index]
corner case:
    array: None? N
    array: only one? N
    target: out of range of array combination? N
    target: None? N

A. traversal and count
    Method:
        1. corner case
        2. scan numbers i from 0 to len(nums) - 1
            scan numbers j from i + 1 to len(nums)
                if i + j == target
                    return [i + 1, j + 1]

    Time complexity: O(N*2)
    space: O(1)
易错点：
    scan j from i + 1开始
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:  # corner case
            return None

        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]


'''
B. binary search
    Method:
        1. corner case
        2. traversal i in numbers, other right elems named left elements: numbers[i + 1:]  # tO(N)
            use binary search to find the (target - i)'s index j in left elements # time O(logN)
                if find, return [i + 1, i + 1 + j + 1]

        Time complexity: O(NlogN)
        Space: O(1)

'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:  # corner case
            return None

        for i in range(len(numbers) - 1):
            leftVal = target - numbers[i]
            index = self.find(leftVal, numbers[i + 1:])
            if index != -1:
                return [i + 1, i + index + 2]

    def find(self, target, arr):  # find target's index, else return -1
        if arr is None:
            return -1

        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == arr[mid]:
                return mid
            if target < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1


'''
test case

           0,1,2, 3
numbers = [2,7,11,15], target = 9

pass corner case

len(number - 1) = 3
loop1:
    i = 0
    leftVal = 9 - 2 = 7
    index = 0
    return [0 + 1, 0 + 0 + 2] = [1, 2]


    test the find()    0, 1, 2
    target = 7, arr = [7,11, 15]
    pass corner case
    l, r = 0, 2
    loop1:
        mid = 1
        target = 7, nums[mid] = 11
        r = 0
    loop2:
        l,r = 0,0
        mid = 0
        target = 7, nums[mid] = 7
        return 0
'''