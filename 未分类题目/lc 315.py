# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 22:13
# @Author  : LI Dongdong
# @FileName: lc 315.py

class BSTNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 0


class Solution:
    def bst_insert(self, node: BSTNode, insert_node: BSTNode, count_small: int):
        if insert_node.val <= node.val:
            node.count = node.count + 1
            if node.left:
                return self.bst_insert(node.left, insert_node, count_small)
            else:
                node.left = insert_node
                return count_small
        elif insert_node.val > node.val:
            count_small = count_small + node.count + 1
            if node.right:
                return self.bst_insert(node.right,insert_node,count_small)
            else:
                node.right=insert_node
                return count_small


    def countSmaller(self, nums):
        node_vec=[]
        count=[]
        nums.reverse()
        for i in range(len(nums)):
            node_vec.append(BSTNode(nums[i])) #list里面是可以加入多种类型的东西的，包括树节点
        count.append(0)
        for j in range(1,len(node_vec)):
            count_small=0
            count_small=self.bst_insert(node_vec[0],node_vec[j],count_small)
            count.append(count_small)
        count.reverse()
        print(count)




x=Solution()
x.countSmaller([5,-7,9,1,3,5,-2,1])
