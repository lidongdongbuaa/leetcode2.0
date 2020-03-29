class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        if not matrix or matrix == [[]]:
            return 0

        r, c = len(matrix), len(matrix[0])

        visited = [[0 for _ in range(c)] for _ in range(r)]
        def dfs(i, j, d, path):  # save all path length in path
            if i < 0 or j < 0 or i > r - 1 or j > c - 1 or visited[i][j] == 1:
                return


            path.append(d)
            visited[i][j] = 1
            for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                dfs(x, y, d + 1, path)


        res = 0
        for i in range(r):
            for j in range(c):
                path = []
                dfs(i, j, 1, path)
                res = max(res, max(path))
        return res

x = Solution()
x.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])