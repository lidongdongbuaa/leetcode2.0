'''
C.DFS
    Method:
        1. build graph
            a -> b 2.0, b -> a 1.0 / 2
        2. do dfs on each pairs in queries
            corner case i or j not in graph
            do dfs, find depth path of i, collect the weight and multiply them as ans
            return ans
        3 sum up the ans and return
    Time complexity: O(e + q*e)
    Space: O(e)
易错点：改为buildMap
'''

from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):
        def buildMap():
            graph = defaultdict(dict)
            for (i, j), val in zip(equations, values):
                graph[i][j] = val
                graph[j][i] = 1.0 / val
            return graph

        graph = buildMap()
        res = []

        def dfs(i, j):  # return pair's multiply result
            if i == j:
                return 1.0

            visited.add(i)
            for elem in graph[i]:
                if elem not in visited:
                    return graph[i][elem] * dfs(elem, j)
            return -1.0


        for i, j in queries:
            if i not in graph or j not in graph:
                res.append(-1.0)
            visited = set()
            res.append(dfs(i, j))
        return res


x = Solution()
print(x.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x2","x4"]]))