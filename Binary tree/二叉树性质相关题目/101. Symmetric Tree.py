#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 11:20
# @Author  : LI Dongdong
# @FileName: 101. Symmetric Tree.py
''''''
'''
题目分析
1.要求：Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
    For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    But the following [1,2,2,null,3,null,3] is not:
        1
       / \
      2   2
       \   \
       3    3
    Bonus points if you could solve it both recursively and iteratively.
2.理解： judge whether it is symmetric 
3.类型： binary features
4.确认输入输出及边界条件：
    input: root with definition, repeated? N order? N node numb range? N node value range? N
    output: True or false
    corner case: None? Y - False Only one? Y- True
4.方法及方法分析： recursion, iteration
time complexity order: recursion O(N) iteration O(N)
space complexity order: recursion O(N) iteration O(N)
'''
'''
失败 - 无法完整的生成list
思路：brute force - in-order scan
方法：
    1. in-order scan the tree, save node in list tO(N) sO(N) 
    2. check the list tO(N) sO(1)
time complex:  O(N)
space complex: O(1)
易错点：
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
def constructTree(nodeList):  # input: list using bfs, output: root
    new_node = []
    for elem in nodeList:  # transfer list val to tree node
        if elem:
            new_node.append(TreeNode(elem))
        else:
            new_node.append(None)

    queue = deque()
    queue.append(new_node[0])

    resHead = queue[0]
    i = 1

    while i <= len(new_node) - 1:  # bfs method building
        head = queue.popleft()
        head.left = new_node[i]  # build left and push
        queue.append(head.left)
        if i + 1 == len(new_node):  # if no i + 1 in new_node
            break
        head.right = new_node[i + 1]  # build right and push
        queue.append(head.right)
        i = i + 2
    return resHead

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:  # corner case
            return True

        treeList = self.record(root, [])  # transfer as list

        for i in range(len(treeList) // 2):  # check symmetric
            if treeList[i] != treeList[-(i + 1)]:
                return False
        return True

    def record(self, root: TreeNode, res) -> bool:  # transfer tree node as list
        if not root:  # corner case
            return res

        self.record(root.left, res)
        res.append(root.val)  # in-order traversal
        self.record(root.right, res)
        return res



root = constructTree([1,2,2,3,4,4,3])
x = Solution()
print(x.record(root, []))

'''
失败 - 没做出来
思路：bfs
方法：
    1. save every level's node in list
    2. check the list's symmetric
time complex:  O(N)
space complex: best O(1) worst O(N)
易错点：
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:  # corner case
            return True

        data = []
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(data)

x = Solution()
x.isSymmetric(root)

'''
思路：recursion based on pre-order dfs
方法：
    1. judge two root have same value
    2. judge root1.left == root2.right, and root1.right == root2.left
time complex:  O(N)
space complex: worst O(N), average(logN)
易错点：在r1，r2均不为None的情况下，别忘记if r1.val != r2.val
'''

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:  # corner case
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, r1, r2):  # judge whether r1 is symmetric to r2
        if not r1 and not r2:  # corner case
            return True

        if not r1 or not r2:  # one is None, one is not None
            return False

        if r1.val != r2.val:  # r1, r2 aren't None
            return False
        else:
            return self.isMirror(r1.left, r2.right) and self.isMirror(r1.right, r2.left)

'''
思路：iteration method
方法：
    bfs method to check left and right
time complex: O(N)
space complex: worst O(N) best(1)
易错点：
'''
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:  # corner case
            return True

        queue = deque()
        queue.append([root.left, root.right])

        while queue:
            l, r = queue.popleft()
            if not l and not r:
                pass
            elif not l or not r:
                return False
            elif l and r:
                if l.val != r.val:
                    return False
                else:
                    queue.append([l.left, r.right])
                    queue.append([l.right, r.left])
        return True




