class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        if k >= len(arr):
            return arr

        l, r = 0, len(arr) - k
        while l <= r:
            mid = l + (r - l) // 2
            if x - arr[mid] < arr[mid + k - 1] - x:
                r = mid - 1
            elif x - arr[mid] == arr[mid + k - 1] - x:
                r = mid - 1
            else:
                l = mid + 1
        return arr[l:l + k]


x = Solution()
print(x.findClosestElements([0,1,2,2,2,3,6,8,8,9],1,9))