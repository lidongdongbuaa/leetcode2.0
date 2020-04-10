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
思路：BFS + stack
方法：
    use breath first search to scan every node of each level
        use queue and for loop to scan and save every level's node in tmp
        for even level, reverse tmp, add to res
        for odd, add to res
    return res
time complex: O(N)
space complex: O(N)
易错点：实质上是树的层次遍历（广度优先遍历）。只需要把偶数层的结果进行反转即可
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:  # corner case
            return []

        queue = deque([root])
        res = []
        reverse = False  # give signal

        while queue:  # scan every node
            tmp = []
            length = len(queue)
            for _ in range(length):  # scan every level's node
                root = queue.popleft()
                tmp.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            if reverse == False:
                res.append(tmp)
                reverse = True
            else:
                res.append(tmp[::-1])
                reverse = False
        return res

'''
test code
corner case: None -> []
[3,9,20,null,null,15,7]

'''
'''
思路：DFS + helper
方法：
    main()：set res，helper(root, dic = {}, level = 0), transfer dic to res while odd level is reversed
    helper(): 
        depth first search scan every node, use dic to label/save the node's level, level + 1
time complex: O(N)
space complex: O(N)
易错点：根本还是树的层次遍历，关键是从表面上发现问题在于偶数层的反转，和现在方法的联系就是偶数层直接反转即可
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:  # corner case
            return []

        dic = {}
        level = 0
        self.dfs(root, dic, level)

        i = 1
        res = []
        for values in dic.values():
            if i % 2 != 0:
                res.append(values)
            else:
                res.append(values[::-1])
            i += 1
        return res

    def dfs(self, root, dic, level):  # save level and node in dic
        if not root:  # corner case
            return {}

        if level not in dic:  # save node to its level list
            dic[level] = [root.val]
        else:
            dic[level].append(root.val)

        self.dfs(root.left, dic, level + 1)
        self.dfs(root.right, dic, level + 1)
        return
