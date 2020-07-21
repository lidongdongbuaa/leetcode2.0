#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 9:25
# @Author  : LI Dongdong
# @FileName: 103. Binary Tree Zigzag Level Order Traversal.py
''''''
'''
题目分析
1.要求：Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its zigzag level order traversal as:
    [
      [3],
      [20,9],
      [15,7]
    ]
2.理解：use zigzag order to scan and output tree level node
3.类型：binary tree
4.确认输入输出及边界条件：
    input: tree root with API, node repeated? Y order? N node number? value range?
    output: [[level node val]]
    corner case: None - []
4.方法及方法分析： BFS + stack， DFS + helper
time complexity order: BFS + stack O(N) = DFS + helper O(N)
space complexity order: BFS + stack O(N) = DFS + helper O(N)
'''
'''
input: tree root; node number range is from 0 to inf; node value range is no limit; have order? BST? N
output: list[list]
corner case
    not root, return []

bfs, use tag to record the left/right order
'''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:  # corner case
            return []

        from collections import deque
        queue = deque([root])
        res = []
        tag = 0

        while queue:
            n = len(queue)
            level_val = []
            for _ in range (n):
                root = queue.popleft()
                level_val.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            if tag == 0:
                res.append(level_val)
                tag = 1
            else:
                res.append(level_val[::-1])
                tag = 0
        return res

'''
dfs - record the level index, add node value to dic's value, then return the dic values but reverse odd level value

'''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:  # corner case
            return []

        from collections import defaultdict

        dic = defaultdict(list)

        def dfs(root, index):
            if not root:
                return

            dic[index].append(root.val)

            dfs(root.left, index + 1)
            dfs(root.right, index + 1)
            return

        dfs(root, 1)

        res = list(dic.values())
        return [value if index % 2 == 0 else value[::-1] for index, value in enumerate(res)]