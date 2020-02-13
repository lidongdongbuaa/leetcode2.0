#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 8:07
# @Author  : LI Dongdong
# @FileName: 662. Maximum Width of Binary Tree.py
''''''
'''
题目分析
1.要求：Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.
    The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
    Example 1:
        Input: 
               1
             /   \
            3     2
           / \     \  
          5   3     9 
        Output: 4
        Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
    Example 2:
        Input: 
             1
             /  
            3    
           / \       
          5   3     
        Output: 2
        Explanation: The maximum width existing in the third level with the length 2 (5,3).
    Example 3:
        Input: 
    
              1
             / \
            3   2 
           /        
          5      
        Output: 2
        Explanation: The maximum width existing in the second level with the length 2 (3,2).
    Example 4:
        Input: 
    
              1
             / \
            3   2
           /     \  
          5       9 
         /         \
        6           7
        Output: 8
        Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
        Note: Answer will in the range of 32-bit signed integer.
2.理解：find the max width of level of tree, None between the node was counted into.
3.类型：binary tree basic
4.确认输入输出及边界条件：
    input: root with definition, no range of node val, repeated? Y, order？ N
    output: int
    corner case: 
        None -> 0
        Only one -> 1
4.方法及方法分析：bfs, dfs
time complexity order: bfs O(N) = dfs O(N)
space complexity order: average dfs O(logN) < bfs O(N)
'''
'''
思路：bfs + count numb
方法：
    1.create a deque to save [node, index of node]
    2 scan all node by bfs
        for one level node, scan them, find the max dif of index
time complex: O(N)
space complex: average O(N) best O(1)
易错点：
    计算核心：计算同一层内的index差值
    控制在同一层内
        queue内会保存所有同层node和下层node，
        故在queue一开始就测量其长度length，即此时queue内只有同层。之后用for循环消耗掉此同层的node，不污染下层node
        解决方案：while内部对queue的value进行循环遍历, 使用len(length)控制遍历的次数，不会遍历到下一层的node
        length是每一层的实际长度
        index差是每一层的声明长度
    计算index差值
        使用[root,index]去保存每个节点的index，上层和下层节点的关系是 n -> n*2, n*2 + 1
        两种编码方式
            每层从0到1-> [root, 0]
            整体的从0到i -> [root,1]

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:  # corner case
            return 1

        queue = deque()
        queue.append([root, 0])  # index from 0 to i in every level
        width = 0

        while queue:
            length = len(queue)  # use length to control the scan range, not scan lower level node
            for i in range(length):  # length 是实际宽度
                node, index = queue.popleft()
                if i == 0:
                    first_num = index
                if i == length - 1:
                    end_num = index
                    width = max(width, end_num - first_num + 1)
                if node.left:
                    queue.append([node.left, 2 * index])
                if node.right:
                    queue.append([node.right, 2 * index + 1])
        return width

'''
test code
None -> 0
only one ->1
[1, 3, None, 5, 3]
queue [1, 0] w = 0
leng = 1
node = 1 ind = 0
i = 0
f = 0
i = 0
end = 0
w = 1
queue [3, 0]
length = 1
    i = 0
    node = 3
    ind = 0
    first = 0
    end = 0
    wid = 1
    queue [5, 0] [3, 1]
leng = 2
    i = 0
        node = 5
        index = 0
        first = 0
    i = 1
        node = 3
        index = 1
        end = 1
        wid = max(1, 2) = 2
return 2  
'''

'''
思路：dfs
方法：
    dfs to scan every node, record level, index of node
        meanwhile use dic to store the first node's level val and index of every level
        compare the index with other same level node's index, to get the max width

time complex: O(N)
space complex: O(logN)
易错点：使用dic的key存储每层的层数值，用value存储该层的第一个index
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        level = 0
        index = 0
        dic ={}  # store level and index
        self.res = 1

        self.dfs(root, level, index, dic)
        return self.res

    def dfs(self, root, level, index, dic):
        if not root:  # corner case
            return

        if level not in dic.keys():  # this level's first node show up firstly in dic, so store its level and index
            dic[level] = index
        else:
            self.res = max(self.res, index - dic[level]+ 1)  # not first show, calculate the distance of index of same level
        self.dfs(root.left, level + 1, index * 2, dic)
        self.dfs(root.right, level + 1, index * 2 + 1, dic)

