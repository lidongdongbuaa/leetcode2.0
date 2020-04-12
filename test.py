class Solution:
    def numOfWays(self, n: int) -> int:
        # if n == 1:
        #     return 12

        m = n
        n = 3

        memo = {}

        def dp(i, j, color):  # return color combination numbers
            if (i, j) in memo:
                return memo[(i, j)]

            if i < 0 or j < 0:
                return 0

            if i == 0 and j == 0:
                return 1

            ans = 0
            if color == 'R':
                ans = dp(i - 1, j, 'B') + dp(i, j - 1, 'Y') - dp(i -1, j - 1, 'R') + dp(i - 1, j, 'Y') + dp(i, j - 1, 'B')  - dp(i -1, j - 1, 'R')
            elif color == 'Y':
                ans = dp(i - 1, j, 'B') + dp(i, j - 1, 'R') + dp(i - 1, j, 'R') + dp(i, j - 1, 'B')  - 2 * dp(i -1, j - 1, 'Y')
            elif color == 'B':
                ans = dp(i - 1, j, 'Y') + dp(i, j - 1, 'R') + dp(i - 1, j, 'R') + dp(i, j - 1, 'Y')  - 2 * dp(i -1, j - 1, 'B')
            memo[(i, j, color)] = ans
            return ans

        res = dp(m - 1, n - 1, 'R') + dp(m - 1, n - 1, 'Y') + dp(m - 1, n - 1, 'B')
        return res % (10 ** 9 + 7)

x = Solution()
print(x.numOfWays(3))