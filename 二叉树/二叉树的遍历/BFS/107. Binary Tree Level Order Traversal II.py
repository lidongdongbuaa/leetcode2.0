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
input: tree root node, number of node is from 0 to inf; node value range is no limit; have repeated; no order? Y
output: list[list]
corner case: 
    root is None, return []

Method: bfs + reverse result
Time complexity: O(n)
Space: O(n)
'''
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:  # corner case
            return []

        from collections import deque
        queue = deque([root])
        res = []

        while queue:
            n = len(queue)
            level_val = []
            for _ in range(n):
                root = queue.popleft()
                level_val.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(level_val)
        return res[::-1]

'''
Method: dfs + reverse result
Time complexity: O(n)
Space: O(n)
'''
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:  # corner case
            return []

        from collections import defaultdict
        dic = defaultdict(list)

        def dfs(root, index):  # scan every node, save it in dic
            if not root:  # base case
                return

            dic[index].append(root.val)

            dfs(root.left, index + 1)
            dfs(root.right, index + 1)

            return

        dfs(root, 0)

        return list(dic.values())[::-1]


