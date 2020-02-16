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
4.方法及方法分析：brute force, compare directly - dfs, compare- bfs
time complexity order: brute force O(N) = compare directly - dfs O(N) = compare- bfs O(N)
space complexity order: brute force O(N) = compare directly - dfs O(N) = compare- bfs O(N)
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
思路：compare node directly - dfs
方法：
    recurse the tree, compare every node
time complex: tO(N)
space complex: 
        best case: O(log(N)), completely balanced tree 
        worst case :O(N), completely unbalanced tree, to keep a recursion stack.
易错点：
'''
'''
Optimized code
未变之处：多种情况下的条件判断没变
优化之处：最后递归的合并
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:  # corner case
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

'''
思路：compare node directly - bfs
方法：
    iterate the tree, compare every node
time complex: tO(N)
space complex: 
        best case: O(log(N)), completely balanced tree 
        worst case :O(N), completely unbalanced tree, to keep a deque
易错点：1.初始的q和p的情况判断
    2. 后面的情况判断
'''
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
        if not p and not q:  # corner case
            return True

        queue = deque()  # ues deque
        queue.append([p, q])

        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2:
                continue
            elif not n1 or not n2:
                return False
            elif n1 and n2:
                if n1.val != n2.val:
                    return False
                else:
                    queue.append([n1.left, n2.left])  # if..elif..elif already contain None case
                    queue.append([n1.right, n2.right])
        return True


