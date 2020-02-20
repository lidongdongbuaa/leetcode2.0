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
A.
思路：BFS scan and add
方法：
    use breath first search to scan every nodes in every level
    in level, turn the node pointer to next node, if no next, pointer to None by for loop
    return copy of root
time complex: O(N)
space complex: O(N)
易错点：for _ in range(width)，不是width-1
    deque具有[i]功能
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

        queue = deque()
        queue.append(root)

        res = root

        while queue:
            width = len(queue)
            for i in range(width - 1):  # turn pointer
                queue[i].next = queue[i + 1]
            queue[width -1].next = None
            for _ in range(width):  # pop and append next level
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return res

'''
test code
corner case: None -> None
root = [1,2,3,4,5,6,7]
q = 1
w = 1
1.next = None
root = 1
queue 2, 3
w = 2
q[0].next = q[1] 2.next = 3
q[1].next = None
root = 2
q 3 4 5
root = 3
q 4 5 6 7
w = 4
i = 0->2
q0.next=q1
q1.next =q2
q2.next = q3
q3.next = None
r = 4,5,6,7
return 1
'''
'''
B.
思路：iterative - use up level to control down level pointer
方法：
    copy root as leftmost
    traversal the node level by level from leftMost node
        move head from leftMost node, change pointer of lower level
            common root, head.left.next = head.right
            uncommon root, head.right.next = head.next.left
    return root
time complex: O(N)
space complex: O(1)
易错点：
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

        leftMost = root  # save root for return

        while leftMost.left:  # for perfect tree, last level node have no left node, only scan last second level
            head = leftMost  # keep leftMost, use head for scan
            while head:  # scan this level, change lower level node pointer
                head.left.next = head.right
                if head.next:  # use next head.left
                    head.right.next = head.next.left
                head = head.next
            leftMost = leftMost.left  # go to next level's leftMost node
        return root
