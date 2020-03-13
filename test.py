class Solution:
    def findPeakElement(self, nums: List[int]) -> int:  # return peak value's index
        if nums is None:
            return None

        l, r = 0, len(nums) - 1
        while l < r:  # 在l = r时，退出，找到这个点
            mid = l + (r - l) // 2
            if nums[mid] <= nums[mid + 1]:
                l = mid + 1
            if nums[mid] > nums[mid + 1]:
                r = mid

        return l

x = Solution()
print(x.findPeakElement([1,2,1,3,5,6,4]))