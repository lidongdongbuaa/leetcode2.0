#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 22:42
# @Author  : LI Dongdong
# @FileName: 102. Binary Tree Level Order Traversal.py
''''''
'''
题目分析
1.要求：Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
    
    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its level order traversal as:
    [
      [3],
      [9,20],
      [15,7]
    ]
2.理解：level order traversal the tree
3.类型：binary tree
4.确认输入输出及边界条件：
    input: tree node with API, repeat? Y order? N value range? N number of node? N
    output: list[list[]]
    corner case: None? [] 
4.方法及方法分析：BFS, DFS + helper
time complexity order:  BFS O(N) =  DFS + helper O(N)
space complexity order: BFS O(N) =  DFS + helper O(N)
'''
'''
思路：BFS traversal
方法：
    use deque to scan every node in dif level
        use for loop to scan node in same level, save them together in res
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:  # corner case
            return []

        res = []

        queue = deque([root])
        while queue:  # scan node
            tmp = []
            length = len(queue)
            for _ in range(length):
                root = queue.popleft()
                tmp.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(tmp)
        return res

'''
test code
corner case: None -> []
[3,9,20,null,null,15,7]
res []
queue 3
tmp [] [] [] 
len = 1, 2, 2
queue [] [20] [7] []
root = 3, 9, 20, 15, 7 
tmp [3] [9] [9,20] [15] [15, 7]
queue [9, 20] [20] [15,7] [7] []
res [3], [9,20] [15,7]
return res
'''

'''
思路：DFS + helper
方法：
    main: set res, helper(root, level, dic[level] = [node.val])
    helper:
        use depth first search to scan every node, record level in dic, 
            when meeting same level node, save them in dic[level]
time complex: O(N)
space complex: O(N) keep the output structure which contains N node values.
易错点： 
    res = [values for values in dic.values()], 不是items()
    space complex: O(N) keep the output structure which contains N node values.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:  # corner case
            return []

        level = 0
        dic = {}
        self.dfs(root, level, dic)

        res = [values for values in dic.values()]
        return res

    def dfs(self, root, level, dic):  # save level value and its node val in dic
        if not root:  # corner case
            return {}

        if level not in dic:
            dic[level] = [root.val]
        else:
            dic[level].append(root.val)
        self.dfs(root.left, level + 1, dic)
        self.dfs(root.right, level + 1, dic)

'''
test code
None? -> []
test dfs
[3,9,20,null,null,15,7]
level: 0
dic: {}
root: 3, 9, 20, 15,7
dic{0 ： [3], 1:[9, 20], 2:[15, 7] }
root.left: 9, level:1, dic
root.right:20, level:1, dic
root.left: 15, level:2, dic
root.right:7, level:2, dic
return dic

test main
res = [[3], [9, 20], [15, 7]
return res
'''

