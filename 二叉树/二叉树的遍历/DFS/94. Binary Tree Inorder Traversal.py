#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 19:28
# @Author  : LI Dongdong
# @FileName: 94. Binary Tree Inorder Traversal.py
''''''
'''
题目分析
1.要求：Given a binary tree, return the inorder traversal of its nodes' values.

    Example:
    
    Input: [1,null,2,3]
       1
        \
         2
        /
       3
    
    Output: [1,3,2]
    Follow up: Recursive solution is trivial, could you do it iteratively?
2.理解：in-order to scan all node and save them in list
3.类型：binary tree
4.确认输入输出及边界条件：
    input: root with tree API, repeated? Y order? N value range? No range
    output: list[int]
    corner case: 
        None? -> []
        Only one - [int]
4.方法及方法分析：DFS - in order, iterative - 0/1 notation
time complexity order: DFS - in order O(N) =  iterative - 0/1 notation O(N)
space complexity order: DFS - in order O(logN) < iterative - 0/1 notation O(N)
'''
'''
思路：DFS - in- order
方法：
    use depth first search to scan all node, save node in res after scan left node
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # corner case
            return []

        res = []
        res += self.inorderTraversal(root.left)
        res.append(root.val)
        res += self.inorderTraversal(root.right)
        return res

'''
思路：stack to simulate recursion
方法：
    stack store and scan all node
time complex: O(N)
space complex: O(N)
易错点：
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []

        stack = []
        output = []

        # 当前访问节点指针
        p_node = root
        while stack or p_node:
            # 把所有当前访问节点的左孩子都入栈
            while p_node:
                stack.append(p_node)
                p_node = p_node.left

            # 操作栈顶节点，如果是第一次运行到这步，那么这是整棵树的最左节点
            cur_node = stack.pop()
            # 因为已经保证没有左节点，可以访问根节点
            output.append(cur_node.val)

            if cur_node.right:
                # 将指针指向当前节点的右节点
                p_node = cur_node.right

        return output

'''
思路：iterative - 0/1 notation
方法：
    0 unvisited, 1 visited
    use stack to store [root, 0/1] and scan every node
    if 0, append right, root, left node
    if 1, save node in res
time complex: O(N)
space complex: O(N)
易错点：
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:  # corner case
            return []

        stack = [[root, 0]]  # 0 is unvisited, 1 is visited
        res = []

        while stack:  # scan all nodes
            root, notation = stack.pop()
            if notation == 0:
                if root.right:
                    stack.append([root.right, 0])
                stack.append([root, 1])
                if root.left:
                    stack.append([root.left, 0])
            else:
                res.append(root.val)
        return res
