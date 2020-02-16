#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 11:32
# @Author  : LI Dongdong
# @FileName: The K Weakest Rows in a Matrix.py
''''''
'''
题目分析
1.要求：Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.
    A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.
    Input: mat = 
    [[1,1,0,0,0],
     [1,1,1,1,0],
     [1,0,0,0,0],
     [1,1,0,0,0],
     [1,1,1,1,1]], 
    k = 3
    Output: [2,0,3]
    Explanation: 
    The number of soldiers for each row is: 
    row 0 -> 2 
    row 1 -> 4 
    row 2 -> 1 
    row 3 -> 2 
    row 4 -> 5 
    Rows ordered from the weakest to the strongest are [2,0,3,1,4]
2.理解：order by 1 number, return K less 1 rows' index
3.类型：list题
4.确认输入输出及边界条件：
    input: matrix [[]], repeated? Y，order？ N K range? 1 <= k <= m
    output: []
    corner case: None？N Only one? N
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：brute force 
方法：
    1. make list recording sum and index tO(N**2) sO(N)
    2. sort list by sum  tO(NlogN) sO(N)
    3. return k weakest row   tO(N) sO(1)
time complex: tO(N**2)
space complex: sO(N)
易错点：
'''


class Solution:
    def kWeakestRows(self, mat, k):
        data = [[sum(j), i] for i, j in enumerate(mat)]  # record sum and index

        data.sort(key=lambda i: i[0])  # sort list using sum

        return [y for x, y in data[:k]]  # return k weakest row


'''
思路：heap
方法：
    1. dic record index as key, sum(list[i]) as value tO(N**2) sO(N)
    2. build k heap with first k mat[i]'s sum tO(k) sO(k)
    3. push mat[i]'s sum into heap tO(N) sO(k)
    4. return key in dic with k value in heap tO(N) sO(k)
time complex: tO(N**2)
space complex: sO(N)
易错点：
'''
# import heapq
# class Solution:
#     def kWeakestRows(self, mat, k):
#         dic = {}
#         for index, val in enumerate(mat):  # dic record index & sum
#             dic[index] = sum(val)
#
#         heap = [value for key, value in dic.items() if key < k]
#         heapq.heapify(heap)  # build heap with first k
#
#         for key, value in dic.items():  # scan left mat[i]
#             if key >= k:
#                 heapq.heappushpop(heap, value)


x = Solution()
print(x.kWeakestRows([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2))
