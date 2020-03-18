#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 19:42
# @Author  : LI Dongdong
# @FileName: 658. Find K Closest Elements.py
''''''
'''
没太懂
题目概述：
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
find k Closest Elements of target X, arr is ascending

input: 
    nums,[int]; length range? [0, +1 0000]; value range? No limit
    target: None? Y; value range? No limit; 
    k:int; value range? [0, len(nums)]
output:
    list[int]
corner case:
    nums is None? []
    target is None? []
    k is 0? []
    k is 1? return closest one []


A. brute force - find the x index, and search the front and later k neighbors
    Method:
        1. corner case
        2. traversal arr to find x's index, or bigger one's elems
            [1,2,4], x is 3 -> 4's index
        3. get more half value before x, get less half value after x
        4. return
    Time complexity: O(N) N is length of arr
    Space: O(1)

B. binary search - from 0 to len(arr) - k, to find i index to get min arr[i:i + k]
    Method:
        1. corner case
        2. binary search
            a. set left and right boundary
            b. find the mid, compare x - arr[mid] and arr[mid + k] - x to scale the boundary
            c. return arr[l:l + k]
            
    Time complexity: O(log(N-K)) binary search + O(K) for res slice 
    Space: O(1)

解释：
    首先取寻找i，使[i,i +k]符合题意，故改变r为len(arr) - k - 1
    其次，把x看成mid和mid + k的中点，要使得左半边x->arr[mid]比右半边arr[mid+k]->x更小，故进行比较
    在相等时，继续缩小右边界
    最后返回找到的l值，得到arr[l:l + k]
'''

class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        l, r = 0, len(arr) - k - 1
        while l <= r:
            mid = l + (r - l) // 2
            if x - arr[mid] < arr[mid + k] - x:
                r = mid - 1
            elif x - arr[mid] == arr[mid + k] - x:
                r = mid - 1
            else:
                l = mid + 1
        return arr[l:l + k]
