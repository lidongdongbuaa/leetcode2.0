
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 22:42
# @Author  : LI Dongdong
# @FileName: 102. Binary Tree Level Order Traversal.py
''''''
'''
题目概述：
题目考点：
解决方案：
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''

'''
input: tree root; node number range is from 0 to inf; node value range is no limit; have order? BST? N
output: list[list]
corner case
    not root, return []

level order traversal, use for loop to scan every level node

time complexity: O(n)
Space: O(1)
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:  # corner case
            return []

        res = []
        from collections import deque
        queue = deque([root])

        while queue:
            n = len(queue)
            level = []
            for _ in range(n):
                root = queue.popleft()
                level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(level)

        return res

'''
dfs - record the level index, add node value to dic's value, then return the dic values

'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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

        return list(dic.values())

