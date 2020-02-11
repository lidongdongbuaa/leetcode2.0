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


root = constructTree([1,2,2,2,None,2])


from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:  # corner case
            return True

        data = []
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(data)

x = Solution()
x.isSymmetric(root)