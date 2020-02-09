class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and q:
            return False
        if not q and p:
            return False
        if not p and not q:  # corner case
            return True

        pdq = deque()
        qdq = deque()
        pdq.append(p)
        qdq.append(q)

        while pdq and qdq:  # bfs two tree
            nodep = pdq.popleft()
            nodeq = qdq.popleft()
            if nodep.val != nodeq.val:  # compare two node
                return False

            if not nodep.left and nodeq.left:
                return False
            elif nodep.left and not nodeq.left:
                return False
            elif nodep.left and nodeq.left:
                pdq.append(nodep.left)
                qdq.append(nodeq.left)

            if not nodep.right and nodeq.right:
                return False
            elif nodep.right and not nodeq.right:
                return False
            elif nodep.right and nodeq.right:
                pdq.append(nodep.right)
                qdq.append(nodeq.right)

        if not pdq and qdq:
            return False
        elif pdq and not qdq:
            return False
        elif not pdq and not qdq:
            return True




a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
# a = []

a1 = TreeNode(1)
b1 = TreeNode(2)
c1 = TreeNode(3)
a1.left = b1
a1.right = c1



x = Solution()
print(x.isSameTree(a, a1))