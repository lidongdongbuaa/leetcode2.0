class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix or matrix == [[]]:  # corner case
            return 0

        m, n = len(matrix), len(matrix[0])

        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]

        maxLength = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (i == 1 and j == 1):
                    if matrix[i - 1][j - 1] == '1':
                        dp[i][j] = 1
                    else:
                        dp[i][j] = float('-inf')
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

                # if dp[i][j] != float('-inf'):
                #     maxLength = max(maxLength, dp[i][j])

        return maxLength * maxLength

x = Solution()
print(x.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))