class DP:
    def backpack01(self, w, wt, val):  # return max value in weight range
        def dp(i):
            if i <= 0:
                return 0
            res = float('-inf')
            res = dp(i - w) + v
            return res
        return dp(w)

x = DP()
print(x.backpack01(n = 3, W = 4, wt = [2, 1, 3], val = [4, 2, 3]))