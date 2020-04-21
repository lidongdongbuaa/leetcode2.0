#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 15:02
# @Author  : LI Dongdong
# @FileName: 350. Intersection of Two Arrays II.py
''''''
'''
题目概述: 求两个list之间共同的元素，要求输出全部的共同元素
题目考点：dict的使用；two pointer的方法
解决方案：转化小size的为dict，对第二个进行遍历；sorted两个nums，然后two pointer进行比较
方法及方法分析：dict save and count；Sorted and 双指针-数组
time complexity order: dict save and count O(m + n) < Sorted and 双指针-数组 O(nlogn + mlogm)
space complexity order:Sorted and 双指针-数组 O(1) <  dict save and count O(min(m,n))
如何考
'''
'''
give two list, compute the intersection

input: nums,list; length range of nums? [0, 10000]; value range? N; nums has repeated value? Y ; num is order? N
output: list[int]
corner case: 
    one of nums is None? -> []
    both nums is None? -> []


A. brute force - dict save and count
    Method:
        1. corner case
        2. transfer nums1/2 to dict1/2
            [1,2,2,1] -> {1:2,2:2}
        3. compare dict1 with dict2, if they have common key, save min value of it to res
    Time complexity: O(m + n + m/n) = O(m + n), m is length of nums1, n is nums2
    Space O(m + n)

B. !!optimized - dict save and count
    Method:
        1. corner case
        2. transfer min of nums1/2 to dict , here use nums1 as min one
            [1,2,2,1] -> {1:2,2:2}
        3. traversal elems of nums with dict, if has, pust it to result and the value of key of dict reduce one 
    Time complexity: O(min(n,m) + max(n,m)) = O(m + n), m is length of nums1, n is nums2
    Space O(min(m,n))


C. !!Sorted and 双指针-数组
    Method:
        1. corner case
        2. sorted nums1 and 2
        3. use 双指针-数组 to compare the nums, and add the common to result
    Time: O(nlogn + mlogm + max(m,n))
    Space: O(m + n)

Follow up quesitons:
1. if sorted
    use C method

2. if nums1's size is small compared to nums2's size
    use B method transder nums1 to dict


3. What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
    if nums1 fits into memory, use B method to transfer nums1 to dict, so we can sequenetially load and process nums
    if neither of arrays fit into memory, we can apply some partical processing strategies
        1. split the  numeric range into subranges that fit into the memory. Modify B method to collect counts only within a given subrange, and call the method multiple times
        2. Use a extranal sort for both arrays. Modify C method to load and process array sequentially

'''

'Method2'


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:  # corner case
            return []

        dic = {}
        for elem in nums1:
            if elem not in dic:
                dic[elem] = 1
            else:
                dic[elem] += 1

        res = []
        for elem in nums2:
            if elem in dic and dic[elem] >= 1:
                dic[elem] -= 1
                res.append(elem)
        return res


'Method3'


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:  # corner case
            return []

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        i = j = 0
        n1 = len(nums1)
        n2 = len(nums2)

        res = []
        while i <= n1 - 1 and j <= n2 - 1:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res


