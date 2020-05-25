#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 8:07
# @Author  : LI Dongdong
# @FileName: 662. Maximum Width of Binary Tree.py
''''''
'''
题目分析
1.要求：
2.理解：find the max width of level of tree, None between the node was counted into.
3.类型：binary tree basic
4.确认输入输出及边界条件：
    input: root with definition, no range of node val, repeated? Y, order？ N
    output: int
    corner case: 
        None -> 0
        Only one -> 1
4.方法及方法分析：bfs, dfs
time complexity order: bfs O(N) = dfs O(N)
space complexity order: average dfs O(logN) < bfs O(N)
'''


'''
input: tree node, node number range is from 0 to inf; 
output: int, the max width
corner case
    if root is None,return 0
    if only root, return 1

BFS + index tag
Steps:
    1. create a queue with (node, node index)
    2. calculate the gap between the first node's index with last node's index, renew the res with the gap
    3. use for loop to popleft the all node, if it have child node, push them into the queue
    4. return res
Time complexity: O(n), n is number of nodes
Space: O(n), average case; in worse case, O(1)

'''


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:
            return 1

        from collections import deque
        queue = deque([(root, 1)])

        res = 0
        while queue:
            res = max(res, queue[-1][1] - queue[0][1] + 1)
            n = len(queue)
            for _ in range(n):
                node, index = queue.popleft()
                if node.left:
                    queue.append([node.left, 2 * index])
                if node.right:
                    queue.append([node.right, 2 * index + 1])
        return res


'''
           1
         /   \
        3     2
       / \     \  
      5   3     9 

queue =  (5, 4), (3, 5), (9, 7)
res = 2
n = 2
node = 2
index =3

'''

'''
dfs - 遍历点复杂形式
Steps:
    1. self.res = 0, use dict to record every level's left first index
    2. create a helper function dfs(node, level, index)
        visit current node
            if current level in dict, renew res by calculate gap between current index and dict[level], else, push current level and index into dict
        visite left children tree
        visite right children tree
    3. return res

    Time complexity: O(n)
    Space: O(logN) average case, in worst case, O(n)
易错点： 
index - dic[level] + 1， 加1别忘了

'''
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:
            return 1

        self.res = 0
        dic = dict()

        def dfs(root, level, index):
            if not root:
                return

            if level in dic:
                self.res = max(self.res, index - dic[level] + 1)
            else:
                dic[level] = index
                self.res = max(1, self.res)
            dfs(root.left, level + 1, index * 2)
            dfs(root.right, level + 1, index * 2 + 1)
            return

        dfs(root, 1, 1)
        return self.res

'''
test case
       1
     /   \
    3     2
   / \     \  
  5   3     9 
  
  res = 0
  dic = 2:2, 3:4, 
  root = 3, 5
  level = 2, 3, 3, 2,3
  index = 2, 4, 5, 3,7
  res = 0/1 = 1 / 2 = 2 / 2 = 2/7-4 + 1 = 2 / 4 = 4
  return 4
  
  

'''

