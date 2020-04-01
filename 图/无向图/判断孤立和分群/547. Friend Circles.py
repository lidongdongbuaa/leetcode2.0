#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 15:56
# @Author  : LI Dongdong
# @FileName: 547. Friend Circles.py
''''''
'''
题目分析
1.要求：There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
2.理解：find the isolate number in a undirected graph
3.类型：graph
4.确认输入输出及边界条件：
    input: matrix, [n * n], order? N; n range? [1, 200]
    output:int
    corner case:
        1. None? N
        2. only one? Y

5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. DFS method
    Method:
        1. build visited matrix
        2. scan nodes by traversal
            if node is unvisited
                visit the node and other connected node by dfs(), and marked them visited
            record the scan times as res
        3.return the res
    time O(N) space O(N)
易错点：for j in range(len(M)) 索引的是第i行的第j个数，而不是M[i]里的数
'''
class Solution:
    def findCircleNum(self, M) -> int:
        if len(M) == 1:  # corner case
            return 1

        m = len(M)
        visit = [0] * m
        count = 0

        for i in range(m):
            if visit[i] == 0:
                self.dfs(i, visit, M)
                count += 1
        return count

    def dfs(self, i, visit, M):  # dfs scan all node connected to i node
        if visit[i] == 1:
            return
        visit[i] = 1
        for j in range(len(M)):
            if M[i][j] == 1 and visit[j] == 0:
                self.dfs(j, visit, M)
        return


'''
B. Union-find set
    Method:
        1. create graphTag by using the index as tag
        2. scan every pair(node i, j)
            use dfs() to find the i, and j's root
            if i root = j root, pass
            if i root ！= j root, set j root as i root and record the times
        3. res is the n - times
        4. return the res
    time complexity O(N) space O(N)
易错点：矩阵是左下和右上的三角形，并且for i in range(i + 1)
'''
class Solution:
    def findCircleNum(self, M) -> int:
        if len(M) == 1:  # corner case
            return 1

        m = len(M)
        graphTag = [i for i in range(m)]

        times = 0
        for i in range(m):
            for j in range(i + 1):
                if M[i][j] == 1:
                    root1 = self.find(i, graphTag)
                    root2 = self.find(j, graphTag)
                    if root1 == root2:
                        pass
                    else:
                        graphTag[root2] = root1
                        times += 1
        return m - times

    def find(self, i, graph):  # return root index of i node
        if graph[i] == i:
            return i
        else:
            return self.find(graph[i], graph)

