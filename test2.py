class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.mid = None
        self.right = None


class Tree:
    def findPath(self, root):
        if not root:
            return []

        res = []

        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:
                res.append(path[:])

            path.append(root.val)
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()

        dfs(root, [])
        return res

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

x = Tree()
print(x.findPath(a))