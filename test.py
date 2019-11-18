class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = []
        self.node_list = []

    def preorder(self, root, target):
        if not root:
            return
        self.node_list.append(root.val)
        if root.left is None and root.right is None and sum(self.node_list) == target:
            self.result.append(list(self.node_list))
        self.preorder(root.left, target)
        self.preorder(root.right, target)

    def pathSum(self, root: TreeNode, sum: int):
        self.preorder(root, sum)
        return self.result

'''
test case
'''
a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(11)
d = TreeNode(7)
e = TreeNode(2)
f = TreeNode(8)
g = TreeNode(13)
h = TreeNode(4)
i = TreeNode(1)

a.left = b
a.right = f
b.left = c
c.left = d
c.right = e
f.left = g
f.right = h
h.right = i

x = Solution()
x.pathSum(a, 22)