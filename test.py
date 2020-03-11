class Graph:
    def countIsland(self, grid):  # return number of island
        if not grid:  # corner case
            return 0
        if grid == [['0']]:
            return 0
        if grid == [['1']]:
            return 1

        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        times = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    from collections import deque
                    queue = deque([(i, j)])
                    visited[i][j] = 1
                    while queue:
                        print(len(queue))
                        r, c = queue.popleft()
                        visited[r][c] = 1
                        if r - 1 >= 0 and visited[r - 1][c] == 0 and grid[r - 1][c] == '1':
                            queue.append([r - 1, c])
                            visited[r - 1][c] = 1
                        if r + 1 <= len(grid) - 1 and visited[r + 1][c] == 0 and grid[r + 1][c] == '1':
                            queue.append([r + 1, c])
                            visited[r + 1][c] = 1
                        if c - 1 >= 0 and visited[r][c - 1] == 0 and grid[r][c - 1] == '1':
                            queue.append([r, c - 1])
                            visited[r][c - 1] = 1
                        if c + 1 <= len(grid[0]) - 1 and visited[r][c + 1] == 0 and grid[r][c + 1] == '1':
                            queue.append([r, c + 1])
                            visited[r][c + 1] = 1
                    times += 1
        return times

x = Graph()
print(x.countIsland([['1','1','1','1','1'],['1','1','1','1','1'],['1','1','1','1','1'],['1','1','1','1','1']]))