class Solution:
    def quickSort(self, arr):
        if len(arr) == 0 or len(arr) == 1:  # corner case
            return arr

        i = l = 0
        j = r = len(arr) - 1
        pivot = arr[i]

        while i < j:
            while i < j and pivot < arr[j]:  # 扫描一段去寻找合适的值, 循环条件是正常的顺序（pivot < arr[j]），若发现异常，则跳出更换i和j
                j -= 1
            arr[i] = arr[j]  # 搜寻一段之后，找到值，再替换
            while i < j and arr[i] <= pivot:
                i += 1
            arr[j] = arr[i]
        arr[i] = pivot  # i in center, give it pivot
        arr[:i] = self.quickSort(arr[:i])  # L part = arr[0:i] < pivot
        arr[i + 1:] = self.quickSort(arr[i + 1:])  # R part = arr[i + 1, j] > pivot
        return arr


class SortList:
	# Merge sort
	def mergeSort(self, arr):
		if len(arr) == 0 or len(arr) == 1:
			return

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

			#             while i < len(L):  # process left data in L part
			#                 arr[k] = L[i]
			#                 k += 1
			#                 i += 1
			if i < len(L):
				arr[k:] = L[i:]

			#             while j < len(R):  # process right data in R part
			#                 arr[k] = R[j]
			#                 k += 1
			#                 j += 1
			if j < len(R):
				arr[k:] = R[j:]

		return arr


x = SortList()
print(x.mergeSort([9, 8, 7, 4, 5, 6, 3, 2, 1]))


y = Solution()
print(y.quickSort([5,1,1,2,0,0]))