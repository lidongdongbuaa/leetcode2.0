# -*- coding: utf-8 -*-
# @Time    : 2/11/2020 11:44 AM
# @Author  : LI Dongdong
# @FileName: Construt Binary Tree from Level Order Traversal.py
''''''
'''
题目分析
1.要求：
2.理解：
3.类型：
4.确认输入输出及边界条件：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
A.
思路：bfs
方法：
time complex: 
space complex:
易错点：while i的判断
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
优化版
A. BFS
    Method:
        use queue to save [root of nodeList[0], index], index in nodeList
        save root as res
        queue scan all node until Noe
            queue popleft as root, index
            root.left/right = nodelist[2*index + 0/+ 1]
            if root.left or right exit, push [them, 2*index + 0/+ 1] into queue
        return res
    time O(N) sO(N)
易错点： 序号要从1开始
'''
from collections import deque
class Solution:
    def constructTree(self, nodeList):  # input: list using bfs, output: root
        if not nodeList:  # corner case
            return None

        res = root = TreeNode(nodeList[0])
        queue = deque([(root, 0)])
        while queue:
            root, ind = queue.popleft()
            l_ind = ind * 2 + 1
            r_ind = ind * 2 + 2
            if l_ind < len(nodeList):  # judge if left or right exist
                root.left = TreeNode(nodeList[l_ind])
            if r_ind < len(nodeList):
                root.right = TreeNode(nodeList[r_ind])
            if root.left:
                queue.append([root.left, ind * 2 + 1])
            if root.right:
                queue.append([root.right, ind * 2 + 2])
        return res

x = Solution()
print(x.constructTree([1, 2, 3, None, 5, None, 7]).left.left.val)
