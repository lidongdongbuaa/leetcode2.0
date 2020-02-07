# 问题？k的作用，k每次都更新为0，不久让arr又重头开始了吗
class SortList:
    # Merge sort
    def mergeSort(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return arr

        if len(arr) >= 2:
            # 普通划分
            mid = len(arr) // 2  # find the mid of the array
            L = arr[:mid]  # divide the array elements
            R = arr[mid:]  # into 2 haves

            # 递归划分
            self.mergeSort(L)  # Sorting the first half
            self.mergeSort(R)  # Sorting the second half

            # 合并， input: 两个已排序的list，L，R.过程：对L，R进行合并排序。output：合并完成后的一个list
            i = j = k = 0
            while i < len(L) and j < len(R):  # copy data to temp arrays L and R
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            if i < len(L):
                arr[k:] = L[i:]

            if j < len(R):
                arr[k:] = R[j:]

        return arr


x = SortList()
print(x.mergeSort([4, 3, 2, 1]))