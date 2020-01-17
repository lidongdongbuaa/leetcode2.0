
class Solution:
    def singleNumber(self, nums) -> int:
        a = 0
        b = 0
        for elem in nums:
            b = (b ^ elem) & ~a
            a = (a ^ elem) & ~b
        return b

x = Solution()
print(x.singleNumber([0,1,0,1,0,1,99]))