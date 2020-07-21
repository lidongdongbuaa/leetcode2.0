#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 10:21
# @Author  : LI Dongdong
# @FileName: 109. Convert Sorted List to 二分搜索 Tree.py
''''''
'''
题目分析
1.要求：Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
    
    Example:
    
    Given the sorted linked list: [-10,-3,0,5,9],
    
    One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
    
          0
         / \
       -3   9
       /   /
     -10  5
2.理解：use node value of linkedlist to create a height balanced BST
3.类型：create tree
4.确认输入输出及边界条件：
    input: linkedlist head, linkedlist node is order? Y, repeated? N, number of node? N node value range? N
    output: root of tree with definition
    corner case:
        head of linkedlist is None: return None
5.方法及方法分析：brute force - cut linkedlist, 链表转换数组 + 二分, inorder simulation
time complexity order: O(N)
space complexity order: 
6.如何考
'''
'''
input: linked list, length range is from 0 to inf; ascending order; no repeated; 
ouput: root of tree
corner case:
    input is None, return None

Method 1
transfer the linked list to list; time complexity O(n), space O(n)
transfer list to BST by dfs ; time complexity O(n) space O(1)
Time complexity: O(n)
Space: O(n)

'''


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:  # corner case
            return None

        def transferList(head):  # return the listNode value list
            if not head:  # corner case
                return None

            res = []

            while head:
                res.append(head.val)
                head = head.next

            return res

        node_list = transferList(head)

        def transferTree(l):  # return the tree created on the list
            if not l:
                return None
            if len(l) == 1:
                return TreeNode(l[0])

            mid = len(l) // 2
            root = TreeNode(l[mid])

            root.left = transferTree(l[:mid])
            root.right = transferTree(l[mid + 1:])
            return root

        return transferTree(node_list)


'''
Method 2
find the mid directly on the linkedlist
time complexity: O(n*2)
Space O(n)
'''


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        s = f = head
        while f and f.next:
            front_end = s
            s = s.next
            f = f.next.next

        front_end.next = None

        root = TreeNode(s.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(s.next)

        return root


