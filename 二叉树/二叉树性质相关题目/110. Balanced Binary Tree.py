# -*- coding: utf-8 -*-
# @Time    : 2/11/2020 8:28 PM
# @Author  : LI Dongdong
# @FileName: 110. Balanced Binary Tree.py
''''''
'''
题目分析
1.要求：Given a binary tree, determine if it is height-balanced.
    For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
    Example 1:

    Given the following tree [3,9,20,null,null,15,7]:
    
        3
       / \
      9  20
        /  \
       15   7
    Return true.
    
    Example 2:
    
    Given the following tree [1,2,2,3,3,null,null,4,4]:
    
           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    Return false.

2.理解：left and right node's subtree height difference is no more than 1
3.类型：character of tree
4.确认输入输出及边界条件：
    input: root with definition, no range, repeated? Y order? N
    output: True/False
    corner case: None -> True Only one-> True
4.方法及方法分析：top-down-dfs  bottom-up-dfs
time complexity order: top-down-dfs O(N) < brute force-dfs O(NlogN)
space complexity order: top-down-dfs O(N) = brute force-dfs O(N)
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
        queue.append(head.left)
        if i + 1 == len(new_node):  # if no i + 1 in new_node
            break
        head.right = new_node[i + 1]  # build right and push
        queue.append(head.right)
        i = i + 2
    return resHead


'''
A.
思路：top-down-dfs
方法：
    比较每个节点的子树的最大高度
    main function: scan every node, while compare max height of every node's subtree by DFS or BFS
    helper function: calculate the max height of a root by DFS or BFS
time complex: 
    skewed tree: O(N*N)，but after check the height of the first 2 subtrees, function stop, 
        so it is actually O(N*2) = O(N) 
    average: for height function, O(logN). So it was O(NlogN) for N nodes.
space complex: O(N) The recursion stack may contain all nodes if the tree is skewed.
易错点：测量高度的函数
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:  # corner case
            return True

        if abs(self.depth(root.left) - self.depth(root.right)) > 1:  # check root
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)  # check subtree

    def depth(self, root):  # calculate the height of tree, input:root, output:int
        if not root:  # corner case
            return 0

        if not root.left and not root.right: # corner case
            return 1

        return 1 + max(self.depth(root.left), self.depth(root.right)) # dfs to accumulate depth


root = constructTree([3,9,20,None, None, 15,7])
X = Solution()
print(X.isBalanced(root))


'''
自己的写法
'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        if abs(self.depth(root.left, 0) - self.depth(root.right, 0)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root, numb):  # input: root, output: depth
        if not root:
            return numb

        if not root.left and root.right:
            return self.depth(root.right, numb + 1)

        if root.left and not root.right:
            return self.depth(root.left, numb + 1)

        return max(self.depth(root.left, numb + 1), self.depth(root.right, numb + 1))
'''
test code
input None - True, only one - True
input 
        3
       / \
      9  20
        /  \
       15   7
    root        3   9    20  15   7
    root.left  9   None  15  None None
    root.right  20 NOne   7  None None
    abs(L-R)    1  0      9  0    0
'''
'''
B.
要返回是否平衡，就要需要目前最大深度这个中间变量，故dfs返回两个值，一个是是否平衡，一个是高度
基于求最大深度的模板修改，dfs可以返回多个性质，bottom up的思路
dfs返回是否是balanced,和height
'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:  # corner case
            return True

        def dfs(root):  # return max height and if is balanced
            if not root:
                return True, 0

            leftBalanced, leftH = dfs(root.left)

            rightBalanced, rightH = dfs(root.right)

            if abs(leftH - rightH) > 1 or not leftBalanced or not rightBalanced:
                return False, max(leftH, rightH) + 1
            else:
                return True, max(leftH, rightH) + 1



        isBalanced, maxHeight = dfs(root)
        if isBalanced:
            return True
        else:
            return False

'''
思路：bottom-up- 栈模拟递归
'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        depth, stack = {None: 0}, [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                left, right = depth[node.left], depth[node.right]
                if left == -1 or right == -1 or abs(left-right) > 1:
                    depth[node] = -1  # or return False`
                else:
                    depth[node] = max(left, right) + 1
        return depth[root] != -1
'''
test code
input None - True, only one - True
input 
        3
       / \
      9  20
        /  \
       15   7
    root        3   9    20  15   7
    root.left  9         15  
    root.right           
    depth left     0          0    0
    depth right    0          0     0
    abs         1   0          0     0
    return      3    1     2     1    1
     
'''




