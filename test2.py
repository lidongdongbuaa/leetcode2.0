class Sort:
    def quickSort(self, nums):  # return sorted nums
        if not nums or len(nums) == 1:  # corner case
            return nums

        pivot = nums[0]
        l = []
        r = []
        for elem in nums[1:]:
            if elem < pivot:
                l.append(elem)
            else:
                r.append(elem)
        left = self.quickSort(l)
        right = self.quickSort(r)
        nums = left + [pivot] + right
        return nums

X = Sort()
print(X.quickSort([9,8,7,6,5,4,3,2,1]))