# -*- coding: utf-8 -*-
# @Time    : 2/12/2020 11:25 AM
# @Author  : LI Dongdong
# @FileName: 104. Maximum Depth of Binary Tree.py
''''''
'''
题目分析
1.要求：Given a binary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    
    Note: A leaf is a node with no children.
    
    Example:
    
    Given binary tree [3,9,20,null,null,15,7],
    
        3
       / \
      9  20
        /  \
       15   7
    return its depth = 3.
2.理解：calculate the height of root, and return longest
3.类型：binary tree
4.确认输入输出及边界条件：
    input: root with definition, range? No, repeated? N order? N
    output: int
    corner case：
        None? -> 0
        only one? -> 0
4.方法及方法分析： DFS + 积累height, BFS+ 积累height
time complexity order: DFS + 积累height O(N) = BFS+ 积累height O(N)
space complexity order: DFS + 积累height O(logN) < BFS+ 积累height O(N)
'''
'''
A.
思路：DFS + 积累height
方法：
    dfs to get left and right node height by dfs
    get the max height
time complex: O(N)
space complex: worst O(N), average O(logN)
易错点： 辅助函数用不到
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        if not root.left and not root.right: # corner case
            return 1

        length = 0
        length = self.findLength(root, length)  # find longest height
        return length

    def findLength(self, root, length):  # input: root, output: int
            if not root:  # corner case
                return 0
            if not root.right and not root.left:  # corner case
                return 1

            length = 1 + max(self.findLength(root.left, length), self.findLength(root.right, length))
            return length

'''
optimized Code
优化掉辅助函数findLenght
原因：length 没有起到作用
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        if not root.left and not root.right: # corner case
            return 1

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return 1 + max(left_height, right_height) # get the longest one by dfs

'''
B.
思路：BFS + 积累height
方法：
    1. bfs to scan every node, save the [node, height] in deque
    2. when meet leaf, renew the max height
time complex: O(N)
space complex: best O(1) average O(N)
易错点：height += 1每次pop后都要进行，因为height的前值已经固定在弹出值里了
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:  # corner case
            return 1

        queue = deque()
        queue.append([root, 0])
        max_depth = 0

        while queue:  # bfs scan and record
            node, height = queue.popleft()
            height += 1
            if not node.left and not node.right:  # must have subtree, it can add one
                max_depth = max(height, max_depth)
            if node.left:
                queue.append([node.left, height])
            if node.right:
                queue.append([node.right, height])
        return max_depth

'''
test code:
corner case: 
None : 0 ; only one: 1
case: [1,2,3, None, None, 4, 5]
queue ([1, 0]) max = 0
node = 1 h = 0, h+1= 1
queue [2,1], [3,1]
node = 2, h = 1, h + 1 = 2
max = (0, 2) = 2
node = 3, h = 1, h+ 1 = 2
queue [4, 2], [5, 2]
node = 4, h = 2, h+1 = 3
max = (2, 3) =3
node = 5, h= 2, h+ 1= 3
max = (2, 3) = 3
res = 3
'''
'''
optimized code
设初始height为1
原因：利于在加一层操作：queue.append([node.left, height ])时，对增加node.l/r就增加层的理解
'''
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        queue = deque()
        queue.append([root, 1])
        max_depth = 0

        while queue:  # bfs scan and record
            node, height = queue.popleft()
            if not node.left and not node.right:  # must have subtree, it can add one
                max_depth = max(height, max_depth)
            if node.left:
                queue.append([node.left, height + 1])
            if node.right:
                queue.append([node.right, height + 1])
        return max_depth