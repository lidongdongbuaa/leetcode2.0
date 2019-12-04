class SortList:
    # Merge sort
    def mergeSort(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return

        if len(arr) >= 2:
            mid = len(arr) // 2  # find the mid of the array
            L = arr[:mid]  # divide the array elements
            R = arr[mid:]  # into 2 haves

            self.mergeSort(L)  # Sorting the first half
            self.mergeSort(R)  # Sorting the second half

            i = j = k = 0

            while i < len(L) and j < len(R):  # copy data to temp arrays L and R
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):  # process left data in L part
                arr[k] = L[i]
                k += 1
                i += 1

            while j < len(R):  # process right data in R part
                arr[k] = R[j]
                k += 1
                j += 1

        return arr



    def showSort(self, arr):
        self.mergeSort2(arr)
        print(arr)

    def mergeSort2(self, arr):
        if len(arr) < 2:  # arr == [] or just one element
            return

        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        self.mergeSort2(L)
        self.mergeSort2(R)

        i =  j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1


        if len(L) < len(R):
            for i in range(j, len(R)):
                arr[k] = R[i]
                k += 1
        else:
            for j in range(i, len(L)):
                arr[k] = L[j]
                k += 1

        return arr




x = SortList()
print(x.mergeSort([3,5,1,0]))