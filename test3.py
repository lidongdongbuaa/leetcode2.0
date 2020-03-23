from collections import defaultdict


class Solution:
    def makeConnected(self, n: int, connections) -> int:
        if not connections or connections == [[]]:
            return -1
        if len(connections) < n - 1:
            return -1

        graph = defaultdict(set)
        visited = [0] * n

        for i, j in connections:
            graph[i].add(j)
            graph[j].add(i)

        def dfs(i):  # visited i and neighbors in depth
            visited[i] = 1
            for j in graph[i]:
                if visited[j] == 0:
                    dfs(j)
            return

        times = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                times += 1
        return times - 1

x = Solution()
x.makeConnected(5, [[0,1],[0,2],[3,4],[2,3]])