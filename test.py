'''
求所有的路径深度

 input: tree root; root number range is from 0 to inf
 output: int
 corner case
    if root is None, return 0
    if only root, return 1
'''

'''
dfs to scan every node and record
Steps:
    1. create res = []
    2. create helper(root, depth)
        visit current root, if root is leaf, append depth to res
        visit left child tree
        visit right child tree
    3. return res

Time complexity: O(N)
Space: O(logN)
'''
class Tree:
    def findDepth(self, root):  # return all depth in list
        if not root:
            return [0]
        if not root.left and not root.right:
            return [1]

        res = []

        def helper(root, depth):  # scan every nodes
            if not root:
                return

            if not root.left and not root.right:
                res.append(depth)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
            return

        helper(root, 1)
        return res


'''
test case [1, 2, 3, 4]

corner case, pass

res = [ 3, 2 ]
root = 1, 2, 4, 3
depth = 1, 2, 3, 2

return [3, 2
'''
