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
    def quicksort(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return arr

        l = 0
        r = len(arr) - 1

        i = l
        j = r
        pivot = arr[i]
        while i < j:
            while i < j and pivot < arr[j]:
                j -= 1
            if i < j:
                arr[i] = arr[j]
                i += 1
            while i < j and arr[i] < pivot:
                i += 1
            if i < j:
                arr[j] = arr[i]
                j -= 1
        arr[i] = pivot
        self.quicksort(arr[l:i])
        self.quicksort(arr[i + 1:r + 1])
        return arr


x = Sort()
print(x.quicksort([5,1,1,2,0,0]))