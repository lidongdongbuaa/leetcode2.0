#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 11:58
# @Author  : LI Dongdong
# @FileName: Validate Binary Tree Nodes.py
''''''
'''
题目分析
1.要求：You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

    If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

    Note that the nodes have no values and that we only use the node numbers in this problem
2.理解：judge if it is a binary tree given the node left and right node numb
3.类型：binary tree
4.确认输入输出及边界条件：
    input: node number int: n, left list, right list, node range:1 <= n <= 10^4
        len(left or right) = n, value range: -1<= value <= n-1
    output:True or False
    corner case: n== None? N left or right = None? N
        only One: -> True
4.方法及方法分析：construct the tree and judge, tree attribute
time complexity order: 
space complexity order: 
'''
'''
A. construct the tree and judge
    method： 
        1. define tree node time complexity O(1) space O(1)
        2. use index as tree value, build all tree node，save tO(N) sO(N)
        3. traversal leftChild and rightChild to connect all node  tO(N) sO(N)
        4. traversal tree in level order and save them in list tO(N) sO(N)
            case 1: if index repeated, meet crosspoint node 
        5. compare length of list with n
            case 2: if meet common subtree node, False 
        6. return T/F
time complex: O(N)
space complex: O(N)
易错点：
    1.  def __init__(self, x): 注意是init
    2. 考虑双向tree会在level order result里的情况
    3. 考虑交叉tree node会在level order result里的情况
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild) -> bool:
        if n == 1:  # corner case
            return True

        tree = []
        for i in range(n):  # create node and save in tree list
            tree.append(TreeNode(i))

        root = tree[0]
        for i in range(n):  # scan leftChild and rightChild
            if leftChild[i] != -1:
                tree[i].left = tree[leftChild[i]]
            if rightChild[i] != -1:
                tree[i].right = tree[rightChild[i]]

        res = self.levelscan(root)  # scan node into list in level order

        if not res:
            return False
        if len(res) == n:  # case 1: repeated node tree
            return True
        else:
            return False

    def levelscan(self, root):  # output: res[node]
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            root = queue.popleft()
            if root.val in res:  # case2: two direction tree
                return None
            res.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return res

X = Solution()
print(X.validateBinaryTreeNodes(n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]))

'''
B. Find the parent of each node. 
    hint: A valid tree must have nodes with only one parent and exactly one node with no parent.
    Method: 
        traversal the leftChild and rightChild seperately, use list to save node with parent
        if list length < n -1, more than one tree
        if list length > n - 1, bidirectional branch

time complex: O(N)
space complex: O(N)
易错点：利用tree的基本性质，除根节点，每个节点都只有一个parent，故数有parent的节点个数，应该为总节点数减1
'''
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild) -> bool:
        if n == 1:  # corner case
            return True

        left = [x for x in leftChild if x != -1]
        right = [x for x in rightChild if x != -1]

        left.extend(right)

        if len(left) == n -1:
            return True
        else:
            return False