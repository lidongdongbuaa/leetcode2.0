#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 13:06
# @Author  : LI Dongdong
# @FileName: 求每层的宽度.py
''''''
'''
题目分析
1.要求：求每层中，左边第一个到右边第一个的宽度
2.理解：
3.类型：
4.确认输入输出及边界条件：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
bfs + index tag
Steps:
    1. create a queue with [root, node index]
    2. level first search to scan every node
        current level width = last node of queue's index - first's index, add it to res
        for loop current level's all node
            popleft the node
            if it has child node, push them and its index (2* index (+1)) into queue
    3. return res
Time complexity: O(N), N is number of nodes
Space: O(N) in average case; O(1) is best case for skewed tree
'''


class Tree:
    def findAllWidth(self, root):  # return list containing all width
        if not root:  # corner case
            return []
        if not root.left and not root.right:
            return [1]

        from collections import deque
        queue = deque([(root, 1)])
        res = []

        while queue:
            res.append(queue[-1][1] - queue[0][1] + 1)
            n = len(queue)
            for _ in range(n):
                node, ind = queue.popleft()
                if node.left:
                    queue.append([node.left, ind * 2])
                if node.right:
                    queue.append([node.right, ind * 2 + 1])
        return res


'''
test case [1, 2, 3, 4]
  1
 2 3
4
queue = ( []   )
res = [1]
n = 1.2
node = 1, 2
ind = 1, 2


return [1]
'''
'''
dfs + dic save index tag
Steps:
    1. use a dict to save level and left first node's index of this level, res is a dict[level: width]
    2. use a helper (node, level, index) by dfs to scan every  node
        if level not in res, save level and index in dict
        else, renew the res
        visit left child node
        visit right child node
    3. transfer res to list
    4. return res
Time complexity: O(N), N is number of nodes
Space: O(logN) in average case; O(N) is worst case for skewed tree
'''


class Tree:
    def findAllWidth(self, root):  # return list containing all width
        if not root:  # corner case
            return []
        if not root.left and not root.right:
            return [1]

        dic = dict()
        res = dict()

        def dfs(root, level, index):
            if not root:
                return

            if level not in dic:
                dic[level] = index
            else:
                res[level] = index - dic[level] + 1
            dfs(root.left, level + 1, index * 2)
            dfs(root.right, level + 1, index * 2 + 1)
            return

        dfs(root, 1, 1)
        res = [v for k, v in res]
        return res


'''
test case [1, 2, 3, 4]
  1
 2 3
4
'''