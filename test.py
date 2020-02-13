
'''
test code
corner case: None -> 0 only one ->1
input: [1, 3, None, 5, 3]
level = 0
index = 0
dic = {}
res = 1
root = 1
dic = 0:0
root = 3 level = 1 index = 0, dic 0:0
dic 1:0 0:0
root 5 level = 2, index= 0, dic 1:0 0:0
dic 2:0, 1:0, 0:0
root 3 level = 2, index = 1, dic 2:0, 1:0, 0:0
res = max(1, 1 - 0 + 1) = 2


'''
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


root = constructTree([1, 3, 2, 5,3, None,9])
x = Solution()
print(x.widthOfBinaryTree(root))