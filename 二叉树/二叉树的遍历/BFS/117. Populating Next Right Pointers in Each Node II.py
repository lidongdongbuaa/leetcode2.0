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
bfs level scan and connect

time complexity: O(n)
space complexity: O(1)
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:  # base case
            return None

        from collections import deque
        queue = deque([root])

        res = root
        while queue:
            n = len(queue)
            for i in range(n - 1):
                queue[i].next = queue[i + 1]
            for _ in range(n):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)

        return res

'''
scan the node level by level
use next to traverse the node in same level, meanwhile connext next level's node
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        res = root

        while root:  # root is the left most node on every level
            dummy = tail = Node(-1)

            while root:
                if root.left:
                    tail.next = root.left
                    tail = tail.next
                if root.right:
                    tail.next = root.right
                    tail = tail.next

                root = root.next
            root = dummy.next
        return res

