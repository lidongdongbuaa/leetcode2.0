#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 19:08
# @Author  : LI Dongdong
# @FileName: 113. Path Sum II.py
''''''
'''
题目分析
1.要求：Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
    Note: A leaf is a node with no children.
    
    Example:
    
    Given the below binary tree and sum = 22,
    
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1
    Return:
    
    [
       [5,4,11,2],
       [5,8,4,5]
    ]
2.理解：find all path whose sum = sum, return them is list
3.类型：binary tree path sum
4.确认输入输出及边界条件：
    input:root with tree node API, node val repeated? Y order? N value range? N node numb? N
    output: list[[]]
    corner case: None?-> [], Only one? ->[[node.val]]

5.方法及方法分析：preoder traveral and store, iterative method by stack simulating recursion
time complexity order: 
space complexity order: 
6.如何考？
'''
'''
A. preoder traversal and store
    Method:
        1. main(): corner case + helper() + return
        2. helper(res): return 
            scan every node in pre-order traversal recursion, save them in list  time complexity O(N) Space O(N)
                end condition: not root/ root is leaf and sum of nodes = SUM
                trigger recursion: helper(), list pop last elem 
            time： O(N) Space：O(N)
易错点： corner case是 sum == target，不仅仅是root == leaf
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:  # corner case
            return []

        if not root.left and not root.right and root.val == sum:
            return [[root.val]]

        res = []
        tmp = []
        self.dfs(root, sum, tmp, res)
        return res

    def dfs(self, root, target, tmp, res):  # save all res in res: list
        if not root:  # corner case
            return

        tmp.append(root.val)
        if not root.left and not root.right and sum(tmp) == target:
            res.append(tmp.copy())

        self.dfs(root.left, target, tmp, res)
        self.dfs(root.right, target, tmp, res)
        tmp.pop()

'''
B. iterative method by stack simulating recursion
    Method:
        1. traversal the tree node in pre-order while using stack to store [root, list1 = [nodes value]]
            if list1 sum == Sum, save it in res
    time complexity: O(N) space: O(N)  
易错点：stack模式与BFS模式相同，都是stack[root, XXX] 
'''
from copy import deepcopy
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> bool:
        return self.helper(root, sum)

    def helper(self, root, total):
        if not root:  # corner case
            return []

        if not root.left and not root.right and root.val == total:  # corner case
            return [[root.val]]

        stack = [[root, [root.val]]]
        res = []
        while stack:  # traversal all tree
            root, value = stack.pop()
            if root.right:
                right = value.copy()
                right.append(root.right.val)
                stack.append([root.right, right])
            if root.left:
                left = value.copy()
                left.append(root.left.val)
                stack.append([root.left, left])
            if  not root.left and not root.right and sum(value) == total:
                res.append(deepcopy(value))
        return res

'''
          5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1
test code sum = 22
stack [[5, 5]] res [] tmp[]
stack[]
root 5 value 5
tmp [5]
stack [8,13] [4, 9]
root, val = 4, 9
stack [8,13]
tmp [5, 4]
stack [8,13] [11, 20]
root, val = 11, 20
stack [8,13]
tmp [5, 4, 11]
stack  [8,13] [2, 22] [7, 27]
root, val = 7, 27
stack  [8,13] [2, 22]
tmp [5, 4, 11, 7]
root, val = 2, 22
tmep

'''


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
        if head.left:
            queue.append(head.left)
        if i + 1 == len(new_node):  # if no i + 1 in new_node
            break
        head.right = new_node[i + 1]  # build right and push
        if head.right:
            queue.append(head.right)
        i = i + 2
    return resHead


root = constructTree([1,2])
x = Solution()
print(x.findPath(root, 1))

