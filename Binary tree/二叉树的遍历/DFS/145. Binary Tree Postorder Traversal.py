#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 20:15
# @Author  : LI Dongdong
# @FileName: 145. Binary Tree Postorder Traversal.py
''''''
'''
题目分析
1.要求：
    Given a binary tree, return the postorder traversal of its nodes' values.
    
    Example:
    
    Input: [1,null,2,3]
       1
        \
         2
        /
       3
    
    Output: 
    Follow up: Recursive solution is trivial, could you do it iteratively?
2.理解： post order the tree, output the node val in list
3.类型： binary tree
4.确认输入输出及边界条件：
    input： tree root with API, repeated? Y order? N value range? N
    output: list[int]
    corner case: 
        None -> []
        only one -> [int]
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：DFS - postorder
方法：
    use depth first search to scan every node
    after scan right subtree, save the node val in res
time complex: O(N)
space complex: O(logN)
易错点：
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []

        res = []
        res += self.postorderTraversal(root.left)
        res += self.postorderTraversal(root.right)
        res.append(root.val)
        return res

'''
test case
corner case: None -> []
[1,null,2,3]
res []
root = 1
r.l None
res []
r.r  = 2 = r
r.l = None
r.r = 3 = r
r.l = None
r.r = None
res [3]
res[3,2,1]
'''

'''
思路：stack to simulate recursion
方法：
    stack store and scan all node
    pop root and save its value in res
    stack save root left and right
    reverse res
time complex: O(N)
space complex: O(N)
易错点：
    跟pre-order的关系。pre-order, root-left - right -> root - right - left -> 转置 left - right - root
    故与144的 stack to simulate recursion 关系 -> 改变left和right的append顺序 + res [::-1]
'''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []

        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]

'''
思路：iterative - 0/1 notation
方法：
    0 unvisited, 1 visited
    use stack to store [root, 0/1] and scan every node
    if 0, append root, right, left node
    if 1, save node in res
time complex: O(N)
space complex: O(N)
易错点：append 一定是[root,color]
'''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []

        stack = [[root, 0]]  # 0 is unvisited, 1 is visited
        res = []

        while stack:
            root, color = stack.pop()
            if color == 0:
                stack.append([root, 1])
                if root.right:
                    stack.append([root.right, 0])
                if root.left:
                    stack.append([root.left, 0])
            else:
                res.append(root.val)
        return res


