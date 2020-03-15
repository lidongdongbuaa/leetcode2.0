#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 22:01
# @Author  : LI Dongdong
# @FileName: 744. Find Smallest Letter Greater Than Target.py
''''''
'''
题目目的概述: 把数字转化为字母，问比target大的最小值
方法及方法分析：A.brute force - traversal and compare； B. binary search
time complexity order: binary search O(logN) < brute force O(N)
space complexity order: O(1)
如何考
'''
'''
find smallest letter Greater than target
clear target

input: letters: list[str,str,...]; repeated? Y; order? Y; length range of letters? [2, 1000]; 
output: string

A.brute force - traversal and compare
    Method:
        1. if target < letters[0] by transfer letter to numb in ord(), return letters[0]
        2. if target >= letters[-1], return letters[0]
        3.traversal string in letters
            if target < string:
                return string
    Time complexity: O(N)
    Space: O(1)
易错点：target在=letters[-1]时，也需要return letters[0]
'''


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if ord(target) < ord(letters[0]) or ord(target) >= ord(letters[-1]):
            return letters[0]

        for elem in letters:
            if ord(target) < ord(elem):
                return elem


'''


B. binary search
    Method:
        1. set left and right boundary as 0 and len(letters) - 1
        2. do while loop, l <= r, to find i which is bigger than target
            mid = l + (r - l) //2
            if letters[mid] == target:
                l = mid + 1
            if target < letters[mid]
                r = mid - 1
            if letters[mid] < target:
                l = mid + 1
        3. return l if l exist, else return letters[0]
    Time complexity: O(logN)
    Space: O(1)

letters = ["c", "f", "j"]
target = "a"

l = 0, r = 2
loop 1:
    mid = 1
    letter[mid] = f > target
    r = mid - 1 = 0
loop2:
    l = r = 0
    mid = 0
    letter[0] = c > target
    r = -1
    return letter[0] = c


'''


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if letters[mid] == target:
                l = mid + 1
            if ord(target) < ord(letters[mid]):
                r = mid - 1
            else:
                l = mid + 1
        if l > len(letters) - 1:
            return letters[0]
        else:
            return letters[l]
