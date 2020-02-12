class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:  # corner case
            return True

        if self.depth(root) == -1:
            return False
        else:
            return True

    def depth(self, root): # input: root, output: -1 (>1)or 0 (<=1)
        if not root:
            return 0

        if not root.left and not root.right:
            return 0

        depth_left = self.depth(root.left)
        if depth_left == -1:
            return -1

        depth_right = self.depth(root.right)
        if depth_right == -1:
            return -1


        if abs(depth_left - depth_right) > 1:
            return -1
        else:
            return 1 + max(depth_left, depth_right)




