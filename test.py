class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
易错点： 
    左子树为空，也算是子树
    不能以leaf间距层数作为判定标准
'''


class Solution:
    def preorderTraversal(self, root: TreeNode):
        if not root:  # corner case
            return []  #

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


from collections import deque
def constructTree(nodeList):  # input: list using bfs, output: root
    new_node = []
    for elem in nodeList:  # transfer list val to tree node
        if elem:
            new_node.append(TreeNode(elem))
        else:
            new_node.append(None)

    queue = deque()
    queue.append(new_node[0])

    resHead = queue[0]
    i = 1

    while i <= len(new_node) - 1:  # bfs method building
        head = queue.popleft()

        head.left = new_node[i]  # build left and push
        if head.left:
            queue.append(head.left)
        if i + 1 == len(new_node):  # if no i + 1 in new_node
            break
        head.right = new_node[i + 1]  # build right and push
        if head.right:
            queue.append(head.right)
        i = i + 2
    return resHead

root = constructTree([1,2, 3, 4, 5, 6,7])
x = Solution()
print(x.preorderTraversal(root))