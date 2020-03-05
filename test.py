from collections import defaultdict, deque


class Solution:
    def findPath(self, n, pairs):  # return int
        graph = defaultdict(list)

        visited = {i: 0 for i in range(1, n + 1)}

        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)

        res = []

        for i in range(1, n + 1):
            v = visited.copy()
            g = graph.copy()
            path = []
            longest = self.bfs(i, v, g, path)
            res.append(longest)
        return min(res)

    def bfs(self, i, v, g, path):  # return longest path int
        queue = deque([(i, 1)])
        while queue:
            ind, level = queue.popleft()
            v[ind] = 1
            for elem in g[ind]:
                if v[elem] == 0:
                    queue.append([elem, level + 1])
                else:
                    path.append(level)
        return level - 1


def transfer(case):  # transfer input [string] to find level require format
    print(case)
    n = int(case[0])
    pair = [[int(i), int(j)] for i, j in case[1:]]
    return n, pair


n, pair = transfer(['6', ['1', '4'], ['2', '3'], ['3', '4'], ['4', '5'], ['5', '6']])
x = Solution()
print(x.findPath(n, pair))