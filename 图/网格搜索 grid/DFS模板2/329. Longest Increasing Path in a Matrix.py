#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 16:13
# @Author  : LI Dongdong
# @FileName: 329. Longest Increasing Path in a Matrix.py
''''''
'''
题目概述：一个重复数的矩阵，求递增的路径中最长的长度
题目考点：memorization方法；矩阵dfs当递归的算法
解决方案：brute force， dfs求/返回每个点的最长路径长度； dict记录已经访问过点的路径长度
方法及方法分析：brute force; memorize法
time complexity order: brute force O(m*n*m*n) >  memorize法 O(m * n)
space complexity order: O(m * n)
如何考
'''
'''
find the longest path from every node in martix

input: 
    matrix: size range? from 0 to 100+...; value has order? increaseing? N; repeated? Y
output: int
corner case: 
    matrix is None, return 0
    matrix is [[]], return 0

A.DFS - dfs return the longest path of this node
    Method:
        1. corner case
        2. traversal every node i
            a. dfs on i node, search longest path, and return longest path length
    Time: in worst case,即左右递增和上下递增时，每个节点有两个选择，向右和向下，故是 O(2^(mn))
        * 我认为是 O(mn * mn)，m*n个点，每个点最多访问m*n次别的点
    Space: O(H), recursion stack use the space, in worst case, H is m*n, O(m*n)
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or matrix == [[]]:
            return 0

        r, c = len(matrix), len(matrix[0])

        def dfs(i, j):  # return max path length
            ans = 1
            for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < r and 0 <= y < c and matrix[i][j] < matrix[x][y]:
                    ans = max(ans, dfs(x, y) + 1)
            return ans

        res = 0
        for i in range(r):
            for j in range(c):
                res = max(res, dfs(i, j))
        return res

'''
B.DFS - use memo to save longest path in every node
    Method:
        1. corner case
        2. build a dict memo to save every node's longest path length
        3. traversal every node
            dfs to find the node's longest path using the memo and return
            compare with max val and reset the res

        Time complexity: O(N)
        Space: O(N) using by memo
易错点：
    1. DFS的核心其实也是一种递归
    1. res = max(res, 1 + dfs(x, y))
    2.  memo[(i, j)] = res
'''


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or matrix == [[]]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dfs(i, j):  # return longest path length of i, j
            if (i, j) in memo:
                return memo[(i, j)]

            res = 1
            for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    res = max(res, 1 + dfs(x, y))  # 就是求i，j的path长的递归方法
            memo[(i, j)] = res
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans
