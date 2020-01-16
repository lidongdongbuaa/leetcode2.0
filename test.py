class Solution:
    def totalHammingDistance(self, nums) -> int:
        res = 0
        for i in range(32):
            t1 = 0
            t2 = 0
            for elem in nums:
                if elem >> i & 1 == 1:
                    t1 += 1
                else:
                    t2 += 1
            res += t1 * t2
        return res

x = Solution()
print(x.totalHammingDistance([4,14,4,14]))