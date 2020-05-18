#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 16:51
# @Author  : LI Dongdong
# @FileName: 求所有路径的深度.py
''''''
'''
题目分析
1.要求：求所有的路径深度
2.理解：
3.类型：
4.确认输入输出及边界条件：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''


 input: tree root; root number range is from 0 to inf
 output: int
 corner case
    if root is None, return 0
    if only root, return 1
'''

'''
dfs to scan every node and record
Steps:
    1. create res = []
    2. create helper(root, depth)
        visit current root, if root is leaf, append depth to res
        visit left child tree
        visit right child tree
    3. return res

Time complexity: O(N)
Space: O(logN)
'''
class Tree:
    def findDepth(self, root):  # return all depth in list
        if not root:
            return [0]
        if not root.left and not root.right:
            return [1]

        res = []

        def helper(root, depth):  # scan every nodes
            if not root:
                return

            if not root.left and not root.right:
                res.append(depth)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
            return

        helper(root, 1)
        return res


'''
test case [1, 2, 3, 4]

corner case, pass

res = [ 3, 2 ]
root = 1, 2, 4, 3
depth = 1, 2, 3, 2

return [3, 2]
'''
'''
bfs to scan every node and record [node, depth]
Steps:
    1. create a queue and save[node, depth]
    2. use bfs method to scan every node
        if node is leaf, save depth in res
        push node child and its depth into queue
    3. return res

Time complexity: O(N)
Space: O(N), average case, in best case, O(1)
'''
class Tree:
    def findDepth(self, root):  # return all depth in list
        if not root:
            return [0]
        if not root.left and not root.right:
            return [1]

        res = []

        from collections import deque
        queue = deque([(root, 1)])
        while queue:
            root, depth = queue.popleft()
            if not root.left and not root.right:
                res.append(depth)
            if root.left:
                queue.append([root.left, depth + 1])
            if root.right:
                queue.append([root.right, depth + 1])
        return res
'''
test case [1, 2, 3, 4]
res = [ 2,3]
root = 1
queue = [ ( (4, 3)   ]
root = 1, 2, 3,4
depth = 1, 2, 2, 3
'''

