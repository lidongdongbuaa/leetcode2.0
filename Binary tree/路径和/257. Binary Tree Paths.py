#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 16:16
# @Author  : LI Dongdong
# @FileName: 257. Binary Tree Paths.py
''''''
'''
题目分析
1.要求：Given a binary tree, return all root-to-leaf paths.

    Note: A leaf is a node with no children.
    
    Example:
    
    Input:
    
       1
     /   \
    2     3
     \
      5
    
    Output: ["1->2->5", "1->3"]
    
    Explanation: All root-to-leaf paths are: 1->2->5, 1->3
2.理解：scan all tree node and return string with ->
3.类型：binary tree path
4.确认输入输出及边界条件：
    input: tree root node with definition, the node's value range? N, number of node? N, repeated? Y ordered? N
    output: list[string]
    corner case:
        None：[]
5.方法及方法分析：DFS, BFS
time complexity order: O(N)
space complexity order: O(N)
6.如何考: 没法考oa
'''
'''
A. dfs + transfer as string
    Method:
        1. main()
            a. corner case
            b. use helper() to transfer tree as node value list [[1,2,5]..]  # time complexity O(N), space O(N)
            c. traversal elements of list to transfer it to [string...]  # time O(N), space O(N)
        2. helper(root, tmp, res): pre-order recursion 
            a. end：root is None
            b. accumulate node.val in tmp, if node is leaf, save it in res
            c. helper(root.left) + helper(root.right)
        time O(N), space O(N)
易错点：
'''

'''
B. move main() c step to b step
    Method:
        1. main()
            a.corner case
            b.use helper() to transfer tree as [string] by transfer()
            c.return [string] 
        2. helper(root, tmp, res): pre-order recursion , return res
            a. end：root is None
            b. accumulate node.val in tmp, if node is leaf, do transfer(tmp) and save it in res
            c. helper(root.left) + helper(root.right)
        3. transfer([nodes.val]): return string
            a.traversal elem in list and add by '->'
        time O(N) sO(N)
'''
class Solution:
    def binaryTreePaths(self, root):  # return [string]
        if not root:  # corner case
            return []

        tmp = []
        res = []
        self.dfs(root, tmp, res)
        return res

    def dfs(self, root, tmp, res):  # res is result
        if not root:
            return

        tmp.append(root.val)
        if not root.left and not root.right:
            res.append(self.transfer(tmp))

        self.dfs(root.left, tmp, res)
        self.dfs(root.right, tmp, res)
        tmp.pop()  # 易错点

    def transfer(self, tmp:list):  # return string
        if not tmp:  # corner case
            return []

        if len(tmp) == 1:
            return str(tmp[0])  # 易错点，不是[str(tmp[0])]

        res = str(tmp[0])
        for elem in tmp[1:]:
            res = res + '->' + str(elem)
        return res

'''
C.BFS iterative method
    Method:
        keep a queue [root, string] to store node, until None
            queue popleft as node, s, if node is leaf, add s to res
            push[root.left, s + node.val]
            push[root.right, , s + node.val]
        return res
    time complexity: O(N), space complexity O(N)
'''
from collections import deque
class Solution:
    def binaryTreePaths(self, root):  # return [string]
        if not root:  # corner case
            return []

        res = []
        queue = deque([(root, str(root.val))])

        while queue:
            root, string = queue.popleft()
            if not root.left and not root.right:
                res.append(string)
            if root.left:
                queue.append([root.left, string + '->' + str(root.left.va)])
            if root.right:
                queue.append([root.right, string + '->' + str(root.right.val)])
        return res