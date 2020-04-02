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
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        resNode = []

        def dfs(root, path):  # save all path in resNode
            if not root:
                return

            path.append(str(root.val))
            if not root.left and not root.right:
                resNode.append(path[:])

            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()

        dfs(root, [])

        ans = ['->'.join(elem) for elem in resNode]
        return ans

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

'''
D. iterative DSF
    Method:
        stack store root and its string until empty
            stack pop as root and string
            if root is leaf, res add string
            stack append root.right and string + str(root.l.val)
            do same things for left part
        t O(N)  sO(N)
'''
class Solution:
    def binaryTreePaths(self, root):  # return [string]
        if not root:  # corner case
            return []

        res = []
        stack = [[root, str(root.val)]]

        while stack:
            root, string = stack.pop()
            if not root.left and not root.right:
                res.append(string)
            if root.right:
                stack.append([root.right, string + '->' + str(root.right.val)])
            if root.left:
                stack.append([root.left, string + '->' + str(root.left.val)])
        return res