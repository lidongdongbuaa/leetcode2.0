class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:  # corner casse
            return root.val

        res = self.bfs(root)
        return sum(res)   # 不是sum[res]

    def bfs(self, root):  # save every path sum in res
        if not root:  # corner case
            return []
        if not root.left and not root.right:
            return [root.val]

        stack = [[root, [root.val]]]

        res = []
        while stack:
            root, tmp = stack.pop()
            if root.right:
                r = tmp.copy()
                r.append(root.right.val)
                stack.append([root.right, r])
            if root.left:
                l = tmp.copy()
                l.append(root.left.val)
                stack.append([root.left, l])
            if not root.left and not root.right:
                res.append(self.transfer(tmp))
        return res


    def transfer(self, tmp):  # transfer list to int
        if not tmp:  # corner case
            return 0

        if len(tmp) == 1:
            return tmp

        res = 0
        for elem in tmp:  # calculate sum of list
            res = res * 10 + elem
        return res

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
        if head.left:
            queue.append(head.left)
        if i + 1 == len(new_node):  # if no i + 1 in new_node
            break
        head.right = new_node[i + 1]  # build right and push
        if head.right:
            queue.append(head.right)
        i = i + 2
    return resHead


root = constructTree([4,9,0,5,1])
x = Solution()
print(x.sumNumbers(root))