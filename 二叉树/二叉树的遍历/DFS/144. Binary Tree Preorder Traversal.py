#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 16:50
# @Author  : LI Dongdong
# @FileName: 144. Binary Tree Preorder Traversal.py
''''''
'''
题目分析
1.要求：Given a binary tree, return the preorder traversal of its nodes' values.
    Example:
    
    Input: [1,null,2,3]
       1
        \
         2
        /
       3
    
    Output: [1,2,3]
    Follow up: Recursive solution is trivial, could you do it iteratively?
2.理解：前序遍历， 手工栈模拟递归
3.类型：DFS
4.确认输入输出及边界条件：
    input: root of tree, with API of tree, value range? No
    output: list
    corner case: None? -> None Only one? -> [int]
4.方法及方法分析：DFS, iterative - Color notation stack to simulate recursion
time complexity order: DFS O(N) = stack to simulate recursion O(N) = interative - color notation O(N)
space complexity order:  DFS O(logN) < stack to simulate recursion O(N) =  interative - color notation O(N)
'''
'''
思路：DFS
方法：
    use depth first search to scan all node, save root node in res
time complex: O(N)
space complex: average O(logN) worst O(N)
易错点：
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return None

        res = []
        self.dfs(root, res)  # helper() to scan nodes
        return res

    def dfs(self, root, res):  # preorder scan
        if not root:  # corner case
            return None

        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)

'''
test case
corner case: None - None, only one - [int]
[1,null,2,3]
r = 1
res [1]
r.l
r.r =2
res [1, 2]
r = 2
r.l = 3
res [1, 2, 3]
return return ...
'''
'''
optimized code
易错点：corner case return 必须是[], 因为res += 必须加list
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []  # 必须是

        res = []
        res.append(root.val)

        res += self.preorderTraversal(root.left)  # 可以换成res.extend(....)
        res += self.preorderTraversal(root.right)
        return res

'''
思路：stack to simulate recursion
方法：
    use stack to scan all nodes
        pop root, save it in res
        stack save right and left
time complex: O(N)
space complex: O(N)
易错点：
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []  #

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
'''
思路：color notation
方法：
    new - white, visited - gray
    use stack to scan and store every [node, color]
        if color is white, turn gray, push right, left, itself
        if color is gray, output node 
time complex: O(N)
space complex: O(N)
易错点： 对root.right和root.left的判断
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []

        stack = [[root, 0]]  # 0 represent new node for res, 1 represent visited in res

        res = []
        while stack:
            root, color = stack.pop()
            if color == 0:
                if root.right:
                    stack.append([root.right, 0])
                if root.left:
                    stack.append([root.left, 0])
                stack.append([root, 1])
            else:
                res.append(root.val)
        return res