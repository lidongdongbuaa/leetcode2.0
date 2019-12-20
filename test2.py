# def AdjustArr(arr, l, r):  # return pivot position
#     i = l
#     j = r
#     x = arr[i]  # 第一个坑
#     while i < j:
#         while i < j and x < arr[j]:  # find smaller val than x
#             j -= 1
#         if i < j:  # 区别1
#             arr[i] = arr[j]
#             # i += 1  #区别2
#         while i < j and arr[i] < x:
#             i += 1
#         if i < j:
#             arr[j] = arr[i]
#             j -= 1
#     arr[i] = x
#     return arr



class Sort:
    def quicksort(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return nums

        l = 0
        r = len(nums) - 1

        i = l
        j = r
        pivot = nums[i]
        while i < j:
            while i < j and pivot < nums[j]:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot
        L = nums[l:i]
        R = nums[i + 1: r + 1]
        nums[l:i] = self.quicksort(L)  # 产生了一部分，就要把这一部分赋值回去，不然不起作用的
        nums[i + 1: r + 1] = self.quicksort(R)
        return nums


x = Sort()
print(x.quicksort([5,1,1,2,0,0]))