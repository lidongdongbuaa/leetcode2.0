class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and q:
            return False
        if p and not q:
            return False
        if not p and not q:
            return True

        if p.val != q.val:
            return False
        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right, q.right):
            return False
        return True

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and q:
            return False
        if p and not q:
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
a.left = b
# a.right = c

a1 = TreeNode(1)
b1 = TreeNode(2)
c1 = TreeNode(2)
# a.left = b
a1.right = c1


X = Solution()
data = []
print(X.isSameTree(a, a1))