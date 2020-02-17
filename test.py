class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        queue.append(head.left)
        if i + 1 == len(new_node):  # if no i + 1 in new_node
            break
        head.right = new_node[i + 1]  # build right and push
        queue.append(head.right)
        i = i + 2
    return resHead

from collections import deque
class Solution:
    def allDepth(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0

        queue = deque()
        queue.append([root, 1])

        res = []
        while queue:
            node, height = queue.popleft()
            if not node.left and not node.right:  # root is leaf
                res.append(height)
            if node.left:  # 必须有，否则node.left为None时，下个循环中，node为None，判断Node.left报错
                queue.append([node.left, height + 1])
            if node.right:
                queue.append([node.right, height + 1])
        return res

root = constructTree([1,2,3,4,None,5])
x = Solution()
print(x.allDepth(root))
