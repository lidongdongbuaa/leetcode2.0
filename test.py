def findPath2(grid):
    m, n = len(grid), len(grid[0])
    visit = [[False] * n for _ in range(m)]
    def dfs(x, y, temp, visit, res):
        visit[x][y] = True

        temp.append(grid[x][y])
        if x == m - 1 and y == n - 1:
            res += [temp[:]]
        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= i < m and 0 <= j < n and not visit[i][j]:
                dfs(i, j, temp, visit, res)
        temp.pop()
        visit[x][y] = False
    res = []
    dfs(0, 0, [], visit, res)
    return res
grid = [[0,1,2],[3,4,5]]
print(findPath2(grid))
print(grid)