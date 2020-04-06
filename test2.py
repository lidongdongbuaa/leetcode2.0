class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.mid = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if not root:  # corner case
            return []

        res = []

        def backtrack(root, path):  # save path of string in res
            if not root:
                return

            if root:
                path.append(str(root.val))
                if not root.left and not root.right:
                    res.append(path[:])
                for node in (root.left, root.right):
                    backtrack(node, path)
                path.pop()

        backtrack(root, [])
        ans = ['->'.join(elem) for elem in res]
        return ans

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
print(x.binaryTreePaths(a))