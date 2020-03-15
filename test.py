class Solution:
    def calcEquation(self, equations, values, queries):
        def buildMap(equations, values, d):
            for (a, b), c in zip(equations, values):
                d[a][b] = c
                d[b][a] = 1.0 / c

        from collections import defaultdict, deque
        d = defaultdict(dict)
        buildMap(equations, values, d)
        res = []

        def helper(d, query):
            a, b = query
            if a not in d or b not in d:
                return -1.0
            if a == b:
                return 1.0

            q = deque()
            q.append((a, 1.0))
            visited = set()
            visited.add(a)
            while q:
                node, value = q.popleft()
                if node == b:
                    return value
                for v in d[node]:
                    if v not in visited:
                        visited.add(v)
                        q.append((v, value * d[node][v]))
            return -1.0

        for query in queries:
            res.append(helper(d, query))
        return res

x = Solution()
print(x.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))