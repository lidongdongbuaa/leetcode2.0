class Solution:
    def subsets(self, nums):
        size = len(nums)
        n = 1 << size  # 位掩码个数, 即总结果的元素个数
        res = []
        for i in range(n):
            temp = []
            for j in range(size):
                if i >> j & 1:  # 根据当前位掩码是否为1决定是否加入数组该位
                    temp.append(nums[j])
            res.append(temp)
        return res

x = Solution()
x.subsets([1,2,3])