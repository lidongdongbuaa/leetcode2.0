
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) == 0:  # corner case
            return None
        dic = {value : i for i, value in enumerate(inorder)}
        return self.dfs(preorder, inorder, dic, 0, len(preorder), 0, len(inorder))

    def dfs(self, preorder, inorder, dic, pre_l, pre_r, in_l, in_r):  # return root
        if pre_l == pre_r:
            return None

        root = TreeNode(preorder[pre_l])  # 构建当前“根”
        index = dic[preorder[pre_l]]  # 从哈希表中找到当前“根”的索引

        # 更新前序遍历、中序遍历边界，然后递归构建左右子树
        # 我们可以通过“前序和中序个数是相同”这个隐含条件，求出前序左右边界
        root.left = self.dfs(preorder, inorder, dic, pre_l + 1, pre_l + 1 + index - in_l, in_l, index )
        root.right = self.dfs(preorder, inorder, dic, pre_l + 1 + index - in_l, pre_r, index + 1, in_r )
        return root

x = Solution()
print(x.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))