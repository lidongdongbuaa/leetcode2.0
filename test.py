class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        if not nums:  # corner case
            return 0

        prefix = [nums[0]]
        for elem in nums[1:]:
            prefix.append(elem + prefix[-1])

        def binarySearch(target, arr):  # return target index in arr
            l, r = 0, len(arr) - 1
            while l < r:
                mid = l + (r - l) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        res = float('inf')
        n = len(prefix)
        for i in range(n):
            target = s - prefix[i]
            if target > 0:
                j = binarySearch(target, prefix[i + 1:])
                res = min(res, j + i + 1 - i + 1)
            else:
                res = 1


        return res if res != float('inf') else 0

X = Solution()
print(X.minSubArrayLen(4, [1,4,4]))