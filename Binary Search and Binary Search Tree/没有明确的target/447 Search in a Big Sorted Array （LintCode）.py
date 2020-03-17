#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 19:44
# @Author  : LI Dongdong
# @FileName: 447 Search in a Big Sorted Array （LintCode）.py
''''''
'''
    Description
    Given a big sorted array with positive integers sorted by ascending order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++). Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.
    
    Return -1, if the number doesn't exist in the array.
    
    Notice
    If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2,147,483,647.
    
    
    Example
    Given [1, 3, 6, 9, 21, ...], and target = 3, return 1.
    
    Given [1, 3, 6, 9, 21, ...], and target = 4, return -1.
    
    
    Challenge
    O(log k), k is the first index of the given target number.
题目概述：在一列未知长度的sorted的array里，寻找target的第一个值的index
题目考点：倍增方法求右边界；求具有有个target值的序列中，target的第一个index；
解决方案：i = i*2； r = mid - 1
方法及方法分析：brute force; binary search
time complexity order: binary search O(logN) < brute force O(N)
space complexity order: O(1)
如何考
'''
'''
input: 
    ArrayReader.get(k) for a big sorted array
    target: int
output: index: int, else -1

A. brute force
    Method:
        continue calling ArrayReady, compare it with target, until find the target
    Time complexity: O(N)
    Space: O(1)

B. binary search
    Method:
        1. find the bigger value than target by 2 times increasing the index of ArrayReady, get X  # run logN times
        2. from 0 to X - 1, use binary search to find first index of target
    Time: O(logN) N is target 
    Space: O(1)
易错点：ArrayReader有限度
'''
class ArrayReader:
    def __init__(self, x):
        return

    def get(self, x):
        return x*2

class Arr:
    def findFirstIndex(self, target):  # return the first index of target
        i = 1
        while ArrayReader.get(i) != -1 and ArrayReader.get(i) <= target:
            i *= 2

        l, r = 0, i - 1
        while l <= r:
            mid = l + (r - l) // 2
            if ArrayReader.get(mid) == target:
                r = mid + 1
            elif ArrayReader.get(mid) < target:
                l = mid + 1
            else:
                r = mid - 1
        if ArrayReader.get(l) == target:
            return l
        else:
            return -1