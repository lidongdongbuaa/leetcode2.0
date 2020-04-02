class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
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
            path.append(root.val)
            if not root.left and not root.right:
                res.append(path[:])
            findPath(root.left, path)
            findPath(root.right, path)
            path.pop()

        findPath(root, [])
        print(res)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
d.left = g
c.left = f

x = Solution()
x.binaryTreePaths(a)