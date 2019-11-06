# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 11:11
# @Author  : LI Dongdong
# @FileName: lc 449.py

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def BST_insert(self, node: TreeNode, insert_node: int):
        if node.val > insert_node:
            if node.left:
                self.BST_insert(node.left, insert_node)
            else:
                node.left = TreeNode(insert_node)

        else:
            if node.right:
                self.BST_insert(node.right, insert_node)  # 意思是如果有右端点，则从这个右端点开始继续递归，而不是说从右端点的右端点开始
            else:
                node.right = TreeNode(insert_node)


    def preorder(self, node, layer):
        if not node:
            return
        for i in range(layer):
            print("----", end="")
        print(node.val)
        self.preorder(node.left, layer + 1)
        self.preorder(node.right, layer + 1)

    def BST_search(self,node: TreeNode, value:int):
        if node.val==value:
            return True
        elif value<node.val:
            if node.left:
                self.BST_search(node.left, value)
            elif not node.left:
                return False
        elif node.val<value:
            if node.right:
                self.BST_search(node.right,value)
            elif not node.right:
                return False



    def insert_node(self, test: list, value:int):
        a = TreeNode(test[0])
        a.left = None
        a.right = None
        for i in range(1, len(test)):
            self.BST_insert(a, test[i])
        self.preorder(a, 0)
        self.BST_search(a,value)



testlist = [8, 3, 10, 1, 6, 15]
x = Solution()
x.insert_node(testlist,9)
