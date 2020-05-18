'''
求所有的路径深度

 input: tree root; root number range is from 0 to inf
 output: int
 corner case
    if root is None, return 0
    if only root, return 1
'''

'''
bfs to scan every node and record [node, depth]
Steps:
    1. create a queue and save[node, depth]
    2. use bfs method to scan every node
        if node is leaf, save depth in res
        push node child and its depth into queue
    3. return res

Time complexity: O(N)
Space: O(N), average case, in best case, O(1)
'''
class Tree:
    def findDepth(self, root):  # return all depth in list
        if not root:
            return [0]
        if not root.left and not root.right:
            return [1]

        res = []

        from collections import deque
        queue = deque([(root, 1)])
        while queue:
            root, depth = queue.popleft()
            if not root.left and not root.right:
                res.append(depth)
            if root.left:
                queue.append([root.left, depth + 1])
            if root.right:
                queue.append([root.right, depth + 1])
        return res
'''
test case [1, 2, 3, 4]
res = [ 2,3]
root = 1
queue = [ ( (4, 3)   ]
root = 1, 2, 3,4
depth = 1, 2, 2, 3
'''