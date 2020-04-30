#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 12:45
# @Author  : LI Dongdong
# @FileName: Linked List in Binary Tree.py
''''''
'''
题目分析
1.要求：
2.理解：
3.类型：
4.确认输入输出及边界条件：
    input: head with linkedlist, root with binary, repeated value? Y order ? N node val range> [1,100], node numb? [1, 100], tree node numb? [1, 2500]
    output: T/F
    corner case: None? N Only one for linked list? Y only one for tree? Y
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A brute force
    Method: 
        1. transfer linked list node as string
        2. find all path of tree, save them as string in tree-list
        3. check whether linkedlist sting in elem of tree-list
易错点：head = head.next不要漏掉
'''
class Solution:
    def isSubPath(self, head, root) -> bool:
        linkStr = self.transfer(head)

        tmp = []
        tree_res = []
        self.dfs(root, tmp, tree_res)

        for elem in tree_res:
            if linkStr in elem:
                return True
        return False

    def transfer(self, head):  # return linknode in str
        if not head:
            return ''

        res = ''
        while head:
            res += str(head.val)
            head = head.next
        return res

    def dfs(self, root, tmp, tree_res):
        if not root:
            return

        tmp.append(root.val)
        if not root.left and not root.right:
            string= ''
            for elem in tmp:
                string += str(elem)
            tree_res.append(string)

        self.dfs(root.left, tmp, tree_res)
        self.dfs(root.right, tmp, tree_res)
        tmp.pop()
        return



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
def constructTree(nodeList):  # input: list using bfs, output: root
    if not nodeList:  # corner case
        return None

    res = root = TreeNode(nodeList[0])
    queue = deque([(root, 0)])
    while queue:
        root, ind = queue.popleft()
        l_ind = ind * 2 + 1
        r_ind = ind * 2 + 2
        if l_ind < len(nodeList):  # judge if left or right exist
            root.left = TreeNode(nodeList[l_ind])
        if r_ind < len(nodeList):
            root.right = TreeNode(nodeList[r_ind])
        if root.left:
            queue.append([root.left, ind * 2 + 1])
        if root.right:
            queue.append([root.right, ind * 2 + 2])
    return res

root = constructTree([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(1)
b = ListNode(4)
c = ListNode(2)
d = ListNode(6)
a.next = b
b.next = c
c.next = d

x = Solution()
x.isSubPath(a, root)
