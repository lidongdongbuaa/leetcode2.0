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


A. Brute force
    Method:
        1. corner case
        2. target is out of range of nums, return k numbers
        3. traversal elem in nums and compare with target, if target = elem or < elem, stop
            search near k closest elements
    Time O(n)
    Space O(1)

B. binary search
    Method:
        1.
    Time: O(logN)
    Space:O(1)
    
    Intuition
    The array is sorted.
    If we want find the one number closest to x,
    we don't have to check one by one.
    it's straightforward to use binary research.
    
    Now we want the k closest,
    the logic should be similar.
    
    
    Explanation:
    Assume we are taking A[i] ~ A[i + k -1].
    We can binary research i
    We compare the distance between x - A[mid] and A[mid + k] - x
    
    If x - A[mid] > A[mid + k] - x,
    it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
    and we have mid smaller than the right i.
    So assign left = mid + 1.
    
    Note that, you SHOULD NOT compare the absolute value of abs(x - A[mid]) and abs(A[mid + k] - x).
    It fails at cases like A = [1,1,2,2,2,2,2,3,3], x = 3, k = 3
    
    The problem is interesting and good.
    Unfortunately the test cases is terrible.
    The worst part of Leetcode test cases is that,
    you sumbit a wrong solution but get accepted.
    
    You didn't read my post and upvote carefully,
    then you miss this key point.
    
    
    Time Complexity:
    O(log(N - K)) to binary research and find reseult
    O(K) to create the returned list.


'''


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:  # corner case
            return None
        if not k:
            return None
        if x is None:
            return None

        left, right = 0, len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[k + mid] - x:
                left = mid + 1
            elif x - arr[mid] == arr[k + mid] - x:
                right = mid
            else:
                right = mid

        return arr[left:left + k]