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
A. brute force - cut linkedlist
    Method:
        recursion(list head) return root
        end: head is None
        slow and fast pointer, when fast is None or fast.next is None, slow in mid
        pre_slow.next = None
        root = slow
        root.left = recursion(head)
        root.right = recursion(slow.next)
    time O(NlogN) space O(N)
易错点：  while fast and fast.next 不是or，要确保两个存在，有一个不行都不行
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:  # corner case
            return None

        if not head.next:
            return TreeNode(head.val)

        slow = fast = head
        while fast and fast.next:
            prev_s = slow
            slow = slow.next
            fast = fast.next.next

        prev_s.next = None
        root = TreeNode(slow.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root


'''
B. 链表转换数组 + 二分
    Method:
        1. traveral linkedlist to save node val in list  # time complexity O(N) space O(N)
        2. self.binary(list) recursion, return root  # time O(N) sO(N)
            end: list is None
            mid = len(list) // 2
            root.left = binary(left list)
            root.right = binary(right list)
        return root
    tO(N)  sO(N) O(N) to keep the output, and O(logN) for the recursion stack
易错点： root = TreeNode(nodeList[mid]) 不是 root = TreeNode(mid)
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:  # corner case
            return None

        nodeList = self.transfer(head)
        root = self.dfs(nodeList)
        return root

    def transfer(self, head):  # output [nodes' val]
        if not head:  # corner case
            return []

        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    def dfs(self, nodeList):  # return tree root node
        if not nodeList:  # corner case
            return None

        if len(nodeList) == 1:
            return TreeNode(nodeList[0])

        mid = len(nodeList) // 2
        root = TreeNode(nodeList[mid])

        root.left = self.dfs(nodeList[:mid])
        root.right = self.dfs(nodeList[mid + 1:])
        return root

'''
test code
corner case: None -> None
check main then helper()
[-10,-3,0,5,9]
1. sortedListToBST
    nodelist = [-10,-3,0,5,9]
    root
    return root
2. transfer()
    res = []
    head = -10
    loop 1:
        res = [-10]
        head = -3
    loop 2：
        res = [-10, -3]
        head = 0
    loop 3:
        res = [-10, -3, 0]
        head = 5
    loop 4
        res = [-10, -3, 0, 5]
        head = 9
     loop 5
        res = [-10, -3, 0, 5,9]
        head = None
    return res
3. dfs()
    mid = 5 // 2 = 2
    root = 0
    root.left = dfs([-10, 3])
    mid = 2 // 2= 1
    root = 3
    root.left = dfs([:mid]) = dfs[-10]
    return treeNode(-10)
    root.right = dfs([mid + 1:]) = dfs []
    return None
    
     0
    /  \
   3    9
  /  \  /
-10  N  5 
    root.left = dfs([3:]) = dfs[5, 9]
    mid = 2// 2 = 1
    root = 9
    root.left = dfs(5)
    root.right = None
    
    return root
'''
'''
C. inorder simulation
    Method:
        1. iterative over the linkedlist to find its length
        2. fnd the mid elem by (start + end) // 2
        3. recurse on the left half by using start, mid -1 as starting and ending points
        4. head as root, and head = head.next
        5. recurse on the right half by using mid + 1, end as starting and ending points
    time O(N) sO(N): while recursion use O(logN)
'''
class Solution:

    def findSize(self, head):
        tmp = head
        res = 0
        while tmp:
            tmp = tmp.next
            res += 1
        return res


    def sortedListToBST(self, head):
        # Get the size of the linked list first
        size = self.findSize(head)


        # Recursively form a BST out of linked list from l --> r
        def convert(l, r):
            nonlocal head
            #

            # Invalid case
            if l > r:
                return None

            mid = (l + r) // 2

            # First step of simulated inorder traversal. Recursively form
            # the left half
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node
            node = TreeNode(head.val)
            node.left = left

            # Maintain the invariance mentioned in the algorithm
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)
            return node
        return convert(0, size - 1)



