#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 11:11
# @Author  : LI Dongdong
# @FileName: 107. Binary Tree Level Order Traversal II.py
''''''
'''
题目分析
1.要求：Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its bottom-up level order traversal as:
    [
      [15,7],
      [9,20],
      [3]
    ]
2.理解：from bottom to up to output every level's node in list
3.类型：binary tree
4.确认输入输出及边界条件：
    input: tree root with API, repeated? Y order ? N value range? N number range? N
    output:[[level node val]]
    corner case: None? -> []
4.方法及方法分析：BFS + reverse , DFS + reverse 
time complexity order: BFS + reverse O(N) = DFS + reverse O(N)
space complexity order: BFS + reverse O(N) = DFS + reverse O(N)
'''
'''
思路：BFS + reverse 
方法：
    use breath first search to scan every node
        use for loop to scan every level node, save them in res
    reverse the res to bottom to up
    return res
time complex: O(N)
space complex: O(N)
易错点：
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:  # corner case
            return []

        res = []
        queue = deque([root])

        while queue:  # scan every node
            length = len(queue)
            tmp = []
            for _ in range(length):  # scan same level node
                root = queue.popleft()
                tmp.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(tmp)
        return res[::-1]

'''
test case

'''
'''
思路：DFS + reverse 
方法：
     main(): set dic, level, run helper(), extract res from dic, then reverse it
     helper():
        use depth first search to scan every node, record the level
            save node in its level dic
time complex: O(N)
space complex: O(N)
易错点：
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:  # corner case
            return []

        dic = {}
        level = 1
        self.dfs(root, dic, level)

        res = [value for value in dic.values()]  # extract res from dic
        res = res[::-1]
        return res

    def dfs(self, root, dic, level):  # output: None, save level and its node in dic
        if not root:  # corner case
            return {}

        if level not in dic:  # save node and its level in dic
            dic[level] = [root.val]
        else:
            dic[level].append(root.val)

        self.dfs(root.left, dic, level + 1)
        self.dfs(root.right, dic, level + 1)
        return


