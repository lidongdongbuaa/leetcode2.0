class Solution:
    def canJump(self, nums) -> bool:
        farIndex = [ind + val for ind, val in enumerate(nums)]

        end = farIndex[0]
        n = len(farIndex)
        i = 0
        while i <= end and i <= n - 1:
            if farIndex[i] > end:
                end = farIndex[i]
            else:
                i += 1
        if i == n:
            return True
        else:
            return False


X = Solution()
print(X.canJump([2,3,1,1,4]))

