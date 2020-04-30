class Solution:
    def canJump(self, nums) -> bool:
        farIndex = [index + value for index, value in enumerate(nums)]

        i = 0
        n = len(farIndex)
        while i < n:
            end = i
            for j in range(i, farIndex[i] + 1):  # 寻找最远点，并作为新搜索区间的end
                if j < n:  # j在farIndex范围内时
                    end = max(end, farIndex[j])
                else:  # j超过farIndex范围时，即可以到达nums尾部了
                    return True
            if end >= n - 1:
                return True
            if end == i:
                return False

        return True

X = Solution()
print(X.canJump([5,9,3,2,1,0,2,3,3,1,0,0]))
