 #!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 19:11
# @Author  : LI Dongdong
# @FileName: 116. Populating Next Right Pointers in Each Node.py
''''''
'''
题目分析
1.要求：You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

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
    
    
    
    Input: root = [1,2,3,4,5,6,7]
    Output: [1,#,2,3,#,4,5,6,7,#]
    Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
     
    
    Constraints:
    
    The number of nodes in the given tree is less than 4096.
    -1000 <= node.val <= 1000
2.理解：give every node a new pointer to its right node, if it has, else to None
3.类型：binary tree
4.确认输入输出及边界条件：
    input: tree root with definition API, repeated? Y order? N value range? -1000 <= node.val <= 1000 node number? less than 4096
    output: root of the tree Node
    corner case: None? -> None
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''

'''
input: tree node, node number range is from 0 to inf; node value range is no limit; have repeated; no order
output: the root of the tree
corner case
 root is none, return node

bfs from bottom to up
base case
if assume l, r is finished, 
root.left = l; root.right = r, l.next = r, if l.right exist,l.right.next = r.left
return root

time complexity: O(n)
space: O(1)
'''


class Solution:
 def connect(self, root: 'Node') -> 'Node':
     if not root:
         return None

     l = self.connect(root.left)
     r = self.connect(root.right)

     root.left = l
     root.rigth = r
     while l:
         l.next = r
         l = l.right
         r = r.left

     return root

 '''
 bfs
 connect the next in very level
 '''

 class Solution:
     def connect(self, root: 'Node') -> 'Node':
         if not root:
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