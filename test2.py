class Graph:
    def countIsland(self, grid):  # return numb of island
        if not grid:  # corner case
            return 0
        if grid == [['1']]:
            return 1
        if grid == [['0']]:
            return 0

        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]  # 0 is unvisited
        times = 0

        def dfs(i, j):  # from [i, j] to search its neighbors
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or visited[i][j] == 1 or grid[i][j] == '0':  # end condition
                return

            visited[i][j] = 1
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            return

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    dfs(i, j)
                    times += 1
        return times

'''
test code
'''
x = Graph()
print(x.countIsland([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))