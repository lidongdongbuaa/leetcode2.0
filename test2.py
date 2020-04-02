class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.mid = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) :
        if not root:
            return []

        res = []

        def findPath(root, path):
            if not root:
                return
            # 基于前序遍历，针对root这个值，只管root在循环，root没往左走时，加上，弄完
            for child in (root.left, root.mid, root.right):
                if child: print(child.val)
                findPath(child, path)

        findPath(root, [])
        print(res)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
a.mid = c
a.right = d
b.left = e

x = Solution()
x.binaryTreePaths(a)