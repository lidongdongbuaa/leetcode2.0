'''
求每层的宽度index宽度

input: tree root; tree root number is from 0 to inf
output: list[int]
corner case
    root is None, return []
    root is only one, return [1]
'''

'''
dfs + dic save index tag
Steps:
    1. use a dict to save level and left first node's index of this level, res is a dict[level: width]
    2. use a helper (node, level, index) by dfs to scan every  node
        if level not in res, save level and index in dict
        else, renew the res
        visit left child node
        visit right child node
    3. transfer res to list
    4. return res
Time complexity: O(N), N is number of nodes
Space: O(logN) in average case; O(N) is worst case for skewed tree
'''
class Tree:
    def findAllWidth(self, root):  # return list containing all width
        if not root:  # corner case
            return  []
        if not root.left and not root.right:
            return [1]

        dic = dict()
        res = dict()
        def dfs(root, level, index):
            if not root:
                return

            if level not in dic:
                dic[level] = index
            else:
                res[level] = index - dic[level] + 1
            dfs(root.left, level + 1, index * 2)
            dfs(root.right, level + 1, index * 2 + 1)
            return

        dfs(root, 1, 1)
        res = [v for k, v in res]
        return res

'''
test case [1, 2, 3, 4]
  1
 2 3
4
'''
