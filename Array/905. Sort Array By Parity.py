#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 20:56
# @Author  : LI Dongdong
# @FileName: 905. Sort Array By Parity.py
''''''
'''
905. Sort Array By Parity
1.要求：Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
    You may return any answer array that satisfies this condition.
    Input: [3,1,2,4] Output: [2,4,3,1]
    The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
2.理解：数组排序
3.类型：基本题；排序题
4.方法及方法分析：brute force, quick sort
time complexity order: quick sort O(N) = brute force O(N)
space complexity order: quick sort O(1) < brute force O(N)
5.edge case: 
    input: None? Y One? repeat? Y order? N
    output: None/arr/...
    focus on time or space? both
'''

'''
idea：brute force
Method：
    create even list and odd list
    reversal elem, if elem % 2 == 0, add it to even list; else, add it to odd list
    combine even and odd list, return 
time complex: O(N)
space complex: O(N)
易错点：
'''
class Solution:
    def sortArrayByParity(self, A):  # even first, odd later
        if len(A) == 0:  # edge case
            return A
        if len(A) == 1:  # edge case
            return A

        even = []
        odd = []
        for elem in A:  # judge even or odd
            if elem % 2 == 0:
                even.append(elem)
            else:
                odd.append(elem)
        even.extend(odd)
        return even

'''
idea：use quick sort idea
Method：
    choose first elem as the pivot
    put all even elem to the left of pivot and all odd elem to the right
    return the arr
time complex: O(N)
space complex: O(1)
易错点：
    j -= 1, j是从右向左递减了，故要-1，而不是+1！！！
    j= len(A) - 1, 而不是 j = len(A), -1不要漏掉！！
'''
class Solution:
    def sortArrayByParity(self, A):  # even first, odd later
        if len(A) == 0:  # edge case
            return A
        if len(A) == 1:  # edge case
            return A

        i = 0
        j= len(A) - 1
        pivot = A[i]
        while i < j:
            while i < j and A[j] % 2 != 0:  # A[j] is even
                j -= 1
            A[i] = A[j]
            while i < j and A[i] % 2 == 0:  # A[i] is odd
                i += 1
            A[j] = A[i]
        A[i] = pivot
        return A

x = Solution()
x.sortArrayByParity([3,1,2,4])
