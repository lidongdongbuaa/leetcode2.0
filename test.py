'''
矩阵
求矩阵一个角到另一个角的所有路径

A.backtrack - template 1
易错点， x是小于m，不是小于m - 1
'''
class Matrix:
    def findPath(self, matrix):  # return all path from [0][0] to [-1][-1]
        if not matrix or matrix == [[]]:  # corner case
            return []

        m, n = len(matrix), len(matrix[0])
        visited = [[0] * n for _ in range(m)]

        def backtrack(i, j, path):  # save path in allPath
            for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m  and 0 <= y < n and visited[x][y] == 0:
                    path.append(matrix[x][y])
                    if x == m - 1 and y == n - 1:
                        allPath.append(path[:])
                    visited[i][j] = 1
                    backtrack(x, y, path)
                    path.pop()
                    visited[i][j] = 0

        allPath = []
        visited[0][0] = 1
        backtrack(0, 0, [matrix[0][0]])
        return allPath


'''
B. backtrack - template 2 from root to backtrack
判断条件别忘visitd
'''
class Matrix:
    def findPath(self, matrix):
        if not matrix or matrix == [[]]:
            return []

        m, n = len(matrix), len(matrix[0])
        visited = [[0] * n for _ in range(m)]

        def backtrack(i, j, path): # save all path in allPath
            if i > m - 1 or i < 0 or j < 0 or j > n - 1 or visited[i][j] == 1:
                return

            path.append(matrix[i][j])
            visited[i][j] = 1

            if i == m - 1 and j == n - 1:
                allPath.append(path[:])

            for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                backtrack(x, y, path)

            path.pop()
            visited[i][j] = 0

        allPath = []
        backtrack(0, 0, [])
        return allPath

x = Matrix()
print(x.findPath([[0,1,2],[3,4,5]]))