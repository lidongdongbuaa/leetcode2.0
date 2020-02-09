#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 9:55
# @Author  : LI Dongdong
# @FileName: 100. Same Tree.py
''''''
'''
题目分析
1.要求：Given two binary trees, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
2.理解：judge whether two binary trees are same
3.类型：BT
4.确认输入输出及边界条件：
    input: repeated value? Y ordered? N node val range? None
    output: True or False
    corner case: None? N one only node? N
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：brute force
方法：
    traversal two trees, save them as lists tO(N) sO(N)
    compare these two lists tO(N) sO(1)
time complex: tO(N)
space complex: sO(N)
易错点：
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        data = []
        listP = self.transfer(p, data)  # transfer as list
        data = []
        listQ = self.transfer(q, data)

        if listP == listQ:  # compare
            return True
        else:
            return False

    def transfer(self, treeNode, data):  # transfer tree as list
        if not treeNode:  # corner case
            return data.append(None)

        data.append(treeNode.val)
        self.transfer(treeNode.left, data)
        self.transfer(treeNode.right, data)
        return data


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
a.left = b
# a.right = c

a1 = TreeNode(1)
b1 = TreeNode(2)
c1 = TreeNode(2)
# a.left = b
a1.right = c1

X = Solution()
data = []
print(X.isSameTree(a, a1))

'''
思路：compare node directly
方法：
    recurse the tree, compare every node
time complex: tO(N)
space complex: 
        best case: O(log(N)), completely balanced tree 
        worst case :O(N), completely unbalanced tree, to keep a recursion stack.
易错点：
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and q:
            return False
        if p and not q:
            return False
        if not p and not q:
            return True

        if p.val != q.val:
            return False
        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right, q.right):
            return False
        return True

'''
Optimized code
未变之处：多种情况下的条件判断没变
优化之处：最后递归的合并
'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and q:
            return False
        if p and not q:
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

'''
思路：compare node directly
方法：
    iterate the tree, compare every node
time complex: tO(N)
space complex: 
        best case: O(log(N)), completely balanced tree 
        worst case :O(N), completely unbalanced tree, to keep a deque
易错点：1.初始的q和p的情况判断
    2. 后面的情况判断
'''
from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and q:
            return False
        if not q and p:
            return False
        if not p and not q:  # corner case
            return True

        pdq = deque()
        qdq = deque()
        pdq.append(p)
        qdq.append(q)

        while pdq and qdq:  # bfs two tree
            nodep = pdq.popleft()
            nodeq = qdq.popleft()
            if nodep.val != nodeq.val:  # compare two node
                return False

            if not nodep.left and nodeq.left:
                return False
            elif nodep.left and not nodeq.left:
                return False
            elif nodep.left and nodeq.left:
                pdq.append(nodep.left)
                qdq.append(nodeq.left)

            if not nodep.right and nodeq.right:
                return False
            elif nodep.right and not nodeq.right:
                return False
            elif nodep.right and nodeq.right:
                pdq.append(nodep.right)
                qdq.append(nodeq.right)

        if not pdq and qdq:
            return False
        elif pdq and not qdq:
            return False
        elif not pdq and not qdq:
            return True

'''
Optimized code
未变之处：判断条件
优化之处：
    1. 开头和while中的判断重复，故只保留了while的
    2. 把p和q合并到一个list里，再放入deque
'''
from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = deque()
        stack.append([p, q])

        while stack:
            node1, node2 = stack.popleft()
            if not node1 and not node2:
                continue
            elif not node1 and node2:
                return False
            elif node1 and not node2:
                return False
            elif node1.val != node2.val:
                return False
            elif node1.val == node2.val:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
        return True


