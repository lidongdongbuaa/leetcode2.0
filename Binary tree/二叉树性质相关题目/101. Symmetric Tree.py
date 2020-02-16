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



