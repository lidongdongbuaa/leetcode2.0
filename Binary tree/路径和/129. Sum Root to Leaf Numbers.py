#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 7:14
# @Author  : LI Dongdong
# @FileName: 129. Sum Root to Leaf Numbers.py
''''''
'''
题目分析
1.要求：Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

    An example is the root-to-leaf path 1->2->3 which represents the number 123.
    
    Find the total sum of all root-to-leaf numbers.
    
    Note: A leaf is a node with no children.
    
    Example:
    
    Input: [1,2,3]
        1
       / \
      2   3
    Output: 25
    Explanation:
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.
    Therefore, sum = 12 + 13 = 25.
    Example 2:
    
    Input: [4,9,0,5,1]
        4
       / \
      9   0
     / \
    5   1
    Output: 1026
    Explanation:
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, sum = 495 + 491 + 40 = 1026.
2.理解：find all path and get int by path and sum of them
3.类型：binary tree path
4.确认输入输出及边界条件：
    input:tree root with tree node API,  0 =<node value <= 9, node numb? N repeated? Y order? N
    output:int
    corner case: None -> 0, only one -> int

5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. find all path and calculate sum of them
    Method:
        1. use pre-order traversal to scan every node;  time complexity O(N), space O(N)
            tmp save node, when meet leaf, save tmp in res [[4,9,5],...]
        2. transfer the res elem into ints;  tO(N) sO(N)
        3. calculate the sum of ints; tO(N) sO(1)
        4. return sum
    time complexity O(N), space O(N)
易错点：
'''

'''
B. directly calculate sum in A method by DFS
    Method:
        1. use pre-order traversal to scan every node; tO(N), sO(logN)
            tmp [4,5,9] save node, when meet leaf, transfer tmp to int and save int in res
        2. return sum of res
    time O(N) spaceO(logN)
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:  # corner casse
            return root.val

        tmp = []
        res = []
        self.dfs(root, tmp, res)
        return sum(res)   # 不是sum[res]

    def dfs(self, root, tmp, res):  # save every path sum in res
        if not root:  # corner case
            return

        tmp.append(root.val)
        if not root.left and not root.right:  # root is leaf
            res.append(self.transfer(tmp))

        self.dfs(root.left, tmp, res)
        self.dfs(root.right, tmp, res)
        tmp.pop()

    def transfer(self, tmp):  # transfer list to int
        if not tmp:  # corner case
            return 0

        if len(tmp) == 1:
            return tmp

        res = 0
        for elem in tmp:  # calculate sum of list
            res = res * 10 + elem
        return res


'''
test code
corner case:
None -> None, only one -> root.val
    Input: [1,2,3]
        1
       / \
      2   3
test main(), then helper()
1. sumNumber()
res = [12, 13] -> return 24
2. dfs()
root = 1 tmp []; res [];
tmp [1]
root.l = 2 = root
tmp [1,2]
res [12]
tmp[1]
root.r = 3 = root
tmp [1,3]
res = [12, 13]
3. transfer
[1,2]
elem = 1
res = 1
elem = 2
res = 1*10 + 2= 12
return res
done well
'''
'''
B. directly calculate sum in A method by dfs iterative
    Method:
易错点： 
    left 和right的顺序搞反了！！！
    r.append(root.right.val) .val不要漏
    stack.append([root.right, r]) .right不要漏
    可以继续把transfer整合到bfs里面
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    class Solution:
        def sumNumbers(self, root: TreeNode) -> int:
            if not root:  # corner case
                return 0
            if not root.left and not root.right:  # corner casse
                return root.val

            res = self.bfs(root)
            return sum(res)  # 不是sum[res]

        def bfs(self, root):  # save every path sum in res
            if not root:  # corner case
                return []
            if not root.left and not root.right:
                return [root.val]

            stack = [[root, [root.val]]]

            res = []
            while stack:
                root, tmp = stack.pop()
                if root.right:
                    r = tmp.copy()
                    r.append(root.right.val)
                    stack.append([root.right, r])
                if root.left:
                    l = tmp.copy()
                    l.append(root.left.val)
                    stack.append([root.left, l])
                if not root.left and not root.right:
                    res.append(self.transfer(tmp))
            return res

        def transfer(self, tmp):  # transfer list to int
            if not tmp:  # corner case
                return 0

            if len(tmp) == 1:
                return tmp

            res = 0
            for elem in tmp:  # calculate sum of list
                res = res * 10 + elem
            return res

'''
C. bfs + queue
Method:
    1. use level order traversal to scan node level by level, while use [root, tmp_sum] to be save in deque
            when meet leaf, save the tmp_sum to res
    2. return res
'''
from collections import deque
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:  # corner casse
            return root.val

        queue = deque([(root, 0)])

        res = 0
        while queue:
            root, tmp = queue.popleft()
            tmp *= 10
            tmp += root.val
            if not root.left and not root.right:
                res += tmp  # add directly
            if root.left:
                queue.append([root.left, tmp])
            if root.right:
                queue.append([root.right, tmp])
        return res


