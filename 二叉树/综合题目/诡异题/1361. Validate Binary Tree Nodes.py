#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 11:58
# @Author  : LI Dongdong
# @FileName: Validate Binary Tree Nodes.py
''''''
'''
题目分析
1.要求：You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

    If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

    Note that the nodes have no values and that we only use the node numbers in this problem
2.理解：judge if it is a binary tree given the node left and right node numb
3.类型：binary tree
4.确认输入输出及边界条件：
    input: node number int: n, left list, right list, node range:1 <= n <= 10^4
        len(left or right) = n, value range: -1<= value <= n-1
    output:True or False
    corner case: n== None? N left or right = None? N
        only One: -> True
4.方法及方法分析：construct the tree and judge, Find the parent of each node.
time complexity order: construct the tree and judge O(N) =  Find the parent of each node O(N)
space complexity order: construct the tree and judge O(N) =  Find the parent of each node O(N)
'''
'''
transfer as no direction graph
prove the tree is no cycle and single component tree

method
condition1: n = m - 1
condition2: no cycle
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        if n == 1:  # corner case
            return True

        l = leftChild
        r = rightChild

        # m is number of edge
        m = len([elem for elem in l if elem != -1]) + len([elem for elem in r if elem != -1])

        if n != m + 1:
            return False

        # find the root
        root = []
        l_set = set(l)
        r_set = set(r)
        for i in range(n):
            if i not in l_set and i not in r_set:
                root.append(i)
        if len(root) != 1:
            return False

        # build graph
        root = root[0]

        from collections import defaultdict, deque
        graph = defaultdict(set)

        for index, value in enumerate(l):
            if value != -1:
                graph[index].add(value)

        for index, value in enumerate(r):
            if value != -1:
                graph[index].add(value)

        visited = [0] * n

        queue = deque([root])
        visited[root] = 1

        while queue:
            root = queue.popleft()
            for child in graph[root]:
                queue.append(child)
                if visited[child] == 1:
                    return False
                visited[child] = 1

        if sum(visited) == n:
            return True
        else:
            return False