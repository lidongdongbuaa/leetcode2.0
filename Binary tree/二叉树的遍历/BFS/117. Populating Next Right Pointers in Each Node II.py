#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 14:16
# @Author  : LI Dongdong
# @FileName: 117. Populating Next Right Pointers in Each Node II.py
''''''
'''
题目分析
1.要求：Given a binary tree
    
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
    
    Initially, all next pointers are set to NULL.
    
     
    
    Follow up:
    
    You may only use constant extra space.
    Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
     
    
    Example 1:
    
    
    
    Input: root = [1,2,3,4,5,null,7]
    Output: [1,#,2,3,#,4,5,7,#]
    Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
     
    
    Constraints:
    
    The number of nodes in the given tree is less than 6000.
    -100 <= node.val <= 100
2.理解：use next to connext the node in same level, the last node pointer to None
3.类型：binary tree
4.确认输入输出及边界条件：
    input: tree root with API, repeated? Y, order? N value range? N number of node? N
    output: root of tree
    corner case:
        None: -> None
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：BFS + for loop
方法：
    save res = root
    use breath first search to scan node level by level
        in same level, connect node each other, the last one pointer to None
    return res
time complex: O(N)
space complex: O(N)
易错点：BFS 一定先写from
'''
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:  # corner case
            return None

        res = root
        queue = deque([root])

        while queue:
            length = len(queue)
            for i in range(length - 1):  # connect the pointer
                queue[i].next = queue[i + 1]
            queue[-1].next = None
            for i in range(length):  # scan every node and push the lower level node
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return res



'''
思路：iterative using up level to connect lower level
方法：
    traversal level
        traversal current level's node - cur
            build dummy and tail for lower level
                if cur has left/right, tail connect the node
            renew cur in this level
        renew cur to next level
time complex: O(N)
space complex: O(1)
易错点：cur = cur.next
'''
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:  # corner case
            return None

        cur = root  # set leftMost as root node
        while cur:
            tail = dummy = Node()

            while cur:  # scan node of cur level
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next

                if cur.right:
                    tail.next = cur.right
                    tail = tail.next

                cur = cur.next
            cur = dummy.next  # renew cur to next level
        return root

