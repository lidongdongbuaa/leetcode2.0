class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                l = mid + 1
            elif arr[mid] > x:
                r = mid - 1
        return l



