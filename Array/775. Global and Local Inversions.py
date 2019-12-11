#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 12:10
# @Author  : LI Dongdong
# @FileName: 775. Global and Local Inversions.py
''''''
'''

1.要求：We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
    The number of (global) inversions is the number of i < j, with 0 <= i < j < N and A[i] > A[j].
    The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].
    Return true if and only if the number of global inversions is equal to the number of local inversions.
    Input: A = [1,0,2] Output: true Explanation: There is 1 global inversion, and 1 local inversion.
    Input: A = [1,2,0] Output: false Explanation: There are 2 global inversions, and 1 local inversion.
    A will be a permutation of [0, 1, ..., A.length - 1]. 
    A will have length in range [1, 5000]. 
    The time limit for this problem has been reduced.
2.理解：求全局逆置数和局部逆置数
3.类型：merge sort
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.edge case: 
    input:None？Y only one? Y repeated? N order? N
    output: True / True / True or False
    focus on time or space? Time
'''

'''
idea：brute force
Method：
    For global inversion:  # tO(N2), sO(1)
    traversal elements (i) by for loop
        traversal other next element (j) to compare with i
            if j < i: glo_numb + 1
    For local inversion:  # tO(N), sO(1)
    traversal elements (i) by for loop (i <length -2)
        compare i with i + 1
            if i > i + 1, loc_numb + 1
    compare glo-numb with loc-numb
time complex: O(N2)
space complex: O(1)
易错点：
'''

'''
leetcode 超时
idea：merge sort to calculate glo-numb
Method：
    For global inversion:  tO(NlogN) s(N)
    divide A in to groups of at most one elements
    compares, sort, merge every two groups (i, j), if i > j, numb+1
    compare left two group of two elements, if i > j, i+1...>j, numb + length(left) - i
    Then repeat the above process, until only one group left
    return  numb
time complex: O(NlogN)
space complex: O(N)
易错点：
    glo_numb = self.glo(A.copy()) 时，用merge sort已经改变了arr，不能再用在loc计算中
    故需要复制copy.A 去使用。
'''


class Solution:
    def isIdealPermutation(self, A) -> bool:  # judge glo-num equal loc-num
        if not A:  # edge case
            return True
        if len(A) == 1:  # edge case
            return True

        glo_numb = self.glo(A.copy())  # get global number
        loc_numb = self.loc(A.copy())  # get local number

        if glo_numb == loc_numb:  # judge equal
            return True
        else:
            return False

    def glo(self, arr):  # calcu global inversion number
        if not arr:  # edge case
            return 0
        if len(arr) == 1:  # edge case
            return 0

        length = len(arr)
        g_numb = 0
        mid = length // 2
        L = arr[:mid]
        R = arr[mid:]

        g_numb += self.glo(L)  # recursive to calcu g_numb
        g_numb += self.glo(R)

        i = j = k = 0
        while i < len(L) and j < len(R):  # compare L and R
            if L[i] < R[j]:
                arr[k] = L[i]
                k += 1
                i += 1
            else:
                g_numb += len(L) - i
                arr[k] = R[j]
                k += 1
                j += 1

        while i < len(L):  # add left L part
            arr[k] = L[i]
            k += 1
            i += 1

        while j < len(R):  # add left R part
            arr[k] = R[j]
            k += 1
            j += 1

        return g_numb

    def loc(self, arr):  # calculate loc number
        if not arr:  # egde case
            return 0
        if len(arr) == 1:  # egde case
            return 0

        loc_numb = 0
        for i in range(len(arr) - 1):  # compare and calcu loc_numb
            if arr[i] > arr[i + 1]:
                loc_numb += 1

        return loc_numb


'''
idea：
    A local inversion is also a global inversion. 
    Thus, we only need to check if our permutation has 
    any non-local inversion (A[i] > A[j], i < j) with j - i > 1.
    brute force
Method：
    traversal elements[i] in A
        traversal elements[i+2, i+3...] in A
             if elem[i+2/3..] < element[i] 
                return False
    return True
time complex: O(N2)
space complex: O(1)
易错点：题目条件len(A)>=1
'''


class Solution:
    def isIdealPermutation(self, A) -> bool:
        if len(A) <= 2:  # edge case
            return True

        for i in range(len(A) - 2):
            for j in range(i + 2, len(A)):
                if A[i] > A[j]:
                    return False
        return True


'''
Remember Minimum brute force
idea： 
    check if our permutation has any non-local inversion (A[i] > A[j], i < j) with j - i > 1.
    Remember Minimum - record min(A[0:]), min(A[1:])...
Method：
    iterative A，use stack to record min value of A[0:],..A[n:0]
    iterative A, compare A[i] with stack[i+2]
        if A[i] > stack[i+2] return False
    return True
time complex: O(N2)
space complex: O(N)
易错点：
'''

'''
Remember Minimum R to L
idea： 
    check if our permutation has any non-local inversion (A[i] > A[j], i < j) with j - i > 1.
    Remember Minimum - max A < N, from R to L to compare, make sub compare is O(1)
Method：
    set floor as N
    traversal A from R to L
        floor = min(A[i], floor)
        if A[i-2] > floor, return False
    return True
time complex: O(N)
space complex: O(1)
易错点：[]中有负号也是左开右闭；range内范围不好理解，故用optimized code
'''


class Solution(object):
    def isIdealPermutation(self, A):
        if len(A) <= 2:  # edge case
            return True

        floor = len(A)
        for i in range(len(A) - 1, 1 , -1):  # judge A[i] with min(A[i+2:])
            floor = min(floor, A[i])
            if A[i - 2] > floor:
                return False
        return True

# 先range全部范围，再用if i>= 2进一步圈定，避免了for i in range(len(A) - 1, 1 , -1) 中 1 的难理解，难想到，在范围中，1是不包括的
class Solution(object):
    def isIdealPermutation(self, A):
        if len(A) <= 2:  # edge case
            return True

        floor = len(A)
        for i in range(len(A) - 1, -1 , -1):  # judge A[i] with min(A[i+2:])
            floor = min(floor, A[i])
            if i >= 2 and A[i - 2] > floor:
                return False
        return True

'''
Linear Scan
idea： 
    check if our permutation has any non-local inversion (A[i] > A[j], i < j) with j - i > 1.
    Linear Scan - for local inversion, must Math.abs(A[i] - i) <= 1. So we check this for every i，即A[i]只能在
Method：
    traversal A 
        if not A[i] - i == 1 and not i - A[i] == 1 and not A[i] == i: return False
    return True
time complex: O(N)
space complex: O(1)
易错点：[]中有负号也是左开右闭；range内范围不好理解，故用optimized code
'''

class Solution(object):
    def isIdealPermutation(self, A):
        if len(A) <= 2:  # edge case
            return True

        for i in range(len(A)):
            if not abs(A[i] - i) <= 1:  # no-loc happens
                return False
        return True

# optimized code
class Solution(object):
    def isIdealPermutation(self, A):
        if len(A) <= 2:  # edge case
            return True

        if all(abs(i - j) <= 1 for i, j in enumerate(A)):
            return True
        else:
            return False

x = Solution()
x.isIdealPermutation([1,2,0])
