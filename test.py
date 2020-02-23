

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        height = 0
        res = []
        # self.depth(root, height, res)
        return res

    def depth(self, root):  # root, res:List
        if not root:
            return 0

        height = 0
        if not root.left and not root.right:
            return 1

        height = self.depth(root.left) + 1
        height = self.depth(root.right) + 1
        return height

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


root = constructTree([1,2,3,4,None,5])
x = Solution()
print(x.depth(root))